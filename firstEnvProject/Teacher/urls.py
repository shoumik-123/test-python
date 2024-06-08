from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.machine, name='machine'),
    path('deep/', views.deep, name='deep'),
    path('contact/', views.contact_view, name='contact'),


]
