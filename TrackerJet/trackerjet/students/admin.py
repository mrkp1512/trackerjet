from django.contrib.admin import AdminSite
from django.contrib import admin, messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import NoReverseMatch, path, reverse
from django.utils.html import format_html
# from students.forms import FeesReceipt
from .models import Student
from settings.models import StudentFees, Course_fees
from django.http import Http404, HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.contrib.admin.sites import site
from django.template.response import TemplateResponse
from datetime import timedelta



class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'teammember', 'mobile', 'course', 'display_course', 'fee_details', 'registered', 'active')
    fieldsets = (
        # Personal Info
        ('Student Details', {
            "fields": (('student', 'gender'),
                       ('email', 'alternative_email'),
                       ('address', 'alternative_address'),
                       ('dob', 'mobile',),
                       ('state', 'city', 'street', 'district'),
                       ('pincode',))}),
        # Course Info
        ('Course Info', {
            "fields": (('course', 'batch'),('start_date', 'end_date',),
                       ('fees_type'))}),                                                                     
        # Photo
        ('Photo', {
            "fields": (('photo',)),
        }),
        # Status
        ('Status', {
            "fields": ((('joining_date'), ('is_registered',), ('is_active',)))})
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            if obj.is_registered :
                fees_type = obj.fees_type
                print("Is Registered:", obj.is_registered)
                print("Fees Type:", fees_type)
                print("Type of fees_type:", type(fees_type))
                qr = Course_fees.objects.filter(fees_type = fees_type, course = obj.course).order_by('installment_period')

                for q in qr:
                    fee = StudentFees()
                    fee.InstallmentAmount = q.amount
                    fee.student = obj
                    fee.InstallmentDate = fee.student.joining_date + timedelta(days=30 * (q.installment_period + 1))
                    fee.BalanceAmount = q.amount
                    fee.taxper = q.tax
                    fee.save()


    def display_course(self, obj):
        return format_html("<a href='{url}'>GO</a>", url=obj.id)
    
    def fee_details(self,obj):
        student = Student.objects.get(student=obj.student)
        url = reverse('admin:settings_studentfees_changelist')
        url += f'?student__id__exact={student.id}'
        return format_html('<a href="{}">GO</a>', url)


    def registered(self, obj):
        # Display a green tick mark if student is registered, otherwise display a red cross mark
        if obj.is_registered:
            return format_html(
                '<span style="display:inline-block; width:20px; height:20px; border-radius:50%; '
                'background-color:green; color:white; text-align:center; line-height:20px">&#x2713;</span>'
            )
        else:
            return format_html(
                '<span style="display:inline-block; width:20px; height:20px; border-radius:50%; '
                'background-color:red; color:white; text-align:center; line-height:20px">&#x2717;</span>'
            )

    registered.short_description = 'Registered'

    def active(self, obj):
        # Display a green tick mark if student is active, otherwise display a red cross mark
        if obj.is_active:
            return format_html(
                '<span style="display:inline-block; width:20px; height:20px; border-radius:50%; '
                'background-color:green; color:white; text-align:center; line-height:20px">&#x2713;</span>'
            )
        else:
            return format_html(
                '<span style="display:inline-block; width:20px; height:20px; border-radius:50%; '
                'background-color:red; color:white; text-align:center; line-height:20px">&#x2717;</span>'
            )

    active.short_description = 'Active'

    def teammember(self, obj):
        # Retrieve team members for the course and display their names
        return ", ".join([str(trainer) for trainer in obj.course.trainer.all()])

    teammember.short_description = 'Team Members'

    
admin.site.register(Student, StudentAdmin)