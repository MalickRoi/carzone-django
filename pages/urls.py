from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about-us/', about_view, name='about-page'),
    path('services/', services_view, name='services-page'),
    path('contact-us/', contact_view, name='contact-page'),
]

