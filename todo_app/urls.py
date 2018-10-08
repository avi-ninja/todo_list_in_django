from django.urls import path 
from django.urls import path
# from todo_app.views import TodoView #TourView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$',TodoView.as_view()),
	# path('Todo/', TodoView.as_view()),
	#url(r'^tour/$', views.TourView, name='tour'),
	path('first',views.first, name='first'),
	path('', views.index, name='index'),
	path('add', views.addTodo, name='add' ),
	path('complete/<todo_id>', views.completeTodo, name='complete'),
	path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
	path('deleteall', views.deleteAll, name='deleteall')
]
