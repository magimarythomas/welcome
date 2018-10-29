from django.http import Http404
from django . shortcuts import render
from .models import Album,songs
def index(request):
     all_albums = Album.objects.all()
     return render(request,'music/index.html',{'all_albums':all_albums})
def detail(request,album_id):
    try:
         albums = Album.objects.get(pk=album_id)
    except:
         raise Http404("album doesnot exist")
    return render(request,'music/detail.html/',{'albums':albums})


def index1(request,album_id,song_logo):
    try:
          albums = Album.objects.get(pk=album_id)
    except:
        raise Http404("album doesnot exist")
    return render(request,'music/indi.html/',{'albums':albums})

def index2(request,album_id,song_logo,song_video):
    try:
          albumss = Album.objects.get(pk=album_id)
    except:
        raise Http404("album doesnot exist")
    return render(request,'music/first.html/',{'albumss':albumss})
def index3(request,album_id,song_logo,song_video,images):
    try:
          albumsss = Album.objects.get(pk=album_id)
    except:
        raise Http404("album doesnot exist")
    return render(request,'music/second.html/',{'albumsss':albumsss})

