from myapp.models import Dreamreal

from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime


def hello(request):
	today = datetime.datetime.now().date()
	
	daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def redirectTest(request):
   return redirect("https://www.djangoproject.com")

def crudops(request):
	#Creating an entry
	
	dreamreal = Dreamreal(
		website = "www.polo.com", mail = "sorex@polo.com", 
		name = "sorex", phonenumber = "002376970"
	)
	
	dreamreal.save()
	
	#Read ALL entries
	objects = Dreamreal.objects.all()
	res ='Printing all Dreamreal entries in the DB : <br>'
	
	for elt in objects:
		res += elt.name+"<br>"
	
	#Read a specific entry:
	sorex = Dreamreal.objects.get(name = "sorex")
	res += 'Printing One entry <br>'
	res += sorex.name
	
	#Delete an entry
	res += '<br> Deleting an entry <br>'
	sorex.delete()
	
	#Update
	dreamreal = Dreamreal(
		website = "www.polo.com", mail = "sorex@polo.com", 
		name = "sorex", phonenumber = "002376970"
	)
	
	dreamreal.save()
	res += 'Updating entry<br>'
	
	dreamreal = Dreamreal.objects.get(name = 'sorex')
	dreamreal.name = 'thierry'
	dreamreal.save()
	
	return HttpResponse(res)

def datamanipulation(request):
	res = ''
	
	#Filtering data:
	qs = Dreamreal.objects.filter(name = "paul")
	res += "Found : %s results<br>"%len(qs)
	
	#Ordering results
	qs = Dreamreal.objects.order_by("name")
	
	for elt in qs:
		res += elt.name + '<br>'
	
	return HttpResponse(res)