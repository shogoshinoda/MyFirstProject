from django.urls import path
from .views import(
    UserHomeView, follow, clear_follow
)

app_name = 'users'

urlpatterns = [
    path('user_home/<str:username>', UserHomeView.as_view(), name='user_home'),
    path('follow/<str:username>', follow, name='follow' ),
    path('clear_follow/<str:username>', clear_follow, name='clear_follow'),
]