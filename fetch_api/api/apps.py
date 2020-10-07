from django.apps import AppConfig
from threading import Thread
# from .models import Videos
# imports to use GOOGLE API
from googleapiclient.discovery import build
import apiclient


class ApiConfig(AppConfig):
    name = 'api'
