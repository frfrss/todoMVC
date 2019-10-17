from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'note'
urlpatterns = [
    path('', views.index, name='index'),
    path('vote', views.vote, name='vote'),
    path('clear',views.clear,name='clear'),
]