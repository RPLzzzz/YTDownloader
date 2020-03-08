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
        """
        Constructor
        """
        self.url=args.url
        self.path=args.path
        self.size=0
        self.nb_song=0
        try:
            self.playlist=False
            self.yt=YouTube(self.url)
        except RegexMatchError:
            self.playlist=True
            self.pl=Playlist(self.url)
        self.filename="pouet"
        
    def _getname(self):
        """
        Method to get the name of the video without special characters
        @attributs:
            self.yt     -required : YouTube() object containing the link of the video
        """
        filename=(str(self.yt.title)+".mp3")
        filename = re.sub('[^A-Za-z0-9. \-_]+', '', filename)#Remove special caractère
        if filename=="Youtube.mp3":
            filename=str(self.yt.author)+str(self.yt.views)+".mp3"
        return filename
   
    def _iter(self):
        """
        Method to iterate download
        @attributs:
            self.yt     -required : YouTube() object containing the link of the video
            self.path   -required : Path will contain the song 
        """
        if os.path.exists(self.path)==False:
            os.makedirs(self.path)
        # Just one song
        if self.playlist==False:
            self._download()
            print(self.filename+" ... downloaded")
        # Playlist containing several songs
        else:
            self.nb_song=len(self.pl)
            self._printProgressBar(0, self.nb_song, prefix = 'Loading Playlist:', suffix = 'Completed', length = 50)
            count=0
            for video in self.pl:
                self.size= self.size + YouTube(video).streams.filter(only_audio=True, file_extension = "mp4").first().filesize
                count=count+1
                self._printProgressBar(count, self.nb_song, prefix = 'Loading Playlist:', suffix = 'Completed', length = 50)
            print('\n')
            print(str(self.nb_song)+" song detected in the playlist, it require approximately "+ str(self.size*1e-6)+"Mb")
            print('\n')
            self._printProgressBar(0, self.size, prefix = 'Progress:', suffix = 'Complete', length = 50)
            size_temp=0
            for video in self.pl:
                self.yt=YouTube(video)
                size_temp= size_temp + self.yt.streams.filter(only_audio=True, file_extension = "mp4").first().filesize
                self._download()
                # print(self.filename+" ... downloaded")
                self._printProgressBar(size_temp, self.size, prefix = 'Progress:', suffix = 'Completed', length = 50)
            
    def _download(self):
        """
        Method to download audio from a video link (youtube) in mp3.
        @attributs:
            self.yt     -required : YouTube() object containing the link of the video
            self.path   -required : Path will contain the song 
        """
        self.filename=self._getname()
        self.yt.streams.filter(only_audio=True, file_extension = "mp4").first().download(output_path=self.path, filename="temp")
        mp4 = self.path+"/"+"temp.mp4"
        mp3 = self.path+"/"+"temp.mp3"
        ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
        subprocess.run(ffmpeg, stderr=subprocess.DEVNULL)#No display in console
        filename=self.filename
        if filename=="Youtube.mp3" or filename=="YouTube.mp3" :
            filename=str(self.yt.author)+str(self.yt.views)+".mp3"
        os.rename(mp3,self.path+"/"+filename)
        os.remove(mp4)
        
    def _printProgressBar(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()
       
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Tools to download the audio of a Youtube video. You must give the URL & the download path to use it.",
        epilog="Pouet")
    parser.add_argument("path", help="Path of the download folder will contain mp3 file")
    parser.add_argument("url", help="Link of the Youtube video")
    args = parser.parse_args()
    
    tool=YTdownloader()
    tool._iter()


# https://www.youtube.com/watch?v=9bZkp7q19f0
# https://www.youtube.com/playlist?list=PLDKnWFJufFAElSOvCm39Z2mgcmr4KXo3j

