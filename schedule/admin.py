from django.contrib import admin
from .models import Standard_Day_Schedule, Alt_Klass_Schedule, Slot

class Standard_Day_ScheduleAdmin(admin.ModelAdmin):
    list_display=('int_date','start_time','slot_length','num_slots')

# class KlassScheduleDetailsAdmin(admin.ModelAdmin):
#     list_display=('klass','num_pm_slots','num_am_slots','slot_length','am_start','pm_start')
#     list_filter=('klass__name',)
#     
#     def has_add_permission(self, request):
#         return False
#         
#     def klass_name(self, obj):
#         return obj.klass.name


class SlotAdmin(admin.ModelAdmin):
    list_display=('klass_name','int_date', 'start','end','student','not_available')
    list_filter=('klass__name','int_date')
    ordering=['klass','int_date','start'] 
    
    def klass_name(self, obj):
        return obj.klass.name

admin.site.register(Standard_Day_Schedule, Standard_Day_ScheduleAdmin)
admin.site.register(Alt_Klass_Schedule)
admin.site.register(Slot,SlotAdmin)
