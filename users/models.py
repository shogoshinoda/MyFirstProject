from django.db import models
from django.db.models.query_utils import Q
from accounts.models import Users

# User
class UserActivities(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )
    user_picture = models.FileField(upload_to='group_activities')
    user_comment = models.CharField(max_length=150)

    class Meta:
        db_table = 'user_activities'


# follow Manager
class FollowFollowerUserManager(models.Manager):

    def count_follow(self, follow_user):
        return self.filter(follow_user=follow_user).all().count()
    
    def count_follower(self, follower_user):
        return self.filter(follower_user=follower_user).all().count()


# follow
class FollowFollowerUser(models.Model):
    follow_user = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )
    follower_user = models.IntegerField()
    objects = FollowFollowerUserManager()
    

    class Meta:
        db_table = 'follow_follower_user'


