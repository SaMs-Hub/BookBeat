from django.conf.urls import url
from django.contrib import admin
from django.urls import path,translate_url
from . import views
from django.views.static import serve
from django.conf import  settings

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add/', views.BookCreate.as_view(), name='book-add'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
