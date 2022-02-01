from enum import unique
from django import forms
from django.forms import fields, widgets
from .models import Users, UserProfiles
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

import re
from datetime import datetime


# ユーザ登録
class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザ名', required=True)
    email = forms.EmailField(label='メールアドレス', required=True)
    password1 = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    password2 = forms.CharField(label='パスワード(確認)', widget=forms.PasswordInput)
    
    class Meta:
        # モデルの指定及び表示するフィールド
        model = Users
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_password2(self):
        # パスワードの確認
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('パスワードが一致しません')
        return password2
        
    def save(self, commit=False):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        passsword1 = self.cleaned_data['password1']
        meijo_email = '@ccmailg.meijo-u.ac.jp'
        if not re.search(f'{ meijo_email }\Z', email):
            raise ValidationError('名城大学のメールアドレスを入力してください')
        user.set_password(passsword1)
        user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フォームにCSSをあてる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# ユーザログイン
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態維持', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フォームにCSSをあてる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    

# profile作成フォーム
class ProfileForm(forms.ModelForm):
    picture = forms.FileField(label='プロフィール写真')
    nickname = forms.CharField(label='ニックネーム')
    introduction = forms.CharField(label='自己紹介', widget=forms.Textarea(attrs={'rows':4, 'cols':15}))
    
    class Meta:
        model = UserProfiles
        fields = ['picture', 'nickname', 'introduction']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フォームにCSSをあてる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# profile更新フォーム
class ProfileUpdateForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        obj = super(ProfileUpdateForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj
    
    class Meta:
        model = UserProfiles
        fields = ['picture', 'nickname', 'introduction']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'