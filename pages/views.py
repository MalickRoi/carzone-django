from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def services_view(request):
    return render(request, 'pages/services.html')


def contact_view(request):
    return render(request, 'pages/contact.html')

