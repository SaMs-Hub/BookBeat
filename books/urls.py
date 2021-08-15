from django.conf.urls import url
from django.contrib import admin
from django.urls import path,translate_url
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add/', views.BookCreate.as_view(), name='book-add'),

]
