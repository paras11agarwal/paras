from django.shortcuts import render,HttpResponse
from passlib.hash import sha256_crypt
from django.contrib.auth.models import User
from .models import Data,Question
from django.db import IntegrityError

def signup(request):                                                       # signup template
	return render(request,'crypto/signup.html')

def check(request):                                                        # signup storing data
	try:
		entry = User.objects.create(username=request.POST.get('username'),password=sha256_crypt.hash(request.POST.get('password')),email=request.POST.get('email'))
		entry.save()
		d=Data(user=entry,roll1=request.POST.get('roll1'),roll2=request.POST.get('roll2'),phone=request.POST.get('phone'))
		d.save()
		return HttpResponse("signed in")
	except IntegrityError:
		return HttpResponse("username exists")

def login(request):                                                         # login template
	return render(request,'crypto/login.html')

def credential(request):                                                    # checking for login
	user=User.objects.get(username=request.POST.get('username'))
	if(user is not None):
		if(sha256_crypt.verify(request.POST.get('password'),user.password)):
			request.session.create()
			request.session['username']=request.POST.get('username')
			
			return HttpResponse('logged in')
		else:
			return HttpResponse('incorrect password')
	else:
		return HttpResponse('username does nor exist')
	
def logout(request):
	p=Question.objects.get(pk=1)
	del request.session['username']
	return HttpResponse(p.question)
# Create your views here.