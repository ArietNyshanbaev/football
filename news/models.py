from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class League(models.Model):
	"""League of the team"""


	title = models.CharField('название лиги', max_length=100)
	def __unicode__(self):
		return self.title
   
	class Meta:
		verbose_name = "Лига"
		verbose_name_plural = "Лиги"

class Team(models.Model):
	"""Team in league"""

	title = models.CharField('название команды',max_length=100)
	league = models.ForeignKey(League, verbose_name='лига')
	image_emblem = models.ImageField('значок клуба', upload_to='media', null=True, blank=True)
	image_squad = models.ImageField('состав', upload_to='media', null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Команда"
		verbose_name_plural = "Команды"

class News(models.Model):
	"""News for each team """
	title = models.CharField('тема', max_length=100)
	body = models.TextField('тело')
	team = models.ForeignKey(Team, verbose_name='команда')
	image = models.ImageField('фото', upload_to='media', null=True, blank=True)
	added_date = models.DateTimeField('дата добавления', default=datetime.now)
	readed = models.IntegerField('количесто просмотров', default=0)
	added_by = models.ForeignKey(User, verbose_name='добавлено кем')
    
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "Новость"
		verbose_name_plural = "Новости"