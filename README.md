# DownCloud-Tumblr

This is based off of the script that I made to download all of the soundcloud links from a particular subreddit when SC was about to go under. Well, now something similar is happening to Tumblr so here we go again. This is pretty much a wrapper to the following Tumblr program, so much appreciation to them:  https://github.com/dixudx/tumblr-crawler

It needs 4 things:

[Python](https://www.python.org/downloads/)

[Praw (pip install praw)](https://praw.readthedocs.io/en/latest/)

[Reddit API Key](https://github.com/reddit/reddit/wiki/OAuth2)

Put the API stuff in an api_info.py file. Feel free to rename the example I threw in there

Usage:
```
python3 downcloud.py subreddit_name

python3 downcloud.py badwomensanatomy
```

Details:

Searches through a subreddit for tumblr links, then downloads all of the media from that blog. First it finds the blog name and creates a directory for the music and dumps it in there. If a directory already exists for that artist, it is skipped. All individual files are kept in a folder with the following naming convention:

"subreddit name"/Single Images
