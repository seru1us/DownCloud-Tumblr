import os
import praw
import subprocess
import sys
import urllib.request
import runpy
from api_info import *

reddit = praw.Reddit(client_id=praw_client_id,
                     client_secret=praw_client_secret,
                     password=praw_password,
                     user_agent=praw_user_agent,
                     username=praw_username)

#subarg = reddit.subreddit(sys.argv[1])
subarg = "badwomensanatomy"

slash = '/'
underscore = '_'
period = '.'

# for what it's worth, there is probably a better way to do all of this split/join nonsense.

if not os.path.exists(subarg):
    os.makedirs(subarg)
    print('Artist ' + subarg + ' not found, creating...')
else:
    print('Artist ' + subarg + ' already exists, skipping...')

if not os.path.exists(subarg + '/Single Images'):
    os.makedirs(subarg + '/Single Images')
    print('Artist ' + subarg + '/Single Images not found, creating...')
else:
    print('Artist ' + subarg + '/Single Images already exists, skipping...')

# search the sub for tumblr related links.
for submission in reddit.subreddit(str(subarg)).search(f'site:tumblr.com nsfw:{praw_sub_nsfw}', limit=None):

    # save "only iamges" if we want to. 
    if "media" in slash.join(submission.url.split(slash)[:3]) and save_cdn_only_links:
        # take the url and force the highest resolution (this is kinda dirty).
        cdn_url = underscore.join(submission.url.split('_')[:-1]) + '_1280.' + period.join(submission.url.split('.')[-1:])
        # Saves this into the "Single Images" folder, with the title the submission title.
        urllib.request.urlretrieve(cdn_url, os.path.join(subarg + '/Single Images', submission.title))
    else:
        # so it isn't a link to a pic. Grab the blog name and pass it to the script
        del sys.argv[0]
        sys.argv = ['', (submission.url.split('/')[2]).split('.')[0]]
        runpy.run_path('./tumblr-crawler/tumblr-photo-video-ripper.py', run_name='__main__')
        


