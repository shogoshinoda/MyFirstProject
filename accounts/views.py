from datetime import datetime
from re import A
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from .models import UserActivateTokens, UserProfiles, Users
from .forms import ProfileForm, RegistForm, UserLoginForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

# ユーザ登録
class RegistUserView(CreateView):
    template_name = 'accounts/regist.html'
    form_class = RegistForm

# ユーザ登録確認メール送信完了
class ConfirmEmailView(TemplateView):
    template_name = 'accounts/confirm_email.html'

# ユーザアクティベイト
def activate_user(request, token):
    user_activate_token = UserActivateTokens.objects.activate_user_by_token(token)
    return render(
        request, 'accounts/activate_user.html'
    )


# ユーザログイン
class UserLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        next_url = request.POST.get('next')
        if user is not None and user.is_active:
            login(request, user)
        else:
            raise ValueError('メルアドレスもしくはパスワードがまちがっています')
        # ログインしないといけない画面に行ってしまった時そのページに戻るよう
        if next_url:
            return redirect(next_url)
        # プロフィールが存在した時ホーム、存在しない時プロフィール作成画面
        try:
            UserProfiles.objects.get(user_id=self.request.user.id)
            return redirect('boards:board_list')
        except:
            return redirect('accounts:create_profile')

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(10368000)# ログイン状態保持にチェックがある場合120日ログイン状態保持
        return super().form_valid(form)


# ログアウト
class UserLogoutView(LogoutView):
    pass

# プロフィール作成
class CreateProfileView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/create_profile.html'
    model = UserProfiles
    success_url = reverse_lazy('boards:board_list')
    fields = ['picture', 'nickname', 'introduction']

    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        user = get_object_or_404(Users, pk=self.request.user.id)
        form.instance.user = user
        return super(CreateProfileView, self).form_valid(form)

    def get_initial(self, **kwargs):
        initial = super(CreateProfileView, self).get_initial(**kwargs)
        return initial
    
