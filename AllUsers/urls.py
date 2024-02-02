from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import PassChangeView
from .views import payment


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
    path('payment',views.payment, name="payment"),
    # path('AllUsers/payment/<path:pdf_path>/', views.payment, name='payment'),
    path('generatecsv/', views.generate_csv, name='generate_csv'),
    path('generatecsv/generatecsv_invoice', views.generate_csv_invoice, name='generate_csv_invoice'),
    path('generatecsv/generatecsv_user', views.generate_csv_user, name='generate_csv_user'),
    path('generatecsv/generatecsv_payment', views.generate_csv_payment, name='generate_csv_payment'),
]
