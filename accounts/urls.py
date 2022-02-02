from django.urls import path
from .views import(
    CreateProfileView, RegistUserView, ConfirmEmailView, UpdateProfileView, activate_user, UserLoginView, UserLogoutView
)

app_name = 'accounts'
urlpatterns = [
    path('confirm_email/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('activate_user/<uuid:token>', activate_user, name='activate_user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('update_profile/<int:pk>', UpdateProfileView.as_view(), name='update_profile'),
]