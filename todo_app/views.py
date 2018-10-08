from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def first(request):
	context ={}
	return render(request, 'todo_app/first.html', context)

def index(request):
	todo_list = Todo.objects.order_by('id')
	form = TodoForm()
	context = {'todo_list': todo_list, 'form' : form}
	return render(request, 'todo_app/index.html', context)

@require_POST
def addTodo(request):
	form = TodoForm(request.POST)
	print(request.POST['text']) 
	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()
	return redirect('index')

def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()
	return redirect('index')

def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()
	return redirect('index')

def deleteAll(request):
	Todo.objects.all().delete()
	return redirect('index')











# class TodoView(TemplateView):
# 	template_name = 'index.html'
# 	todo_list = Todo.objects.order_by('id')

# def TourView(request):
# 	return render(request, 'todo_app/tour.html',{})
# 	
# 	
# 	