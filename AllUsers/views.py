from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from HomeResidentSystem.models import NoticeBoardModel
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileChangeForm, PassChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import CustomUser
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
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('/ResidentLanding')
    else:
        form = UserProfileChangeForm(instance=request.user)

    return render(request, 'authentication/ResidentEdit.html', {'form': form})


class PassChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PassChangeForm  
    success_url = reverse_lazy('ResidentLanding')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully.")
        return response
    

@login_required
def EmployeeEdit(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('/EmployeeLanding')
    else:
        form = UserProfileChangeForm(instance=request.user)

    return render(request, 'authentication/EmployeeEdit.html', {'form': form})




