# from django import forms
# from django.contrib.admin.widgets import AdminDateWidget
# from django.forms.widgets import DateInput
# from django.urls import reverse
# from django.contrib.auth.models import User, Group
# from .models import Student
# from settings.models import Batch, Course_fees, Course

# class BatchForm(forms.ModelForm):
#     class Meta:
#         model = Batch
#         fields = ['course', 'Startdate', 'Enddate']
#         widgets = {
#             'Startdate': AdminDateWidget(),
#         }

# class CourseFeesForm(forms.ModelForm):
#     class Meta:
#         model = Course_fees
#         fields = ['fees_type']


# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['trainer']


# class CourseEditForm(forms.ModelForm):
#     batch = forms.ModelChoiceField(queryset=Batch.objects.all(), empty_label=None)
#     installment_type = forms.ModelChoiceField(queryset=Course_fees.objects.all(), empty_label=None)
#     startdate = forms.ModelChoiceField(queryset=Batch.objects.values_list('Startdate', flat=True), empty_label=None, initial=Batch.objects.first().Startdate)
#     enddate = forms.ModelChoiceField(queryset=Batch.objects.values_list('Enddate', flat=True), empty_label=None, initial=Batch.objects.first().Enddate)
#     trainer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Faculty'), empty_label=None)
#     coursedetails = forms.CharField(widget=forms.TextInput(attrs={'rows': 4, 'cols': 40}),)

#     class Meta:
#         model = Student
#         fields = ['student', 'course', 'coursedetails', 'batch', 'trainer', 'startdate', 'enddate', 'installment_type']
#         widgets = {
#             'course': forms.Select(attrs={'class': 'vForeignKeyRawIdAdminField'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if 'instance' in kwargs:
#             student = kwargs['instance']
#             student_id = student.pk
#             # self.fields['course'].widget.attrs['form'] = 'course-edit-form'
#             # self.fields['course'].widget.attrs['formaction'] = reverse('admin:students_course_edit', args=[student_id])
#             self.fields['student'].widget.attrs['disabled'] = True
#             self.fields['startdate'].widget.attrs['disabled'] = True
#             self.fields['enddate'].widget.attrs['disabled'] = True
#             self.fields['trainer'].widget.attrs['disabled'] = True

#     def save(self, commit=True):
#         course = super().save(commit=False)
#         coursedetails = self.cleaned_data.get('coursedetails')
#         course.name = f'{course.coursecode} - {coursedetails}'
#         if commit:
#             course.save()
#         return course

