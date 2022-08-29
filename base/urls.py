from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('get_regions/', views.get_regions, name = 'regions'),
	path('searchResults/', views.searchResults, name='searched'),
	path('get_channel_statistics/', views.get_channel_statistics, name = 'statistics'),
	path('get_comments/', views.get_comments, name = 'comments'),
	path('buttonClick/', views.buttonClick, name = 'buttonClick'),
	path('buttonClickStats/', views.buttonClickStats, name = 'buttonClickStats'),
]