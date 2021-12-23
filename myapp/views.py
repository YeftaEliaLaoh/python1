from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})