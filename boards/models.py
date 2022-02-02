from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Users
from django.dispatch import receiver
import os
from django.utils import timezone


# 提示版のマネージャー
class BoardsManager(models.Manager):
    def filter_by_boards(self, user_id):
        return self.filter(user_id=user_id).all()
    
    def count_boards(self, user):
        return self.filter(user=user).all().count()

# 提示版
class Boards(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )
    user_picture = models.FileField(upload_to='boards/')
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    boards_picture = models.FileField(upload_to='boards/', null=True)
    description = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=datetime.now())
    update_at = models.DateTimeField(default=datetime.now())

    objects = BoardsManager()

    class Meta:
        db_table = 'boards'
# データが削除されたらmediaのboards_pictureが消える
@receiver(models.signals.post_delete, sender=Boards)
def delete_picture(sender, instance, **kwargs):
    if instance.boards_picture:
        if os.path.isfile(instance.boards_picture.path):
            os.remove(instance.boards_picture.path)


