from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):
	context = {
		"courses" : Courses.objects.all()
	}

	return render(request, "index.html", context)

def process(request):
	Courses.objects.create( course = request.POST['Cname'], description = request.POST['desc'] )
	return redirect('/')

def toremove(request, id):
	rcourse = Courses.objects.get( id = id)
	request.session['rid'] = rcourse.id
	context = {
		"rc" : Courses.objects.all().get(id = id)
	}

	return render (request, "remove.html" , context)

def remove(request):
	if request.POST['confirm']:
		Courses.objects.filter(id = request.session['rid'] ).delete()
		return redirect('/')

def returnn(request):	
		return	redirect('/')
