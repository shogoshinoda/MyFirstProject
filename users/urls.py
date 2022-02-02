from django.urls import path
from .views import(
    UserHomeView, follow, clear_follow, FollowListView,
    FollowerListView
)

app_name = 'users'

urlpatterns = [
    path('user_home/<str:username>', UserHomeView.as_view(), name='user_home'),
    path('follow/<str:username>', follow, name='follow' ),
    path('clear_follow/<str:username>', clear_follow, name='clear_follow'),
    path('follow_list/<str:username>', FollowListView.as_view(), name='follow_list'),
    path('follower_list/<str:username>', FollowerListView.as_view(), name='follower_list'),
]