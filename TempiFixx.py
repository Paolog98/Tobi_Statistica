import gzip

import matplotlib.pyplot as plt
import csv
import numpy as np
import PySimpleGUI as sg
import pandas as pd
import os
import matplotlib.image as mpimg
import json
import datetime



def convert_unix_to_seconds(unix_timestamp):
 return datetime.datetime.fromtimestamp(unix_timestamp)


def delta_unix_respect_to_video_start(video_start_unix, actual_unix):
 d1 = convert_unix_to_seconds(video_start_unix)
 d2 = convert_unix_to_seconds(actual_unix)
 delta_seconds = round((d2 - d1).total_seconds(), 0)
 return delta_seconds

pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT")
fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
dataTime = fileTime.values.tolist()


ImgTask1=[dataTime[7][1],dataTime[9][1],dataTime[11][1],dataTime[13][1]]
ImgTask2=[dataTime[15][1],dataTime[17][1],dataTime[19][1],dataTime[21][1]]
ImgTas3=[dataTime[23][1],dataTime[25][1],dataTime[27][1],dataTime[29][1]]
ImgTas4=[dataTime[31][1],dataTime[33][1],dataTime[35][1],dataTime[37][1]]

ImgTask1_2=[dataTime[63][1],dataTime[66][1],dataTime[68][1],dataTime[70][1]]
ImgTask2_2=[dataTime[72][1],dataTime[74][1],dataTime[76][1],dataTime[78][1]]
ImgTask3_2=[dataTime[80][1],dataTime[82][1],dataTime[82][1],dataTime[84][1]]
ImgTask4_2=[dataTime[90][1],dataTime[92][1],dataTime[94][1],dataTime[96][1]]



print(ImgTask1)
print(ImgTask1_2)

print("...")

print(ImgTask2)
print(ImgTask2_2)

print("...")

print(ImgTas3)
print(ImgTask3_2)

print("...")
print(ImgTas4)
print(ImgTask4_2)


delta_sec_7_1=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][2])
delta_sec_7_2=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][3])
delta_sec_9_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[9][2])
delta_sec_9_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[9][3])
delta_sec_11_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[11][2])
delta_sec_11_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[11][3])
delta_sec_13_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][2])
delta_sec_13_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][3])

#SECONDA IMMAGINE
delta_sec_60_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[60][2])
delta_sec_60_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[61][3])
delta_sec_62_3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[63][3])
delta_sec_62_4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[66][3])
delta_sec_63_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[68][3])

