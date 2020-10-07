from django.shortcuts import render
from django.http import HttpResponse

from .api_test import getnewposts
from .models import Videos
from .serializers import VideosSerializer

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def fetch_new_posts(request):
    try:
        getnewposts()
        return HttpResponse("new videos have been fetched! add /api to base url to view changes")
    except:
        return HttpResponse("Some error encountered")

class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title']
    filter_fields = ['channelTitle']
    #to sort data in reverse chronlogical order (by default)
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination
