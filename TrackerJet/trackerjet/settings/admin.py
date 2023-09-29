from collections import OrderedDict
from typing import Dict, Optional
from django import forms
from django.contrib import admin
from django.db.models import OuterRef, Subquery, Count
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from .models import State, District, City, Branch, Course, Batch, Course_fees, FeesReceipt, StudentFees
from django.urls import reverse, reverse_lazy
from django.utils.html import format_html
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import path
from students.models import Student
from django.shortcuts import redirect


# District Admin View
class DistrictAdmin(admin.ModelAdmin):
    model = District
    extra = 0
    list_display = ('name', 'State')
    list_filter = ('State',)
    search_fields = ('name', 'State__name')
    ordering = ['name', 'State__name']

# State Admin View
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_district_count']
    ordering = ['name']
    search_fields = ('name',)
    list_filter = ('name',)

    def get_district_count(self, obj):
        if isinstance(obj, State):
             return obj.district_set.count()
        return 0

    get_district_count.short_description = 'Districts Count'

# City Admin View
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'state')
    list_filter = ('district__name',)
    search_fields = ('name', 'district__name', 'district__state__name')

    def state(self, obj):
        return obj.district.State.name

    state.short_description = 'State'

# Batch Form (for boolean in Choices)
class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['course', 'Startdate', 'Enddate', 'status']

# Batch Admin View
class BatchAdmin(admin.ModelAdmin):
    list_display = ('course', 'Startdate', 'Enddate', 'status')
    list_filter = ('course',)
    search_fields = ('course',)
    form = BatchForm

# Course Fees Admin View
class CourseFeesAdmin(admin.ModelAdmin):
    model = Course_fees
    extra = 0
    list_display = ('get_fees_type', 'amount', 'tax', 'installment_period',)
    list_filter = ('installment_period',)
    search_fields = ('fees_type', 'amount')
    ordering = ['fees_type']

    def get_fees_type(self, obj):
        course = obj.course
        fees_type = obj.fees_type
        return f"{course} {fees_type} fees"

class CourseAdmin(admin.ModelAdmin):

    fields = ('name','trainer')
    list_display = ('name', 'display_trainer',)
    list_filter = ('trainer',)
    filter_horizontal = ('trainer',)
    ordering = ['coursecode',]

    def display_trainer(self, obj):
        return ", ".join([str(trainer) for trainer in obj.trainer.all()])

    display_trainer.short_description = 'Team Member'


class FeesReceiptAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'paid_amount', 'receipt_number', 'payment_mode', 'description', 'collected_to_account')


class StudentFeesAdmin(admin.ModelAdmin):
    list_display = ['InstallmentDate', 'InstallmentAmount', 'BalanceAmount', 'pay_link']
    list_display_links = None
    ordering = ('InstallmentAmount',)
    # readonly_fields = ('InstallmentDate', 'BalanceAmount')

   

    
    def pay_link(self, obj):
        url = reverse('admin:settings_feesreceipt_add')
        link = f'<a href="{url}?student_id={obj.student}">Pay</a>'
        return format_html(link)

    pay_link.short_description = 'Payment'

   

# Register models in the admin site
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Branch)
admin.site.register(Course, CourseAdmin)
admin.site.register(Course_fees, CourseFeesAdmin)
admin.site.register(Batch, BatchAdmin)
# admin.site.register(Payment)
admin.site.register(FeesReceipt, FeesReceiptAdmin)
# admin.site.register(FeeDetails, FeeDetailsAdmin)
admin.site.register(StudentFees, StudentFeesAdmin)



 