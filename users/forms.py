from django import forms
from django.db.models import fields
from django.forms.forms import Form
from accounts.models import Users
from .models import FollowFollowerUser

class FollowForm(forms.ModelForm):
    follow_action = forms.BooleanField()


    class Meta:
        model = FollowFollowerUser
        fields = ['follow_action',]
    

class ChangeFollowForm(forms.Form):
    change_follow_action = forms.BooleanField()

    class Meta:
        model = FollowFollowerUser
        fields = ['change_follow_action']