from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Friend
from django import forms
from django.contrib import messages
from django.db import models
from django.conf import settings

def home(request):
	return render(request, 'blog/main.html')


class FriendCreateView(CreateView):
	model = Friend
	fields = ['friend_name', 'email']

	def form_valid(self, form):
		x = form.instance.friend_name
		y = User.objects.filter(username=x)
		if y and y[0].email == form.instance.email:
			form.instance.author_name = self.request.user
			super().form_valid(form)
			return redirect('blog-home')
		else:
			messages.warning(self.request, "Email id does not match with friend")
			return redirect('friend-create')
		return super().form_valid(form)


class FriendListView(TemplateView):
	model = Friend
	template_name = 'blog/home.html'
	context_object_name = 'friends'

	def get_context_data(self, **kwargs):
		context = super(FriendListView, self).get_context_data(**kwargs)
		context.update({
            'abs_amount': Post.objects.raw('''
				SELECT
				Friend.friend_name as friend,
				Friend.author_name as author, 
				sum(Post.abs_amount) as abs_amount,
				FROM Post
				INNER JOIN Friend
				ON
				Post.friend = Friend.friend_name
				AND
				Post.author = Friend.author_name
				GROUP BY Post.Friend, Post.author
					''')
            })
		return context


class PostCreateView(CreateView):
	model = Post
	fields = ['friend', 'details', 'description', 'options', 'amount']
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def form_valid(self, form):
		form.instance.author = self.request.user
		z = Friend.objects.filter(author_name=form.instance.author, friend_name=form.instance.friend)
		if z:
			opt = form.instance.options
			if opt == 1:
				form.instance.abs_amount = form.instance.amount/2
			elif opt == 2:
				form.instance.abs_amount = form.instance.amount/2
			elif opt == 3:
				form.instance.abs_amount = form.instance.amount
			elif opt == 4:
				form.instance.abs_amount = form.instance.amount
			super().form_valid(form)
			return redirect('blog-about')
		else:
			messages.warning(self.request, "Friend does not exist, please add friend")
			return redirect('friend-create')
		return super().form_valid(form)
		


class PostListView(ListView):
	model = Post
	template_name = 'blog/about.html'
	context_object_name = 'posts' 
	ordering = ['date_posted']


#class PostDetailView(DetailView):
	#model = Post



# class PostUpdateView(UpdateView):
# 	model = Post
# 	fields = ['options', 'amount']

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# class PostDeleteView(DeleteView):
# 	model = Post
# 	success_url = '/'

# def about(request):
# 	return render(request, 'blog/about.html', {'title': 'About'})

