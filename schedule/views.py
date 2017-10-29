from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .models import SchoolScheduleDetails, Slot, SlotForm
from classlists.models import Klass, Student, StudentForm, StudentDeleteForm, TeacherForm
from homepage.views import KlassListMixin
from django.urls import reverse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate,Table, Paragraph
from reportlab.lib.styles import ParagraphStyle
from django.http import HttpResponse



class KlassScheduleView(KlassListMixin, TemplateView):
    template_name='schedule/schedule.html'

    def get_context_data(self, **kwargs):
        context=super(KlassScheduleView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        context['klass']=klass
        context['klass_pm_schedule']=Slot.objects.filter(klass=klass, am_pm='pm').order_by('start')
        context['klass_am_schedule']=Slot.objects.filter(klass=klass, am_pm='am').order_by('start')
        return context

class BookSlotView(KlassListMixin, CreateView):
    model=Student
    template_name='schedule/bookslot.html'
    permission_required='classlists.add_klass'

    def get_context_data(self, **kwargs):
        context=super(BookSlotView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        context['klass']=klass
        context['slot']=slot
        return context

    def get_form_class(self):
        if self.request.user.is_authenticated():
            form_class=TeacherForm
        else:
            form_class=StudentForm
        return form_class
    
    def get_initial(self):
        initial=super(BookSlotView, self).get_initial()
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        initial['klass']=klass
        return initial
    
    def form_valid(self, form):
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        if form.prefix=='teacher':
            if form.cleaned_data['notavail']==True:
                slot.not_available=True
            else:
                new_student=form.save()
                slot.student=new_student
                slot.not_available=False
        else:
            new_student=form.save()
            slot.student=new_student
            slot.not_available=False
        slot.save()
        return super(BookSlotView, self).form_valid(form)
        
    def get_success_url(self):
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        return reverse('klass-schedule-view', args=[klass.pk])

class EditSlotView(KlassListMixin, FormView):
    model=Student
    form_class=StudentDeleteForm
    template_name='schedule/editslot.html'

    def get_context_data(self, **kwargs):
        context=super(EditSlotView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        student=Student.objects.get(pk=self.kwargs['pk'])
        context['klass']=klass
        context['slot']=slot
        context['student']=student
        return context

    def get_initial(self):
        initial=super(EditSlotView, self).get_initial()
        student=Student.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_authenticated():
            initial['first_name']=student.first_name
            initial['last_name']=student.last_name
            initial['phone']=student.phone  
        return initial
    
    def form_valid(self, form):
        form_student=form.save(commit=False)
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        student=Student.objects.get(pk=self.kwargs['pk'])
        if form_student.first_name == student.first_name and form_student.last_name == student.last_name and form_student.phone == student.phone:
            student.delete()
            slot.student=None
            slot.not_available=False
            slot.save()
        else:
            ## should be done in clean method
            form.add_error(None, "Are you sure this is your spot? Something does not match. Please try again or click Cancel. ")
            return super(EditSlotView, self).form_invalid(form)
        return super(EditSlotView, self).form_valid(form)
    
    def get_success_url(self):
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        return reverse('klass-schedule-view', args=[klass.pk])

class ClearSlotView(KlassListMixin, FormView):
    model=Slot
    form_class=SlotForm
    template_name='schedule/clearslot.html'
    
    def get_context_data(self, **kwargs):
        context=super(ClearSlotView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        context['klass']=klass
        context['slot']=slot
        return context

    def form_valid(self, form):
        form_slot=form.save(commit=False)
        slot=Slot.objects.get(pk=self.kwargs['slot'])
        if form_slot.not_available:
            slot.not_available=False
        else:
            slot.not_available=True
        slot.save()
        return super(ClearSlotView, self).form_valid(form)
    
    def get_success_url(self):
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        return reverse('klass-schedule-view', args=[klass.pk])

class PrintScheduleView(KlassListMixin, TemplateView):
    template_name='schedule/print.html'
    
    def get_context_data(self, **kwargs):
        context=super(PrintScheduleView, self).get_context_data(**kwargs)
        klass=Klass.objects.get(pk=self.kwargs['klass'])
        context['klass']=klass
        context['klass_pm_schedule']=Slot.objects.filter(klass=klass, am_pm='pm').order_by('start')
        context['klass_am_schedule']=Slot.objects.filter(klass=klass, am_pm='am').order_by('start')
        return context

def PrintPDFView(request, klass):
    klass=Klass.objects.get(pk=klass)
    klass_pm_schedule=Slot.objects.filter(klass=klass, am_pm='pm').order_by('start')
    klass_am_schedule=Slot.objects.filter(klass=klass, am_pm='am').order_by('start')
    
    response=HttpResponse(content_type='application/pdf')
    filename=klass.name+'-'+klass.teacher+'.pdf'
    response['Content-Disposition']='attachement; filename="%s"' %filename
    
    doc=SimpleDocTemplate(response, rightMargin=inch, lefMargin=inch, topMargin=inch, bottomMargin=inch)
    elements=[]
    title_style=ParagraphStyle(name='Title',fontName='Helvetica',fontSize=14,leading=28)
    subtitle_style=ParagraphStyle(name='Sub_Title',fontName='Helvetica',fontSize=12,leading=24)
    
    #Title
    elements.append(Paragraph(klass.teacher+' - Gr. '+klass.grade+' - Rm. '+klass.room,title_style))
    elements.append(Paragraph('Conference Schedule',title_style))
    
    #Thursday
    elements.append(Paragraph('Thursday Evening',subtitle_style))
    
    data=[('Start Time','End Time','Student'),]
    for slot in klass_pm_schedule:
        if slot.student:
            a=slot.student.last_name
            data.append((slot.start, slot.end, slot.student.first_name+' '+slot.student.last_name))
        else:
            data.append((slot.start, slot.end, 'Available'))
    table=Table(data, hAlign='LEFT')
    elements.append(table)
 
    #Friday
    elements.append(Paragraph('Friday Morning',subtitle_style))
    
    data=[('Start Time','End Time','Student'),]
    for slot in klass_am_schedule:
        if slot.student:
            a=slot.student.last_name
            data.append((slot.start, slot.end, slot.student.first_name+' '+slot.student.last_name))
        else:
            data.append((slot.start, slot.end, 'Available'))   
    
    
    table=Table(data, hAlign='LEFT')
    elements.append(table)
    doc.build(elements)
    
    return response