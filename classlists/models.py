from django.db import models
from django.forms import ModelForm
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

class KlassForm(ModelForm):
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
    
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','klass','phone','email','comment',]
        labels={"klass":_("Class"),}

class StudentDeleteForm(ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','phone']