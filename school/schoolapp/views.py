from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'home.html')
def contact_view(request):
    return render(request,'contact.html')
def course_view(request):
    return render(request,'course.html')
def about_view(request):
    return render(request,'about.html')
def notifications_view(request):
    return render(request,'notifications.html')
def Registrations_view(request):
    return render(request,'registrations.html')
def login_view(request):
    return render(request,'login.html')