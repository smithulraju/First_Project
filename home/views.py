from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_function(request):
    return HttpResponse('Home Page')

def about_us_function(request):
    return HttpResponse('about us Page')

def contact_us_function(request):
    return render(request, 'contact.html')


