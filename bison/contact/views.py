from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.forms.models import modelform_factory
from contact.models import Contact

def my_view(request):
	contactForm = modelform_factory(Contact)
	return render(request,"contact/list.html",{"contactForm":contactForm})