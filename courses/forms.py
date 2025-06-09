from .models import CourseModel
from django import forms

class CourseAddEditForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان دوره'}),
            'number_of_sessions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تعداد جلسات دوره'}),
            'age_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'گروه سنی دوره'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قیمت دوره'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'بارگذاری پوستر دوره'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات دوره', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'انتخاب دسته‌بندی دوره'}),
        }

