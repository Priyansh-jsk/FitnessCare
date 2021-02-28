from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def contact(request):
    return HttpResponse('This is contact page')
def about(request):
    return render(request, 'about.html')
def result(request):
    return render(request, 'result.html')
def result_beginner(request):
    return render(request, 'result_beginner.html')
def result_intermidiate(request):
    return render(request, 'result_intermidiate.html')
def result_advance(request):
    return render(request, 'result_advance.html')