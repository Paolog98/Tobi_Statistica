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








csv_file= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA FILE FIX.CSV del paziente")
pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT del paziente")
fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
dataTime = fileTime.values.tolist()

def Fisstask(time1,time2,csv_filef):
    listTime = []
    listTime.append(time1)
    inter = []
    Timeimg = [time1,time2]
    print(Timeimg)
    num = 2

    for i in range(num):

        if i == num - 1:
            helpTime = time2
        else:
            helpTime = Timeimg[i]
        numTime = (str(listTime[i]) + '-' + str(helpTime))
        listTime.append(helpTime)
        inter.append(numTime)

    # dati del grafico fixation
    csv_filee = csv_filef
    dataFrame = pd.read_csv(csv_filee)
    data = dataFrame.iloc[:, [0, 1, 3, 4]].values  # Prendo i valori che mi serviranno
    times = [element for element in data[:, 1]]
    time2 = []
    smin = 0
    numF1 = []

    # calco numFix delle foto
    for i in range(1, len(listTime)):
        for x in times:
            if x <= listTime[i]:
                 time2.append(x)
                 numFix1 = [int(element) for element in data[smin:len(time2), 1]]
        diff = len(time2) - smin
        smin = smin + diff
        numF1.append(len(numFix1))
        numFix1.clear()
        print("VALORIIIIIII")
        print(numF1)
        time2.clear()


    return numF1

def numFissP(dataTime):
    # TEMPI TASK 1 PRIMA VOLTA
    delta_sec_7_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][2])
    delta_sec_13_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][3])
    print(delta_sec_7_1, delta_sec_13_2)

    # SECONDA VOLTA
    delta_sec1_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[63][2])
    delta_sec1_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[70][3])
    print(delta_sec1_1, delta_sec1_2)

    # TEMPI TASK 2 PRIMA VOLTA

    delta_sec_15_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][2])
    delta_sec_21_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[21][3])

    # task 2 SSECONDA VOLTA
    delta_sec2_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[72][2])
    delta_sec2_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[78][3])
    print(delta_sec2_1, delta_sec2_2)

    # TEMPI TASK 3 PRIMA VOLTA
    delta_sec_23_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[23][2])
    delta_sec_29_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[29][3])

    # SECONDA VOLTA TASK3
    delta_sec3_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[80][2])
    delta_sec3_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[84][3])

    # TEMPI TASK 4 PRIMA VOLTA
    delta_sec_31_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][2])
    delta_sec_38_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[37][3])

    # SECONDA VOLTA
    delta_sec4_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[90][2])
    delta_sec4_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[96][3])

    numFiss1_1=Fisstask(delta_sec_7_1,delta_sec_13_2,csv_file)
    numFiss1_2=Fisstask(delta_sec1_1,delta_sec1_2,csv_file)

        #CALCO FISS TASK 2  1 E 2 SECONDA VOLTA
    numFiss2_1=Fisstask(delta_sec_15_1,delta_sec_21_2,csv_file)
    numFiss2_2=Fisstask(delta_sec2_1,delta_sec2_2,csv_file)



        #CALCO FISS TASK 3  1 E 2 SECONDA VOLTA
    numFiss3_1=Fisstask(delta_sec_23_1,delta_sec_29_2,csv_file)
    numFiss3_2=Fisstask(delta_sec3_1,delta_sec3_2,csv_file)



        #CALCO FISS TASK 3  1 E 2 SECONDA VOLTA
    numFiss4_1=Fisstask(delta_sec_31_1,delta_sec_38_2,csv_file)
    numFiss4_2=Fisstask(delta_sec4_1,delta_sec4_2,csv_file)

    FisstaskP=[numFiss1_1[1],numFiss2_1[1],numFiss3_1[1],numFiss4_1[1]]
    FisstaskP2=[numFiss1_2[1],numFiss2_2[1],numFiss3_2[1],numFiss4_2[1]]



    return FisstaskP,FisstaskP2


fiss1,fiss2=numFissP(dataTime)



# Creazione del box-plot
fig, ax = plt.subplots()
ax.boxplot(fiss1)

# Personalizzazione dell'asse y
ax.set_ylabel('Durata delle fissazioni task prima parte')

# Mostra il grafico
fig.savefig('grafic/boxplot1.png')
plt.show()



fig, ax = plt.subplots()
ax.boxplot(fiss2)


# Personalizzazione dell'asse y
ax.set_ylabel('Durata delle fissazioni task seconda parte')
fig.savefig('grafic/boxplot2.png')
# Mostra il grafico
plt.show()