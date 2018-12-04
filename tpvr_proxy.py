 # this is necessary because of the hyphens in the tumblr crawler app name
 
tmp = __import__('tumblr-crawler/tumblr-photo-video-ripper')
globals().update(vars(tmp))