from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'note'
urlpatterns = [
    path('', views.indexf, name='index'),
    path('save_todo', views.save_todo, name='save_todo'),
    path('rm',views.rm,name='rm'),
    path('delete',views.delete,name='delete'),
    path('tick',views.tick,name='tick'),
    path('change',views.change,name='change'),
]