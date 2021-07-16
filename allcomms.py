from googleapiclient.discovery import build
import sys
from apikey import *
from datetime import datetime
startTime = datetime.now()

def channel_videos(channel_id):
    # creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)
    # retrieve youtube video results
    video_response=youtube.playlistItems().list(
            part='contentDetails',
            playlistId=channel_id
            ).execute()
    #print(video_response['items'][0]['snippet']['resourceId']['videoId'])
    print(video_response)

# Call function
print(channel_videos(sys.argv[1]))
print("retrieved in {} ".format(datetime.now() - startTime))
