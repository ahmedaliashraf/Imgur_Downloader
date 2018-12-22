#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Easily download images from an imgur album
through album Id regardless of image format.

Created on Mon Jun  5 07:35:01 2017
@author: Ahmed Ashraf (ultimat3pro)
"""

import urllib.request
import re
import os

def checkIfExists(albumId):
    fullLink = "https://imgur.com/a/"+albumId
    try:
        urllib.request.urlopen(fullLink)
    except urllib.request.HTTPError as err:
        erCode = err.code
        if(erCode==404):
            print("Album doesn't exist")
        return erCode
    
def findImagesIn(albumId):
    print("Finding images in album....")
    #Create album link
    prefix = "https://imgur.com/a/"
    albumLink = prefix + albumId+"/layout/blog"
    #read source
    page = urllib.request.urlopen(albumLink)
    lines = str(page.readlines())
    #Find end identifier and type of image
    images = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', lines)
    download(images,albumId)
    #return images
    
def download(images,albumId):
    print("Creating direct links to images...")
    #create image array without duplicates
    imgB = list(set(images))
    
    #create complete path
    path = "albums/"+albumId+"/"
    
    #Create directory if not exists from path
    if not os.path.exists(path):
        os.makedirs(path)
    
    #Create list with completed link for each image
    imgLinks = []
    for i in range(len(imgB)):
        url = "https://i.imgur.com/"+imgB[i][0]+imgB[i][1]
        imgLinks.append(url)
    
    print("Downloading images...")
    
    #Retrieve images following links
    for i in range(len(imgLinks)):
        urllib.request.urlretrieve(imgLinks[i],path+str(i)+imgB[i][1])
        print(imgLinks[i]+"  .....done.")
    
    print("Download complete")
    
def main():
    albumId = input("Please enter the id of the album: ")
    while (len(albumId)==0 or checkIfExists(albumId)!=None):
        albumId = input("Please enter the id of the album: ")
    findImagesIn(albumId)
    #findImagesIn("tFOwd")
    #findImagesIn("UrVN2")
    
main()    