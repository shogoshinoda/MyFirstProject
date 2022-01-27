from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from datetime import date, datetime
from accounts.models import Users, UserProfiles
from .models import Boards
from .forms import BoardUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

class BoardListView(LoginRequiredMixin, ListView):
    model = Boards
    template_name = 'boards/board_list.html'


# 提示版作成画面
class CreateBoardsView(LoginRequiredMixin, CreateView):
    model = Boards
    template_name = 'boards/create_boards.html'
    fields = ['title', 'description', 'boards_picture']
    success_url = reverse_lazy('boards:board_list')

    def form_valid(self, form):
        user = get_object_or_404(Users, pk=self.request.user.id)
        profile = get_object_or_404(UserProfiles, user_id=user.id)
        form.instance.user_picture = profile.picture
        form.instance.name = profile.nickname
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = user
        return super(CreateBoardsView, self).form_valid(form)


# 提示版更新画面
class BoardUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'boards/update_board.html'
    model = Boards
    form_class = BoardUpdateForm
    success_message = '更新完了しました'
    success_url = reverse_lazy('boards:board_list')


# 削除画面
class BoardDeleteView(DeleteView):
    model = Boards
    template_name = 'boards/delete_board.html'
    success_url = reverse_lazy('boards:board_list')

    
