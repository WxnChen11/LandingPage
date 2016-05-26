from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp #already in newsletters module, so can use .models. Other app-> from someOtherApp.models

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp


admin.site.register(SignUp, SignUpAdmin)