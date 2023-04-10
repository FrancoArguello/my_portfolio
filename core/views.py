from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')


def about(request):
    return render(request, "about_me/about.html")


def projects(request):
    return render(request, "projects/projects.html")


def skill(request):
    return render(request, 'skills/skills.html')


def contact(request):
    return render(request, 'contact/contact.html')
