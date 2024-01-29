from django import forms
from django.forms import ModelForm
from django.db import models
from .models import RegisterForm
from .models import NoticeBoardModel
from .models import FeedbackModel, EmployeeScheduleModel

class RegisterVisitorForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ('noPlate', 'LicenseNum', 'CarModel','PhoneNum','DateTime','CarNum','HouseUnit','leave')

        
class NoticeBoard(forms.ModelForm):
    class Meta:
        model = NoticeBoardModel
        fields = ('NoticeTitle','NoticeDescription','NoticeImage')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ('Feedback','FeedbackImage')

class EmployeeScheduleForm(forms.ModelForm):
    class Meta:
        model = EmployeeScheduleModel
        fields = ('ScheduleNote','ScheduleImage')


