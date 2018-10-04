from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Todo

# def index(request):
# 	context = {}
# 	return render(request, 'todo_app/index.html', context)

class TodoView(TemplateView):
	template_name = 'index.html'
	todo_list = Todo.objects.order_by('id')
	cont = Todo