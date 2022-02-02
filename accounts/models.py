from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta
from django.utils import timezone


# ユーザマネージャー
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            email=email,
            username=username,
            password=password,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def filter_by_username(self, username):
        return self.filter(username=username).first()

    def filter_by_id(self, id):
        return self.filter(id=id).first()

# ユーザ登録
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:confirm_email')


# ユーザ登録トークンのマネージャー
class UserActivateTokensManager(models.Manager):
    
    # ユーザをアクティベイトする処理
    def activate_user_by_token(self, token):
        user_activate_token = self.filter(
            token=token,
            expired_at__gte=datetime.now() #　現在時刻よりも大きいものを取り出す（トークン有効時間設定）
        ).first()
        user = user_activate_token.user
        user.is_active = True
        user.save()


# ユーザ登録トークン
class UserActivateTokens(models.Model):
    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE
    )

    objects = UserActivateTokensManager()

    class Meta:
        db_table = 'user_activate_tokens'

# トークンの発行
@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    user_activate_token = UserActivateTokens.objects.create(
        user=instance, 
        token=str(uuid4()), # 標準ライブラリで発行
        expired_at=datetime.now() + timedelta(days=1) # 1日後に削除
    )
    print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')


# プロフィールのマネージェー
class UserProfilesManager(models.Manager):
    def filter_by_profile(self, user_id):
        return self.filter(user_id=user_id).first()

# プロフィール
class UserProfiles(models.Model):
    picture = models.FileField(upload_to='picture/', null=True, )
    nickname = models.CharField(max_length=150)
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE
    )
    introduction = models.TextField(null=True, blank=True, max_length=255)
    create_at = models.DateTimeField(default=datetime.now())
    update_at = models.DateTimeField(default=datetime.now())

    objects = UserProfilesManager()

    class Meta:
        db_table = 'plofiles'

    