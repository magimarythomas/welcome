from django.conf.urls import url
from django.urls import path
from .import views
app_name="music"
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:album_id>/', views.detail, name='detail'),
    
    path('<int:album_id>/<song_logo>/', views.index1, name='index1'),
    path('<int:album_id>/<song_logo>/<song_video>/', views.index2, name='index2'),
    path('<int:album_id>/<song_logo>/<song_video>/<images>/', views.index3, name='index3')
    ]
