from googleapiclient.discovery import build
import sys
from apikey import *
from datetime import datetime
startTime = datetime.now()

def video_comments(video_id):
    # creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)
    # retrieve youtube video results
    video_response=youtube.videos().list(
            part='statistics',
            id=video_id
            ).execute()
    number_of_comments = video_response['items'][0]['statistics']['commentCount']
    return number_of_comments

# Call function
print(video_comments(sys.argv[1]))
print("retrieved in {} ".format(datetime.now() - startTime))
