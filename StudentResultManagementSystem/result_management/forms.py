# result_management/forms.py
from django import forms
from .models import Student, Course, Result
from datetime import date, timedelta

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'family_name', 'date_of_birth', 'email']

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')

        min_birth_date = date.today() - timedelta(days=10*365)
        if date_of_birth > min_birth_date:
            raise forms.ValidationError("The student must be at least 10 years old.")
        return date_of_birth

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'course', 'score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Select a Student'
        self.fields['course'].empty_label = 'Select a Course'