from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Klass(models.Model):
    name=models.CharField(max_length=10, unique=True)
    room=models.CharField(max_length=3)
    grade=models.CharField(max_length=10)
    teacher=models.CharField(max_length=25)
    
    class Meta:
        verbose_name='Class'
        verbose_name_plural='Classes'
    
    def __str__(self):
        return '%s Gr. %s in Rm. %s' %(self.teacher, self.grade, self.room)

class KlassForm(forms.ModelForm):
    class Meta:
        model=Klass
        fields=['name','room','grade','teacher']

    
class Student(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    email=models.EmailField(blank=True)
    comment=models.TextField(blank=True)
    klass=models.ForeignKey(Klass, on_delete=models.CASCADE)
    
    prefix='student'
    
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','klass','phone','email','comment',]
        labels={"klass":_("Class"),}

class StudentDeleteForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','phone']
        
class TeacherForm(forms.ModelForm):
    notavail=forms.BooleanField(required=False, label='Not Available')
    first_name=forms.CharField(max_length=25, required=False)
    last_name=forms.CharField(max_length=25, required=False)
    phone=forms.CharField(max_length=12, required=False)
    klass=forms.ModelChoiceField(queryset=Klass.objects.all(),empty_label=None, required=False, label='Class')    
    
    prefix='teacher'
    
    class Meta:
        model=Student
        fields=['first_name','last_name','klass','phone','email','comment','notavail']
        