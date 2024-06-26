import csv
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from HomeResidentSystem.models import NoticeBoardModel
from .forms import RegisterUserForm, UploadPaymentForm
from .forms import UserProfileChangeForm, PassChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import CustomUser,UploadPaymentModel,UserPaymentModel
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import UserProfileChangeForm, PassChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import CustomUser,UploadPaymentModel,UserPaymentModel


# Create your views here.
@login_required
def isAdmin(request):
    return redirect('/admin')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            role = request.user.role

            if request.user.is_superuser:
                return redirect('/admin')
            
            elif role == 'Employee':
                return redirect('/EmployeeLanding')
    
            elif role == 'Resident':
                announcement = NoticeBoardModel.objects.all()
                return redirect('/ResidentLanding', {'notice_list' : announcement})
            
        else:
            messages.error(request,"Nope, something wrong")
            return redirect('home')
            
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')


def RegisterUser(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registeration Success"))
            return redirect('/ResidentLanding')
        
        else:
                # Display error messages at the top of the form
                for field, errors in form.errors.items():
                    for error in errors:
                        if field == "password2":
                            custom_error = f"Password: {error}"
                            messages.error(request, custom_error)

                        elif field == "password1":
                            custom_error = f"Password: {error}"
                            messages.error(request, custom_error)

                        elif field == "email":
                            custom_error = f"Email: {error}"
                            messages.error(request, custom_error)

                        else:
                            messages.error(request, f"{field}: {error}")
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register.html',
                  {'form':form})


@login_required
def ResidentEdit(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.has_changed(): 
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('/ResidentLanding')
            
            else:
                messages.info(request, "No changes were made to your profile")
                return redirect('/ResidentLanding')
    else:
        form = UserProfileChangeForm(instance=request.user)

    return render(request, 'authentication/ResidentEdit.html', {'form': form})



from django.http import HttpResponseRedirect                                                                                                                                            
class PassChangeView(PasswordChangeView):
    form_class = PassChangeForm  
    success_url = reverse_lazy('ResidentLanding')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully.")
        print("Password changed successfully.")

        # Get the current user
        user = self.request.user

        # Redirect based on user's role
        if user.role == 'Resident':
            return HttpResponseRedirect(reverse_lazy('ResidentLanding'))
        elif user.role == 'Employee':
            return HttpResponseRedirect(reverse_lazy('EmployeeLanding'))
        else:
            # Default redirect if role is not recognized
            return HttpResponseRedirect(reverse_lazy('DefaultRedirect'))

        return response    

    def form_invalid(self, form):
            # Handle form errors
            for field, errors in form.errors.items():
                for error in errors:
                    if field == "old_password":
                        custom_error = f"Old Password: {error}"
                        messages.error(self.request, custom_error)

                    elif field == "new_password2":
                        custom_error = f" New Password: {error}"
                        messages.error(self.request, custom_error)

                    else:
                        messages.error(self.request, f"{field}: {error}")

            return super().form_invalid(form)                                                                                                                
    

@login_required
def EmployeeEdit(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.has_changed():  # Check if the form data has changed
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('/EmployeeLanding')
            else:
                messages.info(request, "No changes were made to your profile")
                return redirect('/EmployeeLanding')
    else:
        form = UserProfileChangeForm(instance=request.user)

    return render(request, 'authentication/EmployeeEdit.html', {'form': form})





@login_required
def payment(request):
    context = UserPaymentModel.objects.all()
    if request.method == "POST":
        form = UploadPaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted successfully!')
            return redirect('ResidentLanding')  
    else:
        form = UploadPaymentForm()


    return render(request, 'Sites/payment.html', {'form':form, 'context': context})



from django.contrib.auth.decorators import user_passes_test
def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def generate_csv(request):
    return render(request, 'authentication/testreport.html')


@login_required
@user_passes_test(is_admin)
def generate_csv_invoice(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="invoice_records.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['Invoice ID', 'username', 'Outstanding Payment', 'Invoice Date','Invoice Time', 'Invoice Image','paid?','user ID'])

    # Write data rows
    invoice_records = UserPaymentModel.objects.all()
    for payment in invoice_records:
        writer.writerow([
            payment.InvoiceID,
            payment.userID.username if payment.userID else '',
            payment.PaymentAmount,
            payment.InvoiceDate,
            payment.InvoiceTime,
            payment.InvoiceImage,
            payment.paid,
            payment.userID,
        ])

    return response



@login_required
@user_passes_test(is_admin)
def generate_csv_user(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_records.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name','last_name','email','is_staff','is_active','date_joined','role','HouseUnit','ParkingLot'])

    # Write data rows
    user_records = CustomUser.objects.all()
    for user in user_records:
        writer.writerow([
            user.id,
            user.password,
            user.last_login,
            user.is_superuser,
            user.username,
            user.first_name,
            user.last_name,
            user.email,
            user.is_staff,
            user.is_active,
            user.date_joined,
            user.role,
            user.HouseUnit,
            user.ParkingLot
        ])

    return response

@login_required
@user_passes_test(is_admin)
def generate_csv_payment(request):
    # Check if a date parameter is provided in the request


    # Filter payment records based on the date range
    payment_records = UploadPaymentModel.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="payment_records.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Payment ID', 'Payment Receipt', 'Payment User'])

    # Write data rows
    for payment in payment_records:
        writer.writerow([
            payment.PaymentID,
            payment.PaymentImage,
            payment.username,
        ])

    return response
