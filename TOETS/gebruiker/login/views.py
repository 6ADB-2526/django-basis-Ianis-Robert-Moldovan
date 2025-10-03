from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def opstart(request):
    return render(request, 'start.html',)