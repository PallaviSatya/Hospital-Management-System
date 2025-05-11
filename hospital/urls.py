from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import department_view

urlpatterns = [
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('cardio_dept/', views.cardio_dept, name='cardio_dept'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('doctor_single/', views.doctor_single, name='doctor_single'),
    path('doctor/', views.doctor, name='doctor'),
    path('gyno_dept/', views.gyno_dept, name='gyno_dept'),
    path('', views.index, name='index'), 
    path('neuro_dept/', views.neuro_dept, name='neuro_dept'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('raj_single/', views.raj_single, name='raj_single'),
    path('service/', views.service, name='service'),
    path('shambhavi-single/', views.shambhavi_single, name='shambhavi_single'),
    path('vanshika-single/', views.vanshika_single, name='vanshika_single'),
    path('womenhealth/', views.womenhealth, name='womenhealth'),
    path('cardiology/', lambda request: department_view(request, 'raj'), name='cardiology'),
    path('neurology/', lambda request: department_view(request, 'vanshika'), name='neurology'),
    path('gynecology/', lambda request: department_view(request, 'shambhavi'), name='gynecology'),
    path('login/', views.doctor_login, name='doctor_login'),
    path('logout/', LogoutView.as_view(next_page='doctor_login'), name='logout'),
    path('patient/<str:patient_name>/', views.patient_profile, name='patient_profile'),
    path('visit/<int:visit_id>/', views.visit_detail, name='visit_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
