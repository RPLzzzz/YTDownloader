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
+ You need to install FFmpeg Builds (https://ffmpeg.zeranoe.com/builds/), it is a framework to decode, encode, transcode, mux, demux, stream, filter and play multimedia. To install the build you have to unzip the file and verify if it has been installed correctly by opening a CMD and type :
```
ffmpeg -h
```
If it doesn't work, just add the path where you installed FFmpeg build to your local environmentr variable path on windows (https://www.computerhope.com/issues/ch000549.htm)
+ Download the script (Crop.py)
+ Launch anaconda prompt
+ Go to the path of the script :

```
cd username/mypath/...
```
+ Execute the script :

```
python Grabit.py -h
```
Here an exemple : 
![output](https://i.imgur.com/L2AwWIV.png)

## Other infomation ?
+ Created on 08/03/2020
+ Build with python 3.7 on Windows 10

## Authors

* **Loïc ARGENTIER** - *Initial work* - [argent-lo](https://github.com/argent-lo)