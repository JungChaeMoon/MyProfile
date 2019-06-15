from django.urls import path, include
from mainapp import views

app_name='mainapp'

urlpatterns = [

    path('chaemoon/', views.index, name='index'),
    path('video', views.video, name='video'),
    path('comment/', views.detail, name='detail'),
    path('redirect/', views.redirect, name='redirect'),
]