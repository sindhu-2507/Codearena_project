from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Friend(models.Model):
	#author_name = models.ForeignKey(User, on_delete=models.CASCADE)
	author_name = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
	#author_name = models.CharField(max_length=100, default=User.objects.get(username=))
	friend_name = models.CharField(max_length=100, default="")
	email = models.EmailField(default="")

	class Meta:
		unique_together = ('friend_name', 'email',)
		
	def __str__(self):
		return self.friend_name
		
	def get_absolute_url(self):
		return reverse('blog-home')


class Post(models.Model):
	DETAIL_CHOICES = (
      (1, 'food'),
      (2, 'clothing'),
      (3, 'groceries'),
      (4, 'hospital'),
      (5, 'travel'),
      (6, 'housing'),
      (7, 'movies'),
      (8, 'others'),
  	)

	OPTION_CHOICES = (
		(1, 'paid by user and split equally'),
		(2, 'paid by friend and split equally'),
		(3, 'you owe the full amount'),
		(4, 'they owe the full amount'),
	)

	author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
	#author = models.ForeignKey(Friend, related_name='author', on_delete=models.CASCADE)
	#author = models.CharField(max_length=100, default="")
	#friend = models.ForeignKey(Friend, related_name='friend', on_delete=models.CASCADE)
	#request = GenericForeignKey('author', 'friend')
	friend = models.CharField(max_length=100, default="")
	details = models.PositiveSmallIntegerField(choices=DETAIL_CHOICES)
	description = models.CharField(max_length=500, default="")
	date_posted = models.DateTimeField(default=timezone.now)
	options = models.PositiveSmallIntegerField(default=0, choices=OPTION_CHOICES)
	amount = models.PositiveIntegerField(default=0)
	abs_amount = models.IntegerField(default=0)

	def __str__(self):
		return self.friend

	def get_absolute_url(self):
		#return reverse('blog-home', kwargs={'pk': self.pk})
		return reverse('blog-about')