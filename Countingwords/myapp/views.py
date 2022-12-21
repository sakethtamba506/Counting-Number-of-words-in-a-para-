from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    name="saketh1"
    return  render(request,'index.html',{'name':name})
def counter(request):
    text=request.GET['text']
    amt=len(text.split())
    # word2=request.GET['text1']
    return render(request,'counter.html',{'word1':amt})