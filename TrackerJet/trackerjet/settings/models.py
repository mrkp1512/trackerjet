# Create your models here.
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings
from django import forms
from django.contrib import admin

# State Model
class State(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        ordering = ['name']  
    def __str__(self):
        return self.name


# District Model
class District(models.Model):
    name = models.CharField(max_length=100)
    State = models.ForeignKey(State, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        ordering = ['name']

    def __str__(self):
        return self.name


# City Model
class City(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cities'
        verbose_name_plural = 'City'
        ordering = ['name']

    def __str__(self):
        return self.name


# Branch Model
class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=50)
    street = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(max_length=20)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name
    

# TrainerFilter for Admin
class TrainerFilter(admin.SimpleListFilter):
    title = 'Trainer'
    parameter_name = 'trainer'

    def lookups(self, request, model_admin):
        # Return the available trainers
        trainers = User.objects.filter(groups__name='Faculty').distinct()
        return [(trainer.id, trainer.username) for trainer in trainers]

    def queryset(self, request, queryset):
        # Apply the filter based on the selected trainers
        if self.value():
            return queryset.filter(trainer=self.value())
        return queryset

    
# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    coursecode = models.CharField(max_length=10)
    trainer = models.ManyToManyField(User, related_name='courses', blank=False)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        faculty_group = Group.objects.get(name='Faculty')
        self.trainer.set(User.objects.filter(groups=faculty_group))


# Course Fees Model
class Course_fees(models.Model):

    FEES_CHOICES = (
    ('Registration', 'Registration'),
    ('one_times', 'One Time'),
    ('two_times', 'Two Times'),
    ('three_times', 'Three Times')
)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    fees_type = models.CharField(max_length=50, null=True, choices=FEES_CHOICES)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    installment_period = models.IntegerField()
    
    class Meta:
        verbose_name = 'Course Fee'
        verbose_name_plural = 'Course Fees'

    def __str__(self):
        return self.fees_type

# Batch Model
class Batch(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Closed'),
    ]
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    Startdate = models.DateField()
    Enddate = models.DateField()
    status = models.BooleanField(default=False, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return f"Batch of {self.course} course"

class FeesReceipt(models.Model):
    PAYMENT_MODE_CHOICES = [                                                                                            
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cheque', 'Cheque'),
    ]

    COLLECTED_TO_ACCOUNT_CHOICES = [
        ('oneteam ac 1', 'Oneteam ac 1'),
        ('oneteam ac 2', 'Oneteam ac 2'),
        ('oneteam ac 3', 'Oneteam ac 3'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.DO_NOTHING, null=True)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=50)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_to_account = models.CharField(max_length=100, choices=COLLECTED_TO_ACCOUNT_CHOICES)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    description = models.TextField()
    receipt_image = models.ImageField(upload_to='receipts/')

    def __str__(self):
        return self.receipt_number
    # def name__method(self):
    #     from students.models import Student
    #     students = Student.objects.all()
    
# class FeeDetails(models.Model):
#     FEES_CHOICES = (
#     ('one_times', 'One Time'),
#     ('two_times', 'Two Times'),
#     ('three_times', 'Three Times')
# )
#     student = models.ForeignKey('students.Student', on_delete=models.DO_NOTHING, null=True)
#     selection_type = models.CharField(null=True,max_length=20, choices=FEES_CHOICES)
#     first_pay = models.DateField(null=True, blank=True)
#     first_pay_amount = models.IntegerField(null=True, blank=True)
#     second_pay = models.DateField(null=True, blank=True)
#     second_pay_amount = models.IntegerField(null=True, blank=True)
#     third_pay = models.DateField(null=True, blank=True)
#     third_pay_amount = models.IntegerField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if self.selection_type == 'one_times':
#             self.second_pay = None
#             self.second_pay_amount = None
#             self.third_pay = None
#             self.third_pay_amount = None
#         elif self.selection_type == 'two_times':
#             self.third_pay = None
#             self.third_pay_amount = None

#         super().save(*args, **kwargs)




# class Payment(models.Model):
    
#     std_name_P = models.ForeignKey('students.Student',on_delete=models.DO_NOTHING)
#     amount = models.DecimalField(max_digits=8, decimal_places=2)
#     payment_date = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'Payment'
#         verbose_name_plural = 'Payments'

#     def __str__(self):
#         return f"Payment of {self.amount} made by {self.std_name} on {self.payment_date}"
    


class StudentFees(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.DO_NOTHING)
    InstallmentDate = models.DateField()
    InstallmentAmount = models.IntegerField(null=True)
    BalanceAmount = models.IntegerField(null=True)
    taxper = models.IntegerField(verbose_name="Tax Per.", blank=True, null=True)
    
    def  __str__(self):
        return f"Fees {self.InstallmentAmount} of {self.student} with installment date {self.InstallmentDate}"  
    