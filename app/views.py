from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this is my first string response')
def second(request):
    return HttpResponse('this is my second string response')
def first_htmlpage(request):
    return render(request,'first_htmlpage.html')
def second_htmlpage(request):
    return render(request,'second_htmlpage.html')



