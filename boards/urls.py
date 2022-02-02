from django.urls import path
from .views import(
    BoardDeleteView, BoardListView, CreateBoardsView, BoardUpdateView
)

app_name = 'boards'

urlpatterns = [
    path('board_list/', BoardListView.as_view(), name='board_list'),
    path('create_boards/', CreateBoardsView.as_view(), name='create_boards'),
    path('update_board/<int:pk>', BoardUpdateView.as_view(), name='update_board'),
    path('delete_board/<int:pk>', BoardDeleteView.as_view(), name='delete_board'),
]