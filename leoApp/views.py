from django.shortcuts import render
from .models import Feature
# from django.http import HttpResponse

# Create your views here.
def index(request):

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Smart vTracker'
    feature2.detail = 'We offer advanced already-made and customized tracking solutions to individuals, companies and governments.'

    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'app1'
    feature1.detail = 'This is app1'

    feature = [feature1, feature2,]
    return render(request, 'index.html', {'feature' : feature})