from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('match/new/', views.create_match, name='create_match'),
]