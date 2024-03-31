from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def dashboard(request):
    return render(request, 'dashboard.html')