# -*- coding: utf-8 -*-
"""
@author: Loïc ARGENTIER
"""

import argparse
from pytube import YouTube
from pytube import Playlist
import subprocess
import os
from pytube.exceptions import RegexMatchError
import re

class YTdownloader():
    def __init__(self):
        self.url=args.url
        self.path=args.path
        self.size=0
        self.nb_song=0
        try:
            self.playlist=False
            self.yt=YouTube(self.url)
        except RegexMatchError:
            self.playlist=True
            self.yt=Playlist(self.url)
        self.filename="pouet"
    
    def _downloader(self):
        if os.path.exists(self.path)==False:
            os.makedirs(self.path)
            
        if self.playlist==False:
            self.filename=self._getname()
            self.yt.streams.filter(only_audio=True, file_extension = "mp4").first().download(output_path=self.path, filename="temp")
            mp4 = self.path+"/"+"temp.mp4"
            mp3 = self.path+"/"+"temp.mp3"
            ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
            subprocess.run(ffmpeg, stderr=subprocess.DEVNULL)#No display in console
            os.rename(mp3,self.path+"/"+self.filename)
            os.remove(mp4)
            print(self.filename+" ... downloaded")
        else:
            for video in self.yt:
                self.size= self.size + YouTube(video).streams.filter(only_audio=True, file_extension = "mp4").first().filesize
                self.nb_song=self.nb_song+1
            print(str(self.nb_song)+" song detected in the playlist")
        
    def _getname(self):
       filename=(str(self.yt.streams.filter(only_audio=True).first().title)+".mp3")
       filename = re.sub('[^A-Za-z0-9. \-_]+', '', filename)#Remove special caractère
       return filename
   
    def _iter(self):
        if os.path.exists(self.path)==False:
            os.makedirs(self.path)
    
    def _download(self):
        
       
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Tools to download the audio of a Youtube video. You must give the URL & the download path to use it.",
        epilog="Pouet")
    parser.add_argument("path", help="Path of the download folder will contain mp3 file")
    parser.add_argument("url", help="Link of the Youtube video")
    args = parser.parse_args()
    
    tool=YTdownloader()
    tool._downloader()


#  https://www.youtube.com/watch?v=9bZkp7q19f0
# https://www.youtube.com/playlist?list=PLDKnWFJufFAElSOvCm39Z2mgcmr4KXo3j

# yt=YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
# filename=(str(yt.streams.filter(only_audio=True).first().title)+".mp3")
# filename = str(filename.encode('latin-1', "replace")).replace("'","").replace("?","")
# path="D:/Téléchargements" 
# mp3 = "temp.mp3"
# os.rename(path+"/"+mp3,path+"/"+filename)
# test=filename.encode('latin-1')
    
# yt=Playlist("https://www.youtube.com/playlist?list=PLDKnWFJufFAElSOvCm39Z2mgcmr4KXo3j")
# size=0
# nb_song=0
# for video in yt:
#     size=size + YouTube(video).streams.filter(only_audio=True, file_extension = "mp4").first().filesize
#     nb_song=nb_song+1
