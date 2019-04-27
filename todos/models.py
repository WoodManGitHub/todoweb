from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class HashTag(models.Model):
	title = models.CharField(max_length=50)
	created_at = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class Todo(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(null=True)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	hashtags = models.ManyToManyField(HashTag)

	def __str__(self):
		return self.title

class TodoAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'completed', 'created_at', 'user']
