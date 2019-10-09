from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) # user에 맞게 정해지도록 설정합니다.
    title = models.CharField(max_length=30)
    body = models.TextField()

class Album(models.Model): # 사진
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) # 위와 마찬가지로 user에 맞게 정해지도록 합니다.
    image = models.ImageField(upload_to="images") # images 폴더에 업로드 됩니다.
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to="files") # files 폴더에 업로드 됩니다.
    desc = models.CharField(max_length=100)
