from django.shortcuts import render
from .models import Feature
# from django.http import HttpResponse

# Create your views here.
def index(request):
    feature = Feature.objects.all()
    return render(request, 'index.html', {'feature' : feature})