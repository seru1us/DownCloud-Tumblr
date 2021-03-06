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

subarg = reddit.subreddit(sys.argv[1])
strarg = str(subarg)
resetcwd = str(os.getcwd())

slash = '/'
underscore = '_'
period = '.'

# for what it's worth, there is probably a better way to do all of this split/join nonsense.

if not os.path.exists(strarg):
    os.makedirs(strarg)
    print(strarg + ' not found, creating...')
else:
    print(strarg + ' already exists, skipping...')

if not os.path.exists(strarg + '/Single Images'):
    os.makedirs(strarg + '/Single Images')
    print(strarg + '/Single Images not found, creating...')
else:
    print(strarg + '/Single Images already exists, skipping...')

# search the sub for tumblr related links.
for submission in reddit.subreddit(strarg).search(f'site:tumblr.com', sort='relevance', syntax='lucene', time_filter='all', limit=None):

    print("Attempting to download " + submission.url)
    # save "only images" if we want to. 
    if "media" in slash.join(submission.url.split(slash)[:3]) and save_cdn_only_links:
        # take the url and force the highest resolution (this is kinda dirty).
        cdn_url = underscore.join(submission.url.split('_')[:-1]) + '_1280.' + period.join(submission.url.split('.')[-1:])
        # Saves this into the "Single Images" folder, with the title the submission title.
        try:
            urllib.request.urlretrieve(cdn_url, os.path.join(strarg + '/Single Images', submission.title))
        except:
            print("This title is not formatted well, not saving this image.")
    else:

        # so it isn't a link to a pic. Grab the blog name and pass it to the scripts
        blog_name = (submission.url.split('/')[2]).split('.')[0]
        
        # Check to make sure we haven't downloaded it from a different sub.
        if blog_name in open('blog_dl_history').read():
            print("Blog found in history, not downloading again.")
            open('blog_dl_history').close()
        else:
            # set the working directory to the folder that matches the Subreddit name before running tpvr.
            os.chdir(strarg)
            del sys.argv[0]
            sys.argv = ['', blog_name]
            runpy.run_path('../tumblr-crawler/tumblr-photo-video-ripper.py', run_name='__main__')
            os.chdir(resetcwd)

            # Record the blog name to disk. Since we are using dynamic directories, we need to manually check to make sure we aren't
            # downloading a blog twice.
            open('blog_dl_history').close()
            f = open('blog_dl_history', 'a')
            f.write(blog_name + "\n")
            f.close()