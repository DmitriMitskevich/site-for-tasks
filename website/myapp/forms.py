from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={'placeholder': 'Введите название', 'class': 'form-control'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   }
