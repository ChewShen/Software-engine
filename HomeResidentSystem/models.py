from django.db import models

# Create your models here.

# class CustomAutoField(models.Field):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def db_type(self, connection):
#         return 'varchar(10)'
    


class RegisterForm(models.Model):
    VisitorID = models.AutoField(primary_key=True, unique=True)
    noPlate = models.CharField('no Plate', max_length =10)
    LicenseNum = models.CharField(max_length =12)
    CarModel = models.CharField(max_length = 30)
    PhoneNum = models.CharField(max_length = 13)
    DateTime = models.CharField(max_length = 20)
    CarNum = models.CharField(max_length = 20)
    HouseUnit = models.CharField(max_length = 5)
    leave = models.CharField(max_length = 20)

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitor'
  

    def __str__(self):
        return self.noPlate
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Checking if it's a new instance
            last_record = RegisterForm.objects.order_by('-VisitorID').first()
            if last_record:
                self.VisitorID = last_record.VisitorID + 1
            else:
                self.VisitorID = 60000  # Starting from 10001 for the first record

        super().save(*args, **kwargs)
       
  
class NoticeBoardModel(models.Model):
    NoticeBoardID = models.AutoField(primary_key=True, unique=True)
    NoticeTitle = models.TextField()
    NoticeDescription = models.TextField()
    NoticeDate = models.DateField(auto_now=True)
    NoticeTime = models.TimeField(auto_now=True)
   
    class Meta:
        verbose_name = 'Notice Board'
        verbose_name_plural = 'Notice Board'
  

    def __str__(self):
        return self.NoticeTitle
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Checking if it's a new instance
            last_record = NoticeBoardModel.objects.order_by('-NoticeBoardID').first()
            if last_record:
                self.NoticeBoardID = last_record.NoticeBoardID + 1
            else:
                self.NoticeBoardID = 6969000  # Starting from 10001 for the first record

        super().save(*args, **kwargs)


class FeedbackModel(models.Model):

    Feedback = models.TextField()
    

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
  

    def __str__(self):
        return self.Feedback
    

class EmployeeScheduleModel(models.Model):
    ScheduleID = models.AutoField(primary_key=True, unique=True)
    SchedulePostDate = models.DateField(auto_now=True)
    SchedulePostTime = models.TimeField(auto_now=True)
    ScheduleNote = models.TextField()
    ScheduleImage = models.ImageField(null=True, blank=True, upload_to="schedule/")


    class Meta:
        verbose_name = 'Employee Schedule'
        verbose_name_plural = 'Employee Schedule'
  

    def __int__(self):
        return self.ScheduleID
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Checking if it's a new instance
            last_record = EmployeeScheduleModel.objects.order_by('-ScheduleID').first()
            if last_record:
                self.ScheduleID = last_record.ScheduleID + 1
            else:
                self.ScheduleID = 981000  # Starting from 10001 for the first record

        super().save(*args, **kwargs)