from django.contrib import admin
from .models import CustomUser, UserPaymentModel
# Register your models here.



class CustomShow(admin.ModelAdmin):
    list_display = ('id','username','role')  
    list_display_links = ('id','username', 'role') 
    ordering = ['role']  

class CustomUserPaymentModel(admin.ModelAdmin):
    readonly_fields =  ('InvoiceID','InvoiceDate','InvoiceTime')  
    list_display = ('InvoiceID','user_ID','InvoiceDate','InvoiceTime')  
    list_display_links =  ('InvoiceID','user_ID','InvoiceDate','InvoiceTime')  
    ordering = ['InvoiceID'] 
    
    def user_ID(self, obj):
        return obj.userID.username  # Assuming 'UserID' is the attribute of CustomUser model

    user_ID.short_description = 'User ID'


    
admin.site.register(CustomUser, CustomShow)
admin.site.register(UserPaymentModel, CustomUserPaymentModel)