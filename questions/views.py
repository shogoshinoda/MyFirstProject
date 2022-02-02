from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Department, Lectures, Questions, Subjects
from django.contrib import messages
from django.db.models import Q

from functools import reduce
from operator import and_


class SubjectListView(LoginRequiredMixin, TemplateView):

    template_name = 'questions/subject_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departments = []
        subjects = []
        for department in Department.objects.all():
            departments.append(department)
        for subject in Subjects.objects.all():
            subjects.append(subject)
        context['departments'] = departments
        context['subjects'] = subjects
        return context

class LectureListView(LoginRequiredMixin, ListView):
    model = Lectures 
    template_name = 'questions/lecture_list.html'

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        queryset = Lectures.objects.filter(subject_id=subject_id)
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i

            query = reduce(
                            and_, [Q(lecture__icontains=q) | Q(lecture_number__icontains=q) | Q(lecture_teacher__icontains=q) for q in q_list]
                       )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = int(self.kwargs['subject_id'])
        context['subject_id'] = subject_id
        return context


class QuestionListView(LoginRequiredMixin, ListView):

    model = Questions
    template_name = 'questions/question_list.html'
    
    def get_queryset(self):
        lecture_id = self.kwargs['lecture_id']
        queryset = Questions.objects.filter(lecture_id=lecture_id)
        return queryset




