from django.contrib import admin
from .models import SchoolScheduleDetails, Slot, KlassScheduleDetails

class SchoolScheduleDetailsAdmin(admin.ModelAdmin):
    list_display=('num_pm_slots','num_am_slots','slot_length','am_start','pm_start')
    
    def klass_name(self, obj):
        return obj.klass.name

class KlassScheduleDetailsAdmin(admin.ModelAdmin):
    list_display=('klass','num_pm_slots','num_am_slots','slot_length','am_start','pm_start')
    list_filter=('klass__name',)
    
    def has_add_permission(self, request):
        return False
        
    def klass_name(self, obj):
        return obj.klass.name

class SlotAdmin(admin.ModelAdmin):
    list_display=('klass_name','student','start','end','am_pm','not_available')
    list_filter=('klass__name','am_pm')
    ordering=['klass','start'] 
    
    def klass_name(self, obj):
        return obj.klass.name


admin.site.register(SchoolScheduleDetails, SchoolScheduleDetailsAdmin)
admin.site.register(KlassScheduleDetails, KlassScheduleDetailsAdmin)
admin.site.register(Slot,SlotAdmin)
