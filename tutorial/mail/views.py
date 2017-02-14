
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
import random
import crypt
# Create your views here.

def index(request):
	return render(request, 'mail/index.html')
	
def store(request):
	# random password generation
	first="q w e r t y u i o p a s d f g h j k l z x c v b n m"
	last="Q W E R T Y U I O P L K J H G F D S A Z X C V B N M"
	mid="1 2 3 4 5 6 7 8 9 0"
	first=first.split()
	last=last.split()
	mid=mid.split()
	password="_"
	for i in range(0,3):
		password+=first[random.randrange(0,26)]
		password+=mid[random.randrange(0,10)]
		password+=last[random.randrange(0,26)]
'''
	print password
	password_hash=crypt.crypt(password)
	print password_hash

	valid_password=crypt.crypt(cleartext,password_hash)==password_hash
	print valid_password
'''
	list=[request.POST.get('username'),request.POST.get('email')]
	return HttpResponse(list)
