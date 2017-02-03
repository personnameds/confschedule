from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Klass, KlassForm
from homepage.views import KlassListMixin
from schedule.models import SchoolScheduleDetails, Slot, KlassScheduleDetails, KlassScheduleForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings

class KlassCreateView(PermissionRequiredMixin, KlassListMixin, CreateView):
    model=Klass
    form_class=KlassForm
    template_name='classlists/add_klass_form.html'
    permission_required='classlists.add_klass'
    
    def form_valid(self, form):
        new_klass=form.save()
        school_schedule=SchoolScheduleDetails.objects.get(name=settings.SCHOOL_NAME)
        slot_length=school_schedule.slot_length
        
        ##Create PM Slots for a Class
        slot_start=school_schedule.pm_start
        for i in range(0,school_schedule.num_pm_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
            new_slot=Slot.objects.create(klass=new_klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='pm',
                                         not_available=False)
            slot_start=slot_end

        ##Create PM Slots for a Class
        slot_start=school_schedule.am_start
        for i in range(0,school_schedule.num_am_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
            new_slot=Slot.objects.create(klass=new_klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='am',
                                         not_available=False)
            slot_start=slot_end

        return HttpResponseRedirect(reverse_lazy('homepage-view'))

class KlassScheduleCreateView(PermissionRequiredMixin, KlassListMixin, CreateView):
    model=KlassScheduleDetails
    form_class=KlassScheduleForm
    template_name='schedule/klassschedule.html'
    permission_required='classlists.add_klass'
    
    def form_valid(self, form):
        new_schedule=form.save()
        klass=new_schedule.klass
        
        ##Delete old slots
        Slot.objects.filter(klass=klass).delete()
        
        slot_length=new_schedule.slot_length
        ##Create PM Slots for a Class
        slot_start=new_schedule.pm_start
        for i in range(0,new_schedule.num_pm_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
            new_slot=Slot.objects.create(klass=klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='pm',
                                         not_available=False)
            slot_start=slot_end

        ##Create PM Slots for a Class
        slot_start=new_schedule.am_start
        for i in range(0,new_schedule.num_am_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
            new_slot=Slot.objects.create(klass=klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='am',
                                         not_available=False)
            slot_start=slot_end

        return HttpResponseRedirect(reverse_lazy('homepage-view'))