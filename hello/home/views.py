from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is Homepage")


def about(request):
    return HttpResponse("This is Aboutpage")


def services(request):
    return HttpResponse("This is Services page")


def contacts(request):
    return HttpResponse("This is Contact page")
