from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserProfiles, Users
from boards.models import Boards
from .forms import ChangeFollowForm, FollowForm
from .models import FollowFollowerUser
from django.urls import reverse_lazy


class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_home.html'

    def get(self, *args, **kwargs):
        username = self.kwargs.get('username')
        try:
            Users.objects.get(username=username)
        except:
            return redirect('boards:board_list')
        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Users.objects.filter_by_username(username=self.kwargs.get('username'))
        profile = UserProfiles.objects.filter_by_profile(user_id=user.id)
        boards =  Boards.objects.filter_by_boards(user_id=user.id)
        follow_num = FollowFollowerUser.objects.count_follow(follow_user=user.id)
        follower_num = FollowFollowerUser.objects.count_follower(follower_user=user.id)
        boards_num = Boards.objects.count_boards(user=user)
        self_user = Users.objects.filter_by_id(id=self.request.user.id)
        if user == self_user:
            context['follow'] = 'self'
        elif FollowFollowerUser.objects.filter(follow_user=self_user.id, follower_user=user.id):
            context['follow'] = 'followed'
        else:
            context['follow'] = 'follow'
        context['author_username'] = user.username
        context['profile'] = profile
        context['boards'] = boards
        context['follow_num'] = follow_num
        context['follower_num'] = follower_num
        context['boards_num'] = boards_num
        return context


def follow(request, username):
    self_user = Users.objects.filter_by_id(id=request.user.id)
    user = Users.objects.filter_by_username(username=username)
    if FollowFollowerUser.objects.filter(follow_user=self_user.id, follower_user=user.id):
        return redirect('users:user_home', username)
    follow = FollowFollowerUser(
        follow_user = self_user,
        follower_user = user.id
    )
    follow.save()
    return redirect('users:user_home', username)

def clear_follow(request, username):
    self_user = Users.objects.filter_by_id(id=request.user.id)
    user = Users.objects.filter_by_username(username=username)
    clear_follow = FollowFollowerUser.objects.filter(follow_user=self_user.id, follower_user=user.id)
    clear_follow.delete()
    return redirect('users:user_home', username)


class FollowListView(LoginRequiredMixin, TemplateView):

    template_name = 'users/follow_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        user = Users.objects.get(username=username)
        follow_users_id = FollowFollowerUser.objects.filter(follow_user_id=user.id)
        follow_users = []
        for follow_user_id in follow_users_id:
            try:
                follow_user = Users.objects.get(id=follow_user_id.follower_user)
            except:
                pass
            if follow_user:
                follow_users.append(follow_user)
        context['follow_users'] = follow_users
        return context


class FollowerListView(LoginRequiredMixin, TemplateView):

    template_name = 'users/follower_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        user = Users.objects.get(username=username)
        follower_users_id = FollowFollowerUser.objects.filter(follower_user=user.id)
        follower_users = []
        for follower_user_id in follower_users_id:
            print(follower_user_id)
            try:
                follower_user = Users.objects.get(id=follower_user_id.follow_user_id)
            except:
                pass
            if follower_user:
                follower_users.append(follower_user)
        context['follower_users'] = follower_users
        return context
