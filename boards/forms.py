from django import forms
from .models import Boards
from datetime import datetime

#　提示版更新フォーム
class BoardUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Boards
        fields = ['title', 'description', 'boards_picture']
    
    def save(self, *args, **kwargs):
        obj = super(BoardUpdateForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj