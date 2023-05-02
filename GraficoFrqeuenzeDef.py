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
from scipy import stats
from scipy.stats import norm

def convert_unix_to_seconds(unix_timestamp):
 return datetime.datetime.fromtimestamp(unix_timestamp)



def delta_unix_respect_to_video_start(video_start_unix, actual_unix):
 d1 = convert_unix_to_seconds(video_start_unix)
 d2 = convert_unix_to_seconds(actual_unix)
 delta_seconds = round((d2-d1).total_seconds(), 0)
 return delta_seconds

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
    numFix1=[]

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




n=int(sg.popup_get_text("Quanti pazienti vuoi analizzare(grafico immagini)?"))



ImgTask1 = []
ImgTask2 = []
ImgTask4 = []
ImgTask3_01 = []


ImgTask3_02 = []


ImgTask3_03 = []


ImgTask3_04 = []


ImgTask3_05 = []


ImgTask3_06 = []

ImgTask3_07 = []

TimeT1=[]

TimeT2=[]

TimeT3_01=[]
TimeT3_02=[]
TimeT3_03=[]
TimeT3_04=[]
TimeT3_05=[]
TimeT3_06=[]
TimeT3_07=[]

TimeT4=[]



Taskp1=[]
Taskp2=[]
Taskp3_01=[]
Taskp3_02=[]
Taskp3_03=[]
Taskp3_04=[]
Taskp3_05=[]
Taskp3_06=[]
Taskp3_07=[]
Taskp4=[]




def RecupImg(dataTime):
 for numr,i in enumerate(dataTime):
     if i[0] == "['Image'" and i[1].startswith(" 'T1"):
        ImgTask1.append(i[1])
        TimeT1.append(numr)
        print(TimeT1)


     if i[0] == "['Image'" and i[1].startswith(" 'T2"):
        ImgTask2.append(i[1])
        TimeT2.append(numr)




     if i[0] == "['Image'" and i[1].startswith(" 'T3_01"):
        ImgTask3_01.append(i[1])
        TimeT3_01.append(numr)
        print(TimeT3_01)





     if i[0] == "['Image'" and i[1].startswith(" 'T3_02"):
        ImgTask3_02.append(i[1])
        TimeT3_02.append(numr)



     if i[0] == "['Image'" and i[1].startswith(" 'T3_03"):
        ImgTask3_03.append(i[1])
        TimeT3_03.append(numr)



     if i[0] == "['Image'" and i[1].startswith(" 'T3_04"):
        ImgTask3_04.append(i[1])
        TimeT3_04.append(numr)



     if i[0] == "['Image'" and i[1].startswith(" 'T3_05"):
        ImgTask3_05.append(i[1])
        TimeT3_05.append(numr)



     if i[0] == "['Image'" and i[1].startswith(" 'T3_06"):
        ImgTask3_06.append(i[1])
        TimeT3_06.append(numr)



     if i[0] == "['Image'" and i[1].startswith(" 'T3_07"):
        ImgTask3_07.append(i[1])
        TimeT3_07.append(numr)



     if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4"):
        ImgTask4.append(i[1])
        TimeT4.append(numr)


 print(ImgTask1,ImgTask2,ImgTask4,ImgTask3_01, ImgTask3_02, ImgTask3_03, ImgTask3_04, ImgTask3_05, ImgTask3_06, ImgTask3_07)

 #TEMPI FOTO T1
 delta1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[0]][2])
 delta2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[1]][2])
 delta3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[2]][2])
 delta4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[3]][2])

 #seconda parte
 delta5 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[4]][2])
 delta6 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[5]][2])
 delta7 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[6]][2])
 delta8 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT1[7]][2])



 #TEMPI FOTO 2
 delta9 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[0]][2])
 delta10 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[1]][2])
 delta11 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[2]][2])
 delta12 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[3]][2])


 delta13 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[4]][2])
 delta14 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[5]][2])
 delta15 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[6]][2])
 delta16 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT2[7]][2])



  #TEMPI T3-01
 if(len(TimeT3_01)!=0):
  delta117 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_01[0]-1][2])
  delta17 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_01[0]][2])

  delta118 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_01[1]-1][2])
  delta18 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_01[1]][2])


 # TEMPI T3-02
 if (len(TimeT3_02) != 0):
  delta119 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_02[0]-1][2])
  delta19 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_02[0]][2])

  delta220 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_02[1]-1][2])
  delta20 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_02[1]][2])

 #TEMPI T3-03
 if (len(TimeT3_03) != 0):
  delta221 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_03[0]-1][2])
  delta21 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_03[0]][2])

  delta222 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_03[1]-1][2])
  delta22 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_03[1]][2])



 # TEMPI T3-04
 if (len(TimeT3_04) != 0):
  delta223 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_04[0]-1][2])
  delta23 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_04[0]][2])

  delta224 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_04[1]-1][2])
  delta24 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_04[1]][2])


 # TEMPI T3-05
 if (len(TimeT3_05) != 0):
  delta225 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_05[0]-1][2])
  delta25 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_05[0]][2])

  delta226 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_05[1]-1][2])
  delta26 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_05[1]][2])

 # TEMPI T3-06
 if (len(TimeT3_06) != 0):
  delta227 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_06[0]-1][2])
  delta27 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_06[0]][2])

  delta228 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_06[1]-1][2])
  delta28 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_06[1]][2])


 # TEMPI T3-07
 if (len(TimeT3_07) != 0):
  delta229 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_07[0]-1][2])
  delta29 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_07[0]][2])

  delta330 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_07[1]-1][2])
  delta30 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3_07[1]][2])


 #TEMPI T4
 delta31 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[0]][2])
 delta32 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[1]][2])
 delta33 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[2]][2])
 delta34 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[3]][2])


 delta35 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[4]][2])
 delta36 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[5]][2])
 delta37 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[6]][2])
 delta38 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT4[7]][2])






  #RECUPERIMAO LE FISSAZIONI DI OGNI FOTO




  #TASK 1 PRIMA VOLTA
 Img1=Fisstask(delta1,delta1,delta2,delta3,delta4,delta4,csv_file)


    #task2 prima volta
 Img2=Fisstask(delta9,delta9,delta10,delta11,delta12,delta12, csv_file)

 Img3_01=[]
 Img3_011=[]
 Img3_02=[]
 Img3_022=[]
 Img3_03 =[]
 Img3_033=[]
 Img3_04 =[]
 Img3_044=[]
 Img3_05 =[]
 Img3_055=[]
 Img3_06 =[]
 Img3_066=[]
 Img3_07 =[]
 Img3_077=[]

    #task30-1 prima volta
 if (len(TimeT3_01) != 0):
  Img3_01=  Fisstask(delta117,delta117,delta117,delta17,delta17,delta17, csv_file)
 if (len(TimeT3_02) != 0):
  Img3_02 = Fisstask(delta119, delta119, delta119, delta19,delta19,delta19,csv_file)
 if (len(TimeT3_03) != 0):
  Img3_03 = Fisstask(delta221, delta221, delta221, delta21,delta21,delta21, csv_file)
 if (len(TimeT3_04) != 0):
  Img3_04 = Fisstask(delta223, delta223, delta223, delta23,delta23,delta23, csv_file)
 if (len(TimeT3_05) != 0):
  Img3_05 = Fisstask(delta225, delta225, delta225, delta25,delta25,delta25, csv_file)
 if (len(TimeT3_06) != 0):
  Img3_06 = Fisstask(delta227, delta227, delta227, delta27,delta27,delta27, csv_file)
 if (len(TimeT3_07) != 0):
  Img3_07 = Fisstask(delta229, delta229, delta229, delta29,delta29,delta29, csv_file)

    #task4 primavolta
 Img4=Fisstask(delta31, delta31, delta32, delta33, delta34, delta34, csv_file)







    #SECONDA VOLTA 1 TASK
 Img11=Fisstask(delta5,delta5,delta6,delta7,delta8,delta8,csv_file)



    #SECONDA VOLTA 2 TASK
 Img22=Fisstask(delta13,delta13,delta14,delta15,delta16,delta16,csv_file)


 #TASK 3 SECONDA VOLTA
 if (len(TimeT3_01) != 0):
  Img3_011=Fisstask(delta118,delta118,delta118,delta18,delta18,delta18, csv_file)
 if (len(TimeT3_02) != 0):
  Img3_022 = Fisstask(delta220, delta220, delta220,  delta20,delta20, delta20, csv_file)
 if (len(TimeT3_03) != 0):
  Img3_033 = Fisstask(delta222, delta222, delta222,  delta22,delta22, delta22, csv_file)
 if (len(TimeT3_04) != 0):
  Img3_044 = Fisstask(delta224, delta224, delta224,  delta24, delta24, delta24, csv_file)
 if (len(TimeT3_05) != 0):
  Img3_055 = Fisstask(delta226, delta226, delta226,  delta26,delta26, delta26,csv_file)
 if (len(TimeT3_06) != 0):
  Img3_066 = Fisstask(delta228, delta228, delta228,  delta28,delta28, delta28, csv_file)
 if (len(TimeT3_07) != 0):
  Img3_077 = Fisstask(delta330, delta330, delta330,  delta30, delta30, delta30, csv_file)




    #SECONDA VOLTA 4 TASK
  Img44=Fisstask(delta35,delta35,delta36,delta37,delta38,delta38,csv_file)


  Task1=Img1+Img11
  Task2=Img2+Img22
  Task3_01=Img3_01+Img3_011
  Task3_02 = Img3_02 + Img3_022
  Task3_03 = Img3_03 + Img3_033
  Task3_04 = Img3_04 + Img3_044
  Task3_05 = Img3_05 + Img3_055
  Task3_06 = Img3_06 + Img3_066
  Task3_07 = Img3_07 + Img3_077
  Task4=Img4+Img44
  print(Task1,Task2,Task3_01,Task3_02 ,Task3_03 ,Task3_04 ,Task3_05 ,Task3_06 ,Task3_07 ,Task4)




  return  Task1,Task2,Task3_01,Task3_02 ,Task3_03 ,Task3_04 ,Task3_05 ,Task3_06 ,Task3_07 ,Task4















for i in range(n):
        sg.popup("Inserire i file del paziente n:", i + 1)
        pathTime = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA TEMPI.TXT del paziente")
        fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
        dataTime = fileTime.values.tolist()
        # print(dataTime)
        csv_file = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FILE FIX.CSV del paziente")
        Taskp1, Taskp2, Taskp3_01, Taskp3_02, Taskp3_03, Taskp3_04, Taskp3_05, Taskp3_06, Taskp3_07, Taskp4 = RecupImg(dataTime)
        ImgTask11,ImgTask22,ImgTask44,ImgTask33_01, ImgTask33_02, ImgTask33_03, ImgTask33_04, ImgTask33_05, ImgTask33_06, ImgTask33_07=RecupImg(dataTime)
        print("TEMPI DELLE FOTO")
        print(ImgTask11,ImgTask22,ImgTask44,ImgTask33_01, ImgTask33_02, ImgTask33_03, ImgTask33_04, ImgTask33_05, ImgTask33_06, ImgTask33_07)
        '''ImgTask1.append(ImgTask11)
        ImgTask2.append(ImgTask22)
        ImgTask4.append(ImgTask44)
        ImgTask3_01.append(ImgTask33_01)
        ImgTask3_02.append(ImgTask33_02)
        ImgTask3_03.append(ImgTask33_03)
        ImgTask3_04.append(ImgTask33_04)
        ImgTask3_05.append(ImgTask33_05)
        ImgTask3_06.append(ImgTask33_06)
        ImgTask33_07.append(ImgTask33_07)'''
        print(ImgTask1, ImgTask2, ImgTask4, ImgTask3_01, ImgTask3_02, ImgTask3_03, ImgTask3_04, ImgTask3_05,
              ImgTask3_06, ImgTask3_07)
'''for j in range(len(sum_array)):
        if i == 0:
            count = i + 1
            sum_f1.append(sum_array[j])
        elif i == 1:
            count = i + 2
            sum_f1.append(sum_array[j] + sum_array[j])
        elif i == 2:
            sum_f1.append(sum_array[j] + sum_array[j] + sum_array[j])
        elif i == 3:
            sum_f1.append(sum_array[j] + sum_array[j] + sum_array[j] + sum_array[j])
        elif i == 4:
            sum_f1.append(sum_array[j] + sum_array[j] + sum_array[j] + sum_array[j] + sum_array[j])

for j in range(len(sum_array2)):
        if i == 0:
            sum_f2.append(sum_array2[j])
        elif i == 1:
            sum_f2.append(sum_array2[j] + sum_array2[j])
        elif i == 2:
            sum_f2.append(sum_array2[j] + sum_array2[j] + sum_array2[j])
        elif i == 3:
            sum_f2.append(sum_array2[j] + sum_array2[j] + sum_array2[j] + sum_array2[j])
        elif i == 4:
            sum_f2.append(sum_array2[j] + sum_array2[j] + sum_array2[j] + sum_array2[j] + sum_array2[j])'''














#CALCO FISS TASK 1    1 E 2 SECONDA VOLTA





# Dettagli del grafico
#Marcatori

colors = ["blue","red","green"]


fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 27, 1))
ax.tick_params(axis='x', which='major', labelsize=5.7, pad=6)
plt.xticks(rotation=20)


#PRIM0 TASK

plt.bar(ImgTask1[0], Taskp1[1], width=0.3,color=colors[0],label="Prima visione della foto")
plt.bar(0.3, Taskp1[6], width=0.3,color=colors[1],label="Seconda visione della foto")

plt.bar(ImgTask1[1], Taskp1[2], width=0.3,color=colors[0])
plt.bar(1.3, Taskp1[7], width=0.3,color=colors[1])

plt.bar(ImgTask1[2], Taskp1[3], width=0.3,color=colors[0])
plt.bar(2.3, Taskp1[8], width=0.3,color=colors[1])

plt.bar(ImgTask1[3], Taskp1[4], width=0.3,color=colors[0])
plt.bar(3.3, Taskp1[9], width=0.3,color=colors[1])



plt.bar(ImgTask2[0], Taskp2[1], width=0.3,color=colors[0])
plt.bar(4.3, Taskp2[6], width=0.3,color=colors[1])

plt.bar(ImgTask2[1], Taskp2[2], width=0.3,color=colors[0])
plt.bar(5.3, Taskp2[7], width=0.3,color=colors[1])


plt.bar(ImgTask2[2], Taskp2[3], width=0.3,color=colors[0])
plt.bar(6.3, Taskp2[8], width=0.3,color=colors[1])


plt.bar(ImgTask2[3], Taskp2[4], width=0.3,color=colors[0])
plt.bar(7.3, Taskp2[9], width=0.3,color=colors[1])







plt.bar(ImgTask4[0], Taskp4[1], width=0.3,color=colors[0])
plt.bar(8.3, Taskp4[6],width=0.3,color=colors[1])

plt.bar(ImgTask4[1], Taskp4[2], width=0.3,color=colors[0])
plt.bar(9.3, Taskp4[7], width=0.3,color=colors[1])

plt.bar(ImgTask4[2], Taskp4[3], width=0.3,color=colors[0])
plt.bar(10.3, Taskp4[8], width=0.3,color=colors[1])

plt.bar(ImgTask4[3], Taskp4[4], width=0.3,color=colors[0])
plt.bar(11.3, Taskp4[9], width=0.3,color=colors[1])


plt.axvline(x=11.5, color='red', linestyle='--', label="TASK 3->(ogni foto presenta il num. di quante volte è stata vista)")

if (len(ImgTask3_01) != 0):
     count1=len(ImgTask3_01)
     plt.bar(ImgTask3_01[0]+str(count1),Taskp3_01[3] , width=0.3,color=colors[0])
     plt.bar(ImgTask3_01[0], Taskp3_01[8], width=0.3,color=colors[1])

if (len(ImgTask3_02) != 0):
     count2=len(ImgTask3_02)
     plt.bar(ImgTask3_02[0]+str(count2), Taskp3_02[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_02[0], Taskp3_02[8], width=0.3,color=colors[1])

if (len(ImgTask3_03) != 0):
     count3=len(ImgTask3_03)
     plt.bar(ImgTask3_03[0]+str(count3), Taskp3_03[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_03[0], Taskp3_03[8], width=0.3,color=colors[1])

if (len(ImgTask3_04) != 0):
     count4=len(ImgTask3_04)
     plt.bar(ImgTask3_04[0]+str(count4), Taskp3_04[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_04[0], Taskp3_04[8], width=0.3,color=colors[1])

if (len(ImgTask3_05) != 0):
     count5=len(ImgTask3_05)
     plt.bar(ImgTask3_05[0]+str(count5),Taskp3_05[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_05[0], Taskp3_05[8], width=0.3,color=colors[1])

if (len(ImgTask3_06) != 0):
     count6=len(ImgTask3_06)
     plt.bar(ImgTask3_06[0]+str(count6), Taskp3_06[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_06[0], Taskp3_06[8], width=0.3,color=colors[1])

if (len(ImgTask3_07) !=0):
     count7=len(ImgTask3_07)
     plt.bar(ImgTask3_07[0]+str(count7), Taskp3_07[3], width=0.3,color=colors[0])
     plt.bar(ImgTask3_07[0], Taskp3_07[8], width=0.3,color=colors[1])


''''
# shapiro_Wilk sulla durata delle fissazioni per ciasun soggetto per ciasun immagine
data1 = sum_f1
print(sum_f1)
data2 = sum_f2
data_merge=np.concatenate((data1,data2))

# Calcoliamo il p-value del test di Shapiro-Wilk
stat, p = stats.shapiro(data_merge)


# Stampa il p-value
print("shapiro_Wilk sulla durata delle fissazioni per ciasun soggetto per ciasun immagine")
print("p-value:", p)

# Valuta l'ipotesi nulla
alpha = 0.05
if p > alpha:
    print("Non possiamo rifiutare l'ipotesi nulla: i dati seguono una distribuzione normale")

else:
    print("Rifiutiamo l'ipotesi nulla: i dati non seguono una distribuzione normale")'''







# Annotazioni per ogni barra che restituisce il numero di fissazioni
'''for i in range(len(sum_f1)):
    plt.annotate(sum_f1[i], (-0.19 + i, sum_f1[i]))
for j in range(len(sum_f2)):
    plt.annotate(sum_f2[j], ( j+0.2, sum_f2[j]))'''

'''ytemp=max(sum_f1)
ytemp2=max(sum_f2)
ytempf=[ytemp,ytemp2]'''

#plt.ylim([0, max(ytempf)+20])
plt.ylabel('Numero di fissazioni')
plt.xlabel('Immagine')
plt.title('Grafico delle Frequenze assolute relativo a una singola immagine',fontweight='bold', fontsize=16)
plt.legend(loc="best")
# print(count)
count=0
if count==1:
 name=str(os.path.dirname(pathTime))
 fig.savefig(name+"SingoloPazienteImg"+".png")
elif count>2:
    name = str(os.path.dirname(pathTime))
    fig.savefig(name +"PiùPazientiImg" + ".png")

plt.show()



'''
#SECONDO GRAFICO VAL MAX MIN AVG
#dati grafico linee multiple max,medio,min
#Prima Parte
valmax1=max(sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3])
valmax2=max(sum_f1[4],sum_f1[5],sum_f1[6],sum_f1[7])
valmax3=max(sum_f1[8],sum_f1[9],sum_f1[10],sum_f1[11])
valmax4=max(sum_f1[12],sum_f1[13],sum_f1[14],sum_f1[15])
#Seconda Parte
valmax1_2=max(sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[3])
valmax2_2=max(sum_f2[4],sum_f2[5],sum_f2[6],sum_f2[7])
valmax3_2=max(sum_f2[8],sum_f2[9],sum_f2[10],sum_f2[11])
valmax4_2=max(sum_f2[12],sum_f2[13],sum_f2[14],sum_f2[15])


#array prima e seconda parte
array1=[sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3]]
array2=[sum_f1[4],sum_f1[5],sum_f1[6],sum_f1[7]]
array3=[sum_f1[8],sum_f1[9],sum_f1[10],sum_f1[11]]
array4=[sum_f1[12],sum_f1[13],sum_f1[14],sum_f1[15]]

array1_2=[sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[3]]
array2_2=[sum_f2[4],sum_f2[5],sum_f2[6],sum_f2[7]]
array3_2=[sum_f2[8],sum_f2[9],sum_f2[10],sum_f2[11]]
array4_2=[sum_f2[12],sum_f2[13],sum_f2[14],sum_f2[15]]



#media prima parte
valavg1=sum(array1)/4
valavg2=sum(array2)/4
valavg3=sum(array3)/4
valavg4=sum(array4)/4

#media seconda parte
valavg1_2=sum(array1_2)/4
valavg2_2=sum(array2_2)/4
valavg3_2=sum(array3_2)/4
valavg4_2=sum(array4_2)/4




#valore minimo prima parte
valmin1=min(sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3])
valmin2=min(sum_f1[4],sum_f1[5],sum_f1[6],sum_f1[7])
valmin3=min(sum_f1[8],sum_f1[9],sum_f1[10],sum_f1[11])
valmin4=min(sum_f1[12],sum_f1[13],sum_f1[14],sum_f1[15])


#valore minimo seconda parte
valmin1_2=min(sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[3])
valmin2_2=min(sum_f2[4],sum_f2[5],sum_f2[6],sum_f2[7])
valmin3_2=min(sum_f2[8],sum_f2[9],sum_f2[10],sum_f2[11])
valmin4_2=min(sum_f2[12],sum_f2[13],sum_f2[14],sum_f2[15])


# print(valmax1,valmax2,valavg1,valavg2,valmin1,valmin2)
valarray=[valmax1,valmax2,valavg2,valmin1,valmin2]

fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12, 8))

# Dati per il grafico
x = [26,60,90,133,206,236,266,319]  # Valori sull'asse x
y1 = [valmax1,valmax2,valmax3,valmax4,valmax1_2,valmax2_2,valmax3_2,valmax4_2]  # Valori max
y2 = [valmin1,valmin2,valmin3,valmin4,valmin1_2,valmin2_2,valmin3_2,valmin4_2]  # Valori min
y3 = [valavg1,valavg2,valavg3,valavg4,valavg1_2,valavg2_2,valavg3_2,valavg4_2]  # Valori avg

# Creazione del grafico
plt.plot(x, y2,'-o', label='Valore min')
plt.plot(x, y3,'-o', label='Valore avg')
plt.plot(x, y1,'-o',label='Valore max')

# Aggiunta di etichette e titolo
plt.xlabel('Tempo(sec)')
plt.ylabel('Valori fissazioni')
plt.title('Grafico a linee multiple(26-133sec/206-319sec)')
plt.legend(loc="best")

# Aggiunta di una legenda
plt.legend()
name=str(os.path.dirname(pathTime))
if count==1:
 name=str(os.path.dirname(pathTime))
 fig.savefig(name+"SingoloPazienteMAX"+".png")
elif count>2:
    name = str(os.path.dirname(pathTime))
    fig.savefig(name +"PiùPazientiMAX" + ".png")

# Mostra il grafico
plt.show()





plt.plot(val[1], valmin1, width=0.3,color=colori[0])
plt.plot(1.3, valmin2, width=0.3,color=colori[1])

plt.plot(val[2], valavg1, width=0.3,color=colori[0])
plt.plot(2.3, valavg2, width=0.3,color=colori[1])'''

'''
ytemp2=[valmax1,valmax2]
plt.ylim([0,max(ytemp2)+15])
plt.title('Grafico a linee multiple(max,avg,min)',fontweight='bold', fontsize=15)
plt.legend(loc="best")
fig.savefig('grafic/graficMediaMinMax.png')
plt.show()'''

# generiamo dei dati casuali da una distribuzione normale
'''
#  Q-Q plot per ciasun immagine del paziente
merge_array=np.concatenate((data1,data2))

# Normalizziamo i dati
sorted_data = np.sort(merge_array)
n = sorted_data.size
norm_data = norm.ppf((np.arange(1, n+1) - 0.5)/n)

# Creiamo il grafico Q-Q plot
plt.scatter(norm_data, sorted_data)
plt.title('Q-Q plot')
plt.xlabel('Quantili teorici')
plt.ylabel('Quantili empirici')

mu = np.mean(merge_array)
sigma = np.std(merge_array)
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
y = mu + sigma*x
plt.plot(x, y, color='red')


plt.show()'''

