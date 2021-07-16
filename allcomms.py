from googleapiclient.discovery import build
import sys
from apikey import *
from datetime import datetime
startTime = datetime.now()

def channel_videos(channel_id):
    video_ids = []
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_response=youtube.playlistItems().list(
            part='contentDetails',
            playlistId=channel_id
            ).execute()
    while video_response:
        for item in video_response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        if 'nextPageToken' in video_response:
            token = video_response['nextPageToken']
            video_response = youtube.playlistItems().list(
                    part = 'contentDetails',
                    playlistId = channel_id,
                    pageToken = token
                ).execute()
        else:
            break

    return video_ids

def video_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_response=youtube.videos().list(
            part='statistics',
            id=video_id
            ).execute()
    number_of_comments = video_response['items'][0]['statistics']['commentCount']
    return number_of_comments




video_ids = channel_videos(sys.argv[1])
totalvids = len(video_ids)
print("found {} videos".format(totalvids))
totalcomments = 0
fetchedvids = 0
for video_id in video_ids:
    totalcomments += int(video_comments(video_id))
    fetchedvids += 1
    print("Progress : {}%".format(round(fetchedvids/totalvids*100,1)), end="\r")

print("Total comments : {}".format(totalcomments));
print("retrieved in {} ".format(datetime.now() - startTime))
