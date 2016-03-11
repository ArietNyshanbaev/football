#importings
from __future__ import unicode_literals
import threading
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages import get_messages
#impoer of models 

from django.contrib.auth.models import User

def main(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	
	return render(request, 'main/main.html', args)