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
print(delta_sec_60_1,delta_sec_60_2,delta_sec_62_3,delta_sec_62_4,delta_sec_63_1)