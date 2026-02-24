from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('passport-checker/', views.passport_checker, name='passport_checker'),
    path('visa-checker/', views.visa_checker, name='visa_checker'),
    path('application/', views.application_form, name='application_form'),
    path('application/success/<int:application_id>/', views.application_success, name='application_success'),
    path('application/pdf/<int:application_id>/', views.generate_application_pdf, name='generate_pdf'),
    path('whatsapp/<int:application_id>/', views.whatsapp_redirect, name='whatsapp_redirect'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('procedure/', views.procedure, name='procedure'),
]
