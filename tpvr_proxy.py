import os
import sys

 # this is necessary because of the hyphens in the tumblr crawler app name... ugh

filename = "tumblr-crawler/tumblr-photo-video-ripper.py"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    module = __import__(module_name)
finally:
    sys.path[:] = path # restore

globals().update(vars(module))