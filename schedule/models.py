from django.db import models
from django.forms import ModelForm, SelectDateWidget, SplitDateTimeWidget
from classlists.models import Klass, Student

class Standard_Day_Schedule(models.Model):
	int_date=models.DateField()
	start_time=models.TimeField()
	slot_length=models.PositiveSmallIntegerField()
	num_slots=models.PositiveSmallIntegerField()
	
	class Meta:
		verbose_name='Standard Schedule'
		verbose_name_plural='Standard Schedules'

class Alt_Klass_Schedule(models.Model):
    klass=models.ForeignKey(Klass, on_delete=models.CASCADE)
    int_date=models.DateField()
    start_time=models.TimeField(help_text='24 hr time')
    slot_length=models.PositiveSmallIntegerField(help_text='min')
    num_slots=models.PositiveSmallIntegerField()

    class Meta:
        verbose_name='Alternate Class Schedule'
        verbose_name_plural='Alternate Class Schedules'

class Slot(models.Model):
    klass=models.ForeignKey(Klass, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    int_date=models.DateField()
    start=models.TimeField()
    end=models.TimeField()
    not_available=models.BooleanField()

class Alt_Klass_Schedule_FormTwo(ModelForm):
    class Meta:
        model=Alt_Klass_Schedule
        fields=['klass','int_date','start_time','slot_length','num_slots']
        widgets={'int_date':SelectDateWidget(),}

##### NOT UPDATED YET
class SlotForm(ModelForm):
    class Meta:
        model=Slot
        fields=['not_available',]
    
