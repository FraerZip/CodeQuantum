from .models import Courses, Lesson
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django import forms

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'type_cours', 'period', 'exp', 'description', 'price_in_month', 'full_price', 'content']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            "type_cours": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип курса'
            }),
            "period": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Период курса'
            }),
            "exp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Требуемый опыт'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание курса'
            }),
            "price_in_month": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена курса за месяц'
            }),
            "full_price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полная цена курса'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание курса'
            }),

        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'order']
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название урока'
            }),
            "content": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание урока'
             }),
            "order": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Порядок'
            }),
        }