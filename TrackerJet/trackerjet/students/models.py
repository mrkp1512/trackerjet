from django.db import models
from django.db.models import Sum
from settings.models import Course,City,State,District, Batch, Course_fees

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    yes_choice= (
    ('yes','Yes'),
    ('no','No'),
)
    student = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=20)
    alternative_email = models.EmailField(max_length=20)
    address = models.TextField(max_length=200)
    alternative_address = models.TextField(max_length=200)
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    pincode = models.IntegerField(null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)
    has_laptop = models.CharField(max_length=3, choices=yes_choice,blank=True)
    fees_type = models.ForeignKey(Course_fees, on_delete=models.DO_NOTHING, null=True, related_name='students')
    photo = models.ImageField(upload_to='static/admin/img', null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    joining_date = models.DateField(null=True, blank=True, default='2012-12-12')
    is_registered = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.student

    def __str__(self):
        return f"Student name is {self.student}"
