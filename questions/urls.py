from django.urls import path
from .views import(
    QuestionListView, SubjectListView, LectureListView
)


app_name = 'questions'

urlpatterns = [
    path('subject_list/', SubjectListView.as_view(), name='subject_list'),
    path('lecture_list/<int:subject_id>', LectureListView.as_view(), name='lecture_list'),
    path('question_list/<int:lecture_id>', QuestionListView.as_view(), name='question_list'),
]