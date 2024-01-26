from django.contrib import admin
from .models import RegisterForm
from .models import NoticeBoardModel
from .models import FeedbackModel, EmployeeScheduleModel
# Register your models here




class VistiorAdmin(admin.ModelAdmin):
    list_display = ('VisitorID','noPlate', 'PhoneNum')  
    list_display_links = ('VisitorID', 'noPlate', 'PhoneNum') 
    ordering = ['VisitorID']  

class NoticeAdmin(admin.ModelAdmin):
    readonly_fields = ('NoticeBoardID','NoticeDate', 'NoticeTime')
    list_display = ('NoticeBoardID','NoticeTitle')  
    list_display_links = ('NoticeBoardID','NoticeTitle')  
    ordering = ['NoticeBoardID']  

class EmployeeScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('ScheduleID',)
    list_display = ('ScheduleID','ScheduleNote', 'SchedulePostDate')
    list_display_links = ('ScheduleID','ScheduleNote', 'SchedulePostDate')  
    ordering = ['ScheduleID']  




admin.site.register(RegisterForm,VistiorAdmin)
#admin.site.register(RegisterForm)
admin.site.register(NoticeBoardModel,NoticeAdmin)
admin.site.register(FeedbackModel)
admin.site.register(EmployeeScheduleModel,EmployeeScheduleAdmin)

