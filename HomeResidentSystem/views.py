from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterVisitorForm, FeedbackForm, EmployeeScheduleForm, NoticeBoard
from .models import NoticeBoardModel, EmployeeScheduleModel
from django.db.models import Q


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



