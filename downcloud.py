import os
import praw
import subprocess
import sys
from api_info import *

reddit = praw.Reddit(client_id=praw_client_id,
                     client_secret=praw_client_secret,
                     password=praw_password,
                     user_agent=praw_user_agent,
                     username=praw_username)

#subarg = reddit.subreddit(sys.argv[1])
subarg = "futurefunk"

slash = "/"

for submission in reddit.subreddit(str(subarg)).search('site:soundcloud.com', limit=None):
    dalink = slash.join(submission.url.split(slash)[:4])
    print(dalink)

    try:
        directory = submission.secure_media['oembed']['author_name']
    except Exception:
        directory = dalink.split(slash)[-1]

    odirectory = directory.strip() + '/%(title)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': odirectory,
        'ignoreerrors': True

    }

    if not os.path.exists(directory):
        #os.makedirs(directory)
        print('Artist ' + directory + ' already exists, skipping...')
    else:
        print('Artist ' + directory + ' already exists, skipping...')

