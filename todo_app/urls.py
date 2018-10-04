from django.urls import path 
from django.contrib import admin
from django.urls import path
from todo_app.views import TodoView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^$',TodoView.as_view()),
	path('Todo/', TodoView.as_view())
]
