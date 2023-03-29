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







# dati del grafico fixation
'''csv_file1 = csv_file
dataFrame = pd.read_csv(csv_file)
data = dataFrame.iloc[:, [0, 1, 3, 4]].values               # Prendo i valori che mi serviranno
times = [element for element in data[:, 1]]
time2 = []
smin = 0
numF2 = []'''





#!!!!FUNZIONE PER IL CALCOLO DEI TASK IN DET INTERVALLO!!!!!
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
    delta_sec1_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[61][3])
    delta_sec1_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[69][3])
    print(delta_sec1_1, delta_sec1_2)

    # TEMPI TASK 2 PRIMA VOLTA

    delta_sec_15_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][2])
    delta_sec_21_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[21][3])

    # SSECONDA VOLTA
    delta_sec2_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[69][3])
    delta_sec2_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[75][3])
    print(delta_sec2_1, delta_sec2_2)

    # TEMPI TASK 3 PRIMA VOLTA
    delta_sec_23_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[23][2])
    delta_sec_29_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[29][3])

    # SECONDA VOLTA TASK3
    delta_sec3_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[75][3])
    delta_sec3_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[81][3])

    # TEMPI TASK 4 PRIMA VOLTA
    delta_sec_31_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[32][3])
    delta_sec_38_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[56][3])

    # SECONDA VOLTA
    delta_sec4_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[81][3])
    delta_sec4_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[105][3])

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





n=int(sg.popup_get_text("Quanti pazienti vuoi analizzare?"))






for i in range(n):

    pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT")
    fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
    dataTime = fileTime.values.tolist()
    csv_file= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA FILE FIX.CSV")
    FisstaskP, FisstaskP2 = numFissP(dataTime)
    print("ARRAYYYY")
    print(FisstaskP[i])
    print(FisstaskP2[i])



#CALCO FISS TASK 1    1 E 2 SECONDA VOLTA







# Dettagli del grafico
#Marcatori
Idimg=["tsk1","tsk2","tsk3","tsk4"]
colors = ["green","purple"]



fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12, 8))

#PRIM0 TASK
plt.bar(Idimg[0], FisstaskP[0], width=0.3,color=colors[0],label="Prima visione del task")
plt.bar(0.3, FisstaskP2[0], width=0.3,color=colors[1],label="Seconda visione del task")

#SECONDO TASK

plt.bar(Idimg[1], FisstaskP[1], width=0.3,color=colors[0])
plt.bar(1.3, FisstaskP2[1], width=0.3,color=colors[1])

#TERZO TASK
plt.bar(Idimg[2], FisstaskP[2], width=0.3,color=colors[0])
plt.bar(2.3, FisstaskP2[2], width=0.3,color=colors[1])

#QUARTO TASK
plt.bar(Idimg[3], FisstaskP[3], width=0.3,color=colors[0])
plt.bar(3.3, FisstaskP2[3], width=0.3,color=colors[1])
# Annotazioni per ogni barra che restituisce il numero di fissazioni
for i in range(len(FisstaskP)):
    plt.annotate(FisstaskP[i], (-0.05 + i, FisstaskP[i]))
for j in range(len(FisstaskP2)):
    plt.annotate(FisstaskP2[j], ( j+0.2, FisstaskP2[j]))

ytemp=max(FisstaskP)
ytemp2=max(FisstaskP2)
ytempf=[ytemp,ytemp2]

plt.ylim([0, max(ytempf)+50])
plt.ylabel('Numero di fissazioni')
plt.xlabel('Task eseguito ')
plt.title('Grafico delle Frequenze assolute relativo a un singolo task',fontweight='bold', fontsize=15)
plt.legend(loc="best")
fig.savefig('grafic/graficNumFissazioniTASK.png')
plt.show()
