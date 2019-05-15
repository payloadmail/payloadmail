from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from . import emailparser, userlogin


def home(request):
	#return HttpResponse('<h1>Home</h1>')
	emails = {
		'emails': emailparser.check_emails()
	}
	return render(request, 'mail/home.html', emails)

def login(request):
	if request.method == 'POST' and 'login' in request.POST:
		temp = userlogin.UserForm(request.POST)
		if temp.validate():
			useremail = temp.get_user_email()
			emails = {
				'emails': emailparser.check_emails(useremail)
			}
			emails["user"] = useremail
			emails["username"] = useremail.split('@')[0]
			return render(request, 'mail/home.html', emails)
	elif request.method == 'POST' and 'delete' in request.POST:
		user = request.POST['delete']
		emailparser.delete_emails(user)
		emails = {}
		emails["username"] = user.split('@')[0]
		return render(request, 'mail/home.html', emails)
	elif request.method == 'POST' and 'logout' in request.POST:
		log = "out"
	return render(request, 'mail/login.html')