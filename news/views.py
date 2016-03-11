#importings
from __future__ import unicode_literals
import threading

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from .models import News , Team , League
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages import get_messages
#imports of models 

from django.contrib.auth.models import User

# Create your views here.
def main(request):

	# if email is not sepcified
	# if request.user.is_authenticated() and not request.user.email:
	#	messages.add_message(request, messages.WARNING, 'Пожалуйста укажите ваш email чтобы продолжить.',fail_silently=True)
	#	return redirect(reverse("auths:modify_profile"))

	#initialize variables
	args={}
	args.update(csrf(request))
	args['footback_link'] = "news:main"
	#need_for_every(args,request)

	# query of objects
	news = News.objects.all()

	# paginator
	paginator = Paginator(news, 3)
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
 		news = paginator.page(paginator.num_pages)

	# assigning to dicrionary 
 	args['leagues'] = League.objects.all()
	args['news'] = news
	return render_to_response('news/main.html',args)
def league(request, league_id):
	# initialize variables
	args={}
	args.update(csrf(request))
	args['footback_link'] = "news:league"
	# need_for_every(args,request)

	# query of objects
	league = get_object_or_404(League, pk=league_id)
	leagues = League.objects.all()
	teams = league.team_set.all()
	news = News.objects.filter(team__league = league)

	# paginator
	paginator = Paginator(news, 3)
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
 		news = paginator.page(paginator.num_pages)
	# assigning to dicrionary 
 	args['teams'] = teams
 	args['league'] = league
 	args['leagues'] = leagues
	args['news'] = news

	return render_to_response('news/league.html',args)

def team(request, team_id ):
	#initialize variables
	args={}
	args.update(csrf(request))
	args['footback_link'] = "news:team"
	#need_for_every(args,request)

	# query of objects
	team = get_object_or_404(Team, pk = team_id)
	league = get_object_or_404(League, pk=team.league.id)
	teams = league.team_set.all()
	leagues = League.objects.all()
	news = News.objects.filter(team = team)

	# paginator
	paginator = Paginator(news, 3)
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
 		news = paginator.page(paginator.num_pages)

	# assigning to dicrionary 
 	args['teams'] = teams
 	args['team'] = team
 	args['league'] = league
 	args['leagues'] = leagues
	args['news'] = news

	return render_to_response('news/team.html',args)

def content(request, content_id):
	#initialize variables
	args={}
	args.update(csrf(request))
	args['footback_link'] = "news:team"
	#need_for_every(args,request)

	# query of objects
	content = get_object_or_404(News, pk = content_id)
	news = News.objects.filter(team = content.team)
	# this news is readed once more time
	readed = content.readed
 	content.readed = readed + 1
	content.save()
	# assigning to dicrionary 
 	args['content'] = content
 	


	return render_to_response('news/content.html',args)

def need_for_every(args,request):
	"""this function does everything usual that is needed for every def"""
	
	args['user'] = request.user
	if request.user.is_authenticated():
		user_wish = Wish.objects.filter(user=request.user)
		temp = []
		for wish in user_wish:
			temp.append(wish.instance)
		args['user_wish'] = temp
	# dealing with messages
	args['messages'] = list(get_messages(request))
	return args
