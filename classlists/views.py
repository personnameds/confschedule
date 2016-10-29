from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Klass, KlassForm
from homepage.views import KlassListMixin
from schedule.models import SchoolScheduleDetails, Slot
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
from django.contrib.auth.mixins import PermissionRequiredMixin

class KlassCreateView(PermissionRequiredMixin, KlassListMixin, CreateView):
    model=Klass
    form_class=KlassForm
    template_name='classlists/add_klass_form.html'
    permission_required='classlists.add_klass'
    
    def form_valid(self, form):
        new_klass=form.save()
        school_schedule=SchoolScheduleDetails.objects.get(pk=1)
        
        ##Create PM Slots for a Class
        slot_start=school_schedule.pm_start
        for i in range(0,school_schedule.num_pm_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=10)).time()
            new_slot=Slot.objects.create(klass=new_klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='pm')
            slot_start=slot_end

        ##Create PM Slots for a Class
        slot_start=school_schedule.am_start
        for i in range(0,school_schedule.num_am_slots):
            slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=10)).time()
            new_slot=Slot.objects.create(klass=new_klass,
                                         start=slot_start,
                                         end=slot_end,
                                         am_pm='am')
            slot_start=slot_end

        return HttpResponseRedirect(reverse_lazy('homepage-view'))
