# YTDownloader

## How to use it ?
Windows user
+ First, you should have install anaconda (https://docs.anaconda.com/anaconda/install/windows/) & update conda with the Anaconda prompt console :
```
conda update conda
```
+ Install Pytube module with Anaconda prompt :
```
pip install pytube3
```
+ You need to install FFmpeg Builds (https://ffmpeg.zeranoe.com/builds/), it is a framework to decode, encode, transcode, mux, demux, stream, filter and play multimedia. To install the buil you have to unzip the file and verify if it has been installed correctly by opening a CMD and type :
```
ffmpeg -h
```
If it doesn't work, just add the path where you installed FFmpeg build to your local environmentr variable path on windows (https://www.computerhope.com/issues/ch000549.htm)