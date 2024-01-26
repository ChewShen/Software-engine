from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import PassChangeView

import HomeResidentSystem

from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('RegisterUser', views.RegisterUser, name="RegisterUser"),
    path('HomeResidentSystem', include (HomeResidentSystem.urls)),
    path('isAdmin',views.isAdmin, name="admin"),
    path('ResidentEdit',views.ResidentEdit, name="ResidentEdit"),
    path('EmployeeEdit',views.EmployeeEdit, name="EmployeeEdit"),
    path('<int:pk>/password/',PassChangeView.as_view(template_name='authentication/forgetpass.html'),name="password_change"),

]