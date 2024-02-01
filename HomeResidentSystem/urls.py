from django.contrib import admin
from django.urls import include, path

from HomeResidentSystem import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('RegisterVisitor', views.RegisterVisitor, name='RegisterVisitor'),
    path('NoticeBoard',views.NoticeBoard, name="NoticeBoard"),
    path('SearchNotice',views.SearchNotice, name="SearchNotice"),
    path('ResidentLanding',views.ResidentLanding, name="ResidentLanding"),
    path('logout', views.logoutUser, name="logout"),
    path('UserFeedback', views.UserFeedBack, name="UserFeedback"),
    path('EmployeeLanding', views.EmployeeLanding, name="EmployeeLanding"),
    path('admin/logout/', views.adminlogout, name="admin_logout"),
    path('EmployeeSchedule',views.EmployeeSchedule, name="EmployeeSchedule"),
    path('VisitorFeedback', views.VisitorFeedback, name='VisitorFeedback'),
    path('generatecsv_feedback', views.generate_csv_feedback, name='generate_csv_feedback'),
    path('generatecsv_visitor', views.generate_csv_visitor, name='generate_csv_visitor'),
]

