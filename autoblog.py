#!/usr/bin/python
import datetime
from youtube_upload import main 

# uploads a video, returns the video URL
# ex. url = uploadVideo('New Video', 'This is the description', '/home/pi/autoblog/video_samples/sample.mov')


sampleTree = [
  {
    'title': 'Sacramento-Buying-Trip-April-2020',
    'desc': 'This was a trip we made to Sacramento to resue a 1986 Honda TLR200 Reflex trials bike from a dusty shed./n/n- Honda TLR200 Reflex',
    'dateCreated': '2020-4-11',
    'dateUpdated': '2020-4-12',
    'photos': ['https://s3.com/photo1', 'https://s3.com/photo2', 'https://s3.com/photo3'],
    'video': 'https://youtube.com/asdf',
    'map': 'https://maps.google.com/qwert'
  }
]

### MEDIA PUBLISHERS

def uploadPhoto(path):
  # upload photo to S3
  return 'URL'

def uploadVideo(title, description, path):
  uploaderArgs = ['--title={0}'.format(title), '--description={0}'.format(description), path]
  return main.main(uploaderArgs)

def uploadMap(path):
  # upload map to mymaps
  return 'URL'


### DECISION MAKERS

def loadHDDContentTree():
  # generate a dictionary based on the folder structure
  return 0

def loadBlogContentTree():
  # generate a dictionary based on the blog markdowns
  return 0

def compareContentTrees(treeA, treeB):
  # compare trees and create a list of 

def updateBlogContentTree():
  # compareContentTree, if none skip
  # if com 
  # upload and update each piece of content with the updated URL
  return 0

def updateBlog():
  # generate new tree into md structure, then verify that it has no diff with HDD
  # push blog to git if there are any updates (will autotrigger upload)
  #
  return 0

if __name__ == '__main__':
  loadHDDContentTree()





## INPUT - Folder structure on HDD like this.... 

# FAKEHDD/
# `-- Sacramento-Buying-Trip-April-2020
#     |-- desc.txt
#     |-- IMG_4406.jpeg
#     |-- IMG_4413.jpeg
#     |-- IMG_4437.jpeg
#     |-- sample.gpx
#     `-- sample.mov

## OUTPUT - Blog posts with resources uploaded....

# |   `-- Sacramento-Buying-Trip-April-2020
# |       `-- index.md