from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todos.models import Todo

def index(request):
	items = []
	tag = None
	
	if request.user.is_authenticated:
		tag = request.GET.get('tag')
		items = filter_results(request.user, tag)
	return render(request, 'index.html', {'items': items, 'tag': tag})

def filter_results(user, tag):
	if tag == 'completed':
		return Todo.objects.filter(user=user, completed=True).order_by('-created_at')
	elif tag == 'pending':
		return Todo.objects.filter(user=user, completed=False).order_by('-created_at')
	else:
		return Todo.objects.filter(user=user).order_by('-created_at')

@login_required
def create(request):
	return render(request, 'form.html', {'form_type': 'create'})

@login_required
def save(request):
	title = request.POST.get('title')
	description = request.POST.get('description')
	form_type = request.POST.get('form_type')
	id = request.POST.get('id')

	if title is None or title.strip() == '':
		messages.error(request, 'Item not saved.')
		return redirect(request.META.get('HTTP_REFERER'))
	
	if form_type == 'create':
		todo = Todo.objects.create(title=title, description=description, created_at=timezone.now(), user=request.user)
	elif form_type == 'edit' and id.isdigit():
		todo = Todo.objects.get(pk=id)
		todo.title = title
		todo.description = description
		todo.save()
	
	messages.info(request, 'Saved.')
	return redirect('index')

@login_required
def edit(request, id):
	todo = Todo.objects.get(pk=id)
	
	if request.user.id != todo.user.id:
		messages.error(request, 'You are not authorized.')
		return redirect('index')
	
	return render(request, 'form.html', {'form_type': 'edit', 'todo': todo})

@login_required
def delete(request, id):
	todo = Todo.objects.get(pk=id)
	
	if request.user.id == todo.user.id:
		messages.info(request, 'This item has been deleted.')
		todo.delete()
	return redirect('index')

	messages.error(request, 'You are not authorized.')
	return redirect('index')

@login_required
def complete(request, id):
	todo = Todo.objects.get(pk=id)

	if request.user.id == todo.user.id:
		messages.info(request, 'Complete!')
		todo.completed = True
		todo.save()
	return redirect('index')
	
	message.error(request, 'You are not authorized.')
	return redirect('index')
