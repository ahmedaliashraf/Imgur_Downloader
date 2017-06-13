# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 07:35:01 2017

@author: Ultimate Pro
"""

import urllib
import re
import os


def createLinksForImagesIn(albumId,imType):
    prefix = "https://imgur.com/a/"
    albumLink = prefix + albumId
    
    page = urllib.request.urlopen(albumLink)
    lines = str(page.readlines())
    print(lines)
    images = re.findall("i\.imgur\.com/\w+\."+imType,lines)
    #images = images + re.findall("(i\.imgur\.com/[a-zA-Z0-9]+\.jpg)",lines)
    
    return images
    
def download(images,albumId):
    #create image array without duplicates
    imgB = list(set(images))
    
    #create complete path
    path = "albums/"+albumId+"/"
    
    #Create directory if not exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    
    for i in range(len(imgB)):
        urllib.request.urlretrieve("https://"+imgB[i],path+str(i)+".gif")
 
    
def main():
    imgs = createLinksForImagesIn("tFOwd","jpg")
    download(imgs,"tFOwd")
    
main()    