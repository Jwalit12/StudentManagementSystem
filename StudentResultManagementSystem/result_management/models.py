from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=False)

    def __str__(self):
        return f"{self.first_name} {self.family_name}"

    def clean(self):
        age_limit = timezone.now().date() - timezone.timedelta(days=(365.25 * 10))  # 10 years old
        if self.date_of_birth > age_limit:
            raise ValidationError("The student must be at least 10 years old.")

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score_choices = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    score = models.CharField(max_length=1, choices=score_choices)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.score}"