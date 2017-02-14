
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
import random
from cryptography.fernet import Fernet
from django.core.mail import send_mail
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
	password=""
	for i in range(0,3):
		password+=first[random.randrange(0,26)]
		password+=mid[random.randrange(0,10)]
		password+=last[random.randrange(0,26)]

	key=Fernet.generate_key()
	cipher_suite=Fernet(key)
	encoded_pass=cipher_suite.encrypt(password)

	#body=password+"\n"+request.POST.get('email')

	link="http://www.IIITDMsdg.com/login?token=" + encoded_pass
	send_mail(
		'details for login',
		link,
		'parasagarwal@iiitdmj.ac.in',
		[request.POST.get('email')]
	)
	print request
	list=[link]
	return render(request,'mail/index.html')
