import os
import flask
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import sys
sys.path.append("C:/Users/owner/Desktop/CS/hackbu2019/CollabFinder/youtube_tutorial/")
from youtube_videos import youtube_search

test = youtube_search("spinners")
print(test)
