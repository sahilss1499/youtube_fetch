# youtube_fetch
Made an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
It is built using Django and Django Rest Framework.

## Project Setup Guide:
- Clone the repository
- Make a `pip install -r requirements.txt` (after going into the required directory)  to install all the requirements/dependencies preferably setup a virtual environment and then do it. 
(**Note**- Your system must have python installed)
- In settings.py there is a list called `API_KEYS` remove the pre-existing and refer [this](https://developers.google.com/youtube/v3/docs) 
and get yourself your API key(s) and add them into the `API_KEYS` list.
- Now, you are good to go, run your server by `python manage.py runserver`
- To get new posted videos add `new/` to the base url.
- Now, add `api/` to the base url to see changes.
- Each time you add `new/` to the base url you populate the database with the new videos related to cricket query posted in the past 5 minutes.

#### Note(For users whose system supports Cron Jobs): 
- Just configure the settings.py as per [this](https://django-cron.readthedocs.io/en/latest/installation.html) and write a cron class hat extends the CronJobBase class 
in api_test.py inside api app file and call the `getnewposts()` function inside `do(self)` function as prescribed by
 [this](https://django-cron.readthedocs.io/en/latest/installation.html) and set `RUN_EVERY_MINS = 5` 
- Doing this your database will automatically be flooded with the new posts in the past 5 mins. No need to go to `new/` path to fetch new videos.

### Demo:
- Before making a resquest you can see that there are 20 pages (each page contains 10 objects):
 ![alt text](https://github.com/sahilss1499/youtube_fetch/blob/master/DemoImages/BeforeFetchRequest.jpg)
- Making a request to get new videos(this should be done in interval of 5 min):
 ![alt text](https://github.com/sahilss1499/youtube_fetch/blob/master/DemoImages/ToFetchNewVideos.jpg)
- After getting the videos you can see that our there are 25 pages now:
 ![alt text](https://github.com/sahilss1499/youtube_fetch/blob/master/DemoImages/AfterFetchRequest.jpg)
- In the image given below you can see that the results are by default in reverse chronological order:
 ![alt text](https://github.com/sahilss1499/youtube_fetch/blob/master/DemoImages/DefaultOrdering.jpg)
- You can find the basic searching(on basis of title) and filtering(on basis of channelTitle) demo in the DemoImages file.
