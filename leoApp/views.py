from django.shortcuts import render
from .models import Feature
# from django.http import HttpResponse

# Create your views here.
def index(request):
    Feature1 = Feature()
    Feature1.id = 1
    Feature1.name = 'app1'
    Feature1.detail = 'This is app1'
    return render(request, 'index.html', {'feature' : Feature1})