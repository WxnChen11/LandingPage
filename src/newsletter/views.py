from django.shortcuts import render

from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)

	context = {
		"title" : title,
		"form" : form,
	}

	# if request.user.is_authenticated(): #if user is logged in, display their name, else Welcome
	# 	title = "My Title %s" %(request.user)

	#add a form
	# if request.method == "POST":
	# 	print request.POST

	if form.is_valid():

		#print request.POST['email'] -> not recommended
		instance = form.save(commit = False)

		full_name = form.cleaned_data.get("full_name")

		if not full_name:
			full_name = "New Full Name"
		instance.full_name = full_name
		instance.save()
		#print instance.email
		#print instance.timestamp

		context = {
			"title" : "Thank You" #form will now be blank
		}


	return render(request,"home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		for key, value in form.cleaned_data:
			print key, value
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		print email, message, full_name

	context = {
		"form" : form,
	}

	return render(request, "forms.html", context)