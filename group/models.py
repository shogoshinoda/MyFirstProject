from django.db import models
from accounts.models import Users

# グループ
class Group(models.Model):
    author = models.ForeignKey(
       Users, on_delete=models.CASCADE
    )
    group_name = models.CharField(max_length=150)
    group_picture = models.FileField(upload_to='group_picture/')
    group_comment = models.CharField(max_length=255)

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.group_name


# グループメンバー
class GroupMembers(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'group_members'


# グループ活動
class GroupActivities(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE
    )
    group_picture = models.FileField(upload_to='group_activities')
    group_comment = models.CharField(max_length=150)

    class Meta:
        db_table = 'group_activities'