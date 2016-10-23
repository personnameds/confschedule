from django.db import models
from classlists.models import Klass, Student

class SchoolScheduleDetails(models.Model):
    num_pm_slots=models.PositiveSmallIntegerField()
    num_am_slots=models.PositiveSmallIntegerField()
    slot_length=models.PositiveSmallIntegerField()
    am_start=models.TimeField()
    pm_start=models.TimeField()
    
    class Meta:
        verbose_name='School Schedule'
        verbose_name_plural='School Schedule'

# class KlassScheduleDetails(models.Model):
#     num_pm_slots=models.PositiveSmallIntegerField(blank=True)
#     num_am_slots=models.PositiveSmallIntegerField(blank=True)
#     slot_length=models.PositiveSmallIntegerField(blank=True)
#     am_start=models.TimeField(blank=True)
#     pm_start=models.TimeField(blank=True)
#     klass=models.ForeignKey(Klass, on_delete=models.CASCADE)
# 
#     class Meta:
#         verbose_name='Class Schedule'
#         verbose_name_plural='Class Schedules'

class Slot(models.Model):
    klass=models.ForeignKey(Klass, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    start=models.TimeField()
    end=models.TimeField()
    am_pm=models.CharField(max_length=2)

       
    
    
