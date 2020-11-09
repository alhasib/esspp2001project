from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Thi Is Our First Project")


def about_me(request):
    return HttpResponse("This Is Our About Page")


def contact(request):
    return HttpResponse("This Is Our Contact Page")

def service(request):
    return HttpResponse("This is Our Service Page")


def info(request, name, age):
    return HttpResponse('{} is {} years old' .format(name, age))