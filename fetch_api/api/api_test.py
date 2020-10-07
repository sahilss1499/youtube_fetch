from .models import Videos
from fetch_api import settings
from datetime import datetime, timedelta
# imports for GOOGLE_API
from googleapiclient.discovery import build
from apiclient.errors import HttpError

# a function to populate our database with new search results
def getnewposts():
    apikeys = settings.API_KEYS
    current_time = datetime.now()
    # since we need to get the posts those were posted 5 minutes from current_time
    req_time = current_time - timedelta(minutes=5)
    # removing microsecond from time (reason:refer doc of youtube api)
    # req_time.replace(microsecond=0)
    flag=False
    for apikey in apikeys:
        try:
            # we can connect to youtube sevice via build function
            # naming this service as youtube
            youtube = build("youtube", "v3", developerKey=apiKey)
            # calling an instance method and make a request
            req = youtube.search().list(part="snippet", q="cricket", order="date",
                                        maxResults=50, publishedAfter=(req_time.replace(microsecond=0).isoformat()+'Z') )
            response = req.execute()
            flag=True

        # quotaExceeded has status code 403 so we need not break on it
        except HttpError as er:
            err_code = e.resp.status
            if not(err_code == 400 or err_code == 403):
                break

        if flag:
            break

# if flag is set then we store tge response in our model

    if flag:
        for obj in response['items']:
            title = obj['snippet']['title']
            description = obj['snippet']['description']
            publishingDateTime = obj['snippet']['publishedAt']
            thumbnailsUrls = obj['snippet']['thumbnails']['default']['url']
            channelTitle = obj['snippet']['channelTitle']

            Videos.objects.create(title=title, description=description
                    publishingDateTime=publishingDateTime, thumbnailsUrls=thumbnailsUrls
                    channelTitle=channelTitle)
