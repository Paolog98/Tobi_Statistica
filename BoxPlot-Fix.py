import matplotlib.pyplot as plt
import csv
import numpy as np
import PySimpleGUI as sg
import pandas as pd
import os
import matplotlib.image as mpimg
import json
import datetime
from PIL import Image

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

#!!!!FUNZIONE PER IL CALCOLO DEI tempi delle immagini IN DET INTERVALLO!!!!!
def Fisstask(time1,time2,time3,time4,time5,time6,csv_filef):
    listTime = []
    listTime.append(time1)
    inter = []
    Timeimg = [time1,time2,time3,time4,time5]
    # print(Timeimg)
    num = 5

    for i in range(num):

        if i == num - 1:
            helpTime = time6
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
    numFix1 = []

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
        # print("VALORIIIIIII")
        # print(numF1)
        time2.clear()

    return numF1

def numFissP(dataTime):
    # recupero tempi delle 1 immagini della prima parte TASK1
    delta1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][2])
    delta2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][3])
    delta3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[9][3])
    delta4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[11][3])
    delta5 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[12][3])
    delta6 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][3])


    # SECONDA IMMAGINE TASK 1 SECONDA VOLTA
    delta7 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[63][2])
    delta8= delta_unix_respect_to_video_start(dataTime[0][2], dataTime[63][3])
    delta9 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[66][3])
    delta10 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[68][3])
    delta11 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[69][3])
    delta12 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[70][3])






    # TEMPI TASK 2 PRIMA VOLTA

    delta13 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][2])
    delta14 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][3])
    delta15 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[17][3])
    delta16 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[19][3])
    delta17 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[21][3])
    delta18 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[22][3])

    # SSECONDA VOLTA
    delta19 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[72][2])
    delta20 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[72][3])
    delta21 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[74][3])
    delta22 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[76][3])
    delta23 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[77][3])
    delta24 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[78][3])








    # TEMPI TASK 3 PRIMA VOLTA
    delta25 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[23][2])
    delta26 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[23][3])
    delta27 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[24][3])
    delta28 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[26][3])
    delta29 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[28][3])
    delta30 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[29][3])

    # SECONDA VOLTA TASK3
    delta31 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[80][2])
    delta32 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[80][3])
    delta33 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[82][3])
    delta34 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[84][3])
    delta35 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[86][3])
    delta36 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[87][3])







    # TEMPI TASK 4 PRIMA VOLTA
    delta37 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][2])
    delta38 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][3])
    delta39 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[33][3])
    delta40 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[35][3])
    delta41 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[37][3])
    delta42 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[38][3])

    # SECONDA VOLTA
    delta43 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[90][2])
    delta44 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[90][3])
    delta45 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[92][3])
    delta46 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[94][3])
    delta47 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[96][3])
    delta48 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[97][3])


    #PRIME 4 IMMAGINI TASK 1 prima volta
    Img1=Fisstask(delta1,delta2,delta3,delta4,delta5,delta6,csv_file)

    #task2 prima volta
    Img2=Fisstask(delta13, delta14, delta15, delta16, delta17, delta18, csv_file)

    #task3 prima volta
    Img3=Fisstask(delta25, delta26, delta27, delta28, delta29, delta30, csv_file)

    #task4 primavolta
    Img4=Fisstask(delta37, delta38, delta39, delta40, delta41, delta42, csv_file)



    #SECONDA VOLTA 1 TASK
    Img11=Fisstask(delta7,delta8,delta9,delta10,delta11,delta12,csv_file)

    #SECONDA VOLTA 2 TASK
    Img22=Fisstask(delta19,delta20,delta21,delta22,delta23,delta24,csv_file)

    #SECONDA VOLTA 3 TASK
    Img33=Fisstask(delta31,delta32,delta33,delta34,delta35,delta36,csv_file)


    #SECONDA VOLTA 4 TASK
    Img44=Fisstask(delta43,delta44,delta45,delta46,delta47,delta48,csv_file)
    print("valoreeeeeeeeeee")
    print(Img44)


    FisstaskP=[Img1[1],Img1[2],Img1[3],Img1[4],Img2[1],Img2[2],Img2[3],Img2[4],Img3[1],Img3[2],Img3[3],Img3[4],Img4[1],Img4[2],Img4[3],Img4[4]]
    FisstaskP2 = [Img11[1], Img11[2], Img11[3], Img11[4], Img22[1], Img22[2], Img22[3], Img22[4], Img33[1], Img33[2], Img33[3], Img33[4], Img44[1], Img44[2], Img44[3], Img44[4]]



    return FisstaskP,FisstaskP2

fiss1,fiss2=numFissP(dataTime)








#PRIMO TASK 1 E SECONDA PARTE

# Creazione del box-plot
















#primo task
fix1=[fiss1[0],fiss1[1],fiss1[2],fiss1[3]]
fix2=[fiss2[0],fiss2[1],fiss2[2],fiss2[3]]

#secondo task
fix3=[fiss1[4],fiss1[5],fiss1[6],fiss1[7]]
fix4=[fiss2[4],fiss2[5],fiss2[6],fiss2[7]]

#terzo task
fix5=[fiss1[8],fiss1[9],fiss1[10],fiss1[11]]
fix6=[fiss2[8],fiss2[9],fiss2[10],fiss2[11]]

#quarto task
fix7=[fiss1[12],fiss1[13],fiss1[14],fiss1[15]]
fix8=[fiss2[12],fiss2[13],fiss2[14],fiss2[15]]

fixx1 = []
fixx2 = []
fixx3 = []
fixx4 = []

for element in fix1:

    fixx1.append(int(element))

for element in fix3:

    fixx2.append(int(element))

for element in fix5:

    fixx3.append(int(element))


for element in fix7:

    fixx4.append(int(element))







def durataFissTsk(csv_file,time1,line,fix1):
 fileFix = pd.read_csv(csv_file, sep=',', engine='python', header=None)
 dataFix = fileFix.values.tolist()
 print(dataFix[1][1])
 duration_tsk1=[]
 parameter_to_find = int(time1)

 with open(csv_file, 'r') as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  line_count = 0
  for row in csv_reader:
   line_count += 1
   float_row = [float(value) for value in row]
   print(float_row)
   if (float_row[1]) >= round(parameter_to_find):
    print("TROVATOO")
    print(f"La riga {line_count} contiene il parametro {parameter_to_find}.")
    line=line_count
    print(line)
    break

#recupero le durate delle fissazioni che sono presenti nell'intorno di tempo che appare la foto presa in esame



  for l in range(sum(fix1)):#se non ci sono valori neutri
   duration_tsk1.append(dataFix[line+l][2])
   print(time1)
   print(line)



  print(duration_tsk1)
  return duration_tsk1





deltaTSK1= delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][2])
deltaTSK2=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][2])
deltaTSK3=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[23][2])
deltaTSK4=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][2])

line1=""
line2=""
line3=""
line4=""

dur_task1=durataFissTsk(csv_file,deltaTSK1,line1,fixx1)
dur_task2=durataFissTsk(csv_file,deltaTSK2,line2,fixx2)
dur_task3=durataFissTsk(csv_file,deltaTSK3,line3,fixx3)
dur_task4=durataFissTsk(csv_file,deltaTSK4,line4,fixx4)

durdeftsk1=[]
durdeftsk2=[]
durdeftsk3=[]
durdeftsk4=[]



for element in dur_task1:
    durdeftsk1.append(float(element))


for element in dur_task2:
    durdeftsk2.append(float(element))

for element in dur_task3:
    durdeftsk3.append(float(element))

for element in dur_task4:
    durdeftsk4.append(float(element))





data=[durdeftsk1,durdeftsk2,durdeftsk3,durdeftsk4]
fig, ax = plt.subplots(figsize=(12,8))
bp = ax.boxplot(data,labels=["Task1","Task2","Task3","Task4"])

# Personalizzazione dell'asse y

plt.suptitle("Vengono indicate le fissazioni nella durata di ogni singolo task")
plt.ylabel("Tempo(sec)")
plt.xlabel("Task visionato")
plt.title('Boxplot per ogni singolo task')
plt.legend(loc="best")


# Mostra il grafico
fig.savefig('grafic/boxplotsk.png')
plt.show()







