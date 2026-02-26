from django import forms
from .models import Student

COURSE_CHOICES = [
    ('', '-- Select a course --'),
    ('Full Stack Software Development', 'Full Stack Software Development'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Machine Learning', 'Machine Learning'),
]

class studentForm(forms.ModelForm):
    course = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select or type a course',
            'list': 'course-list'
        })
    )
    
    class Meta:
        model = Student
        fields =['first_name','last_name','age','course','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }