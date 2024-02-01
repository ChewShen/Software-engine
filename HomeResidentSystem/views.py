import csv
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterVisitorForm, FeedbackForm, EmployeeScheduleForm, NoticeBoard
from .models import NoticeBoardModel, EmployeeScheduleModel, FeedbackModel, RegisterForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test


# from AllUsers.models import CustomUser
# from AllUsers.forms import RegisterUserForm



import HomeResidentSystem

# Create your views here.
def EmployeeLanding(request):
    return render(request, "Sites/EmployeeLanding.html")

def UserFeedBack(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('home')  
    else:
        form = FeedbackForm()

    return render(request,"Sites/UserFeedBack.html",{'form': form})


def ResidentLanding(request):
    user = request.user  # Fetch the current logged-in user
    # form = request.RegisterUserForm(instance=user)
    return render(request, "Sites/Residentlanding.html", {'user': user})

def SearchNotice(request):
    if request.method == "POST":
        searched = request.POST['searched']
        notice = NoticeBoardModel.objects.filter(Q(NoticeTitle__contains=searched) | Q(NoticeImage__contains=searched))
        NoticeWithDate = NoticeBoardModel.objects.filter(NoticeDate__contains=searched)
        announcement = NoticeBoardModel.objects.all()
        return render(request, "Sites/searchNotice.html", {'searched': searched, 'NoticeWithDate': NoticeWithDate, 'notice': notice, 'notice_list': announcement})

    else:
        return render(request,"Sites/searchNotice.html")



def RegisterVisitor(request):
    if request.method == "POST":
        form = RegisterVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('home') 
    else:
        form = RegisterVisitorForm()
    
    return render(request, "Sites/RegisterVisitor.html", {'form': form})


def home(request):
    return render(request,"Sites/indexs.html")

def NoticeBoard(request):
        announcement = NoticeBoardModel.objects.all()
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submitted successfully!')
                return redirect('/EmployeeLanding')  
            else:
                form = NoticeBoard()

        return render(request,'Sites/NoticeBoard.html',{'notice_list' : announcement})

def logoutUser(request):
    logout(request)
    messages.success(request, ("Log out Success"))
    return redirect('home')


def adminlogout(request):
    logout(request)
    messages.success(request, ("Log out Success"))

    # Redirect to the home page regardless of the request method
    return redirect('home')

def EmployeeSchedule(request):
        Schedule = EmployeeScheduleModel.objects.all().order_by('-SchedulePostDate')
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submitted successfully!')
                return redirect('/EmployeeLanding')  
        else:
            form = EmployeeScheduleForm()

        return render(request,'Sites/EmployeeSchedule.html',{'Schedule' : Schedule})



def VisitorFeedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('home')  
    else:
        form = FeedbackForm()

    return render(request,"Sites/VisitorFeedBack.html",{'form': form})



def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'


@login_required
@user_passes_test(is_admin)
def generate_csv_feedback(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="feedback_records.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['ID', 'Feedback','Feedback Image'])

    # Write data rows
    feedback_records = FeedbackModel.objects.all()
    for feedback in feedback_records:
        writer.writerow([
            feedback.id,
            feedback.Feedback,
            feedback.FeedbackImage, 
        ])

    return response


@login_required
@user_passes_test(is_admin)
def generate_csv_visitor(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visitor_records.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['VisitorID', 'Plate Number','License Number','Car Model','Phone Number','Date arrived','Time arrived','Car amount','HouseUnit','Estimate to leave'])

    # Write data rows
    visitor_records = RegisterForm.objects.all()
    for visitor in visitor_records:
        writer.writerow([
            visitor.VisitorID,
            visitor.noPlate,
            visitor.LicenseNum,
            visitor.CarModel,
            visitor.PhoneNum,
            visitor.DateTime,
            visitor.CarNum,
            visitor.HouseUnit,
            visitor.leave
        ])

    return response