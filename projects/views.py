from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def projects(request):
    return render(request, "projects/projects.html")
