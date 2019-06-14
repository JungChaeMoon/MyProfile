from django.urls import path, include
from mainapp import views

app_name='mainapp'

urlpatterns = [

    path('mainapp/', views.index, name='index'),
    path('video/', views.detail, name='detail')

]