from django.db import models
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField(max_length=1000)
    
    def __str__(self):
        return self.album_title+'-'+self.artist

class songs(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
   
    file_type=models.CharField(max_length=100)
    song_title=models.CharField(max_length=250)
    song_logo = models.FileField(max_length=1000)
    song_video = models.FileField(max_length=1000)
    image = models.FileField(max_length=1000)
    def __str__(self):
        return self.song_title
