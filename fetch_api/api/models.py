from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(null=True,blank=True,max_length=500)
    description = models.CharField(null=True, blank=True, max_length=6000)
    publishingDateTime = models.DateTimeField()
    thumbnailsUrls = models.URLField()
    channelTitle = models.CharField(null=True,blank=True,max_length=500)
