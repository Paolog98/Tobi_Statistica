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

n=int(sg.popup_get_text("Quanti pazienti vuoi analizzare(grafico immagini)?"))



ImgTask1 = []
ImgTask2 = []
ImgTask4 = []
ImgTask3= []




TimeT1=[]

TimeT2=[]

TimeT3=[]


TimeT4=[]



Taskp1=[]
Taskp11=[]
Taskp2=[]
Taskp22=[]
Taskp3=[]
Taskp33=[]
Taskp4=[]
Taskp44=[]

dura1_1=[]
dura1_2=[]
dura2_1=[]
dura2_2=[]
dura3_1=[]
dura3_2=[]
dura4_1=[]
dura4_2=[]

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
















def RecupImg(dataTime):
 for numr,i in enumerate(dataTime):
     if i[0] == "['Image'" and i[1].startswith(" 'T1"):
        ImgTask1.append(i[1])
        TimeT1.append(numr)
        print(TimeT1)


     if i[0] == "['Image'" and i[1].startswith(" 'T2"):
        ImgTask2.append(i[1])
        TimeT2.append(numr)




     if i[0] == "['Image'" and i[1].startswith(" 'T3"):
        ImgTask3.append(i[1])
        TimeT3.append(numr)
        print(TimeT3)




     if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4"):
        ImgTask4.append(i[1])
        TimeT4.append(numr)




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



#TEMPI T3
 delta17 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[0]][2])
 delta18 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[1]][2])
 delta19 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[2]][2])
 delta20 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[3]][2])


 delta21 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[4]][2])
 delta22= delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[5]][2])
 delta23 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[6]][2])
 delta24 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[TimeT3[7]][2])



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





 Img3=Fisstask(delta17,delta17,delta18,delta19,delta20,delta20, csv_file)


    #task4 primavolta
 Img4=Fisstask(delta31, delta31, delta32, delta33, delta34, delta34, csv_file)







    #SECONDA VOLTA 1 TASK
 Img11=Fisstask(delta5,delta5,delta6,delta7,delta8,delta8,csv_file)



    #SECONDA VOLTA 2 TASK
 Img22=Fisstask(delta13,delta13,delta14,delta15,delta16,delta16,csv_file)


 #TASK 3 SECONDA VOLTA
 Img33=Fisstask(delta21,delta21,delta22,delta23,delta24,delta24,csv_file)





    #SECONDA VOLTA 4 TASK
 Img44=Fisstask(delta35,delta35,delta36,delta37,delta38,delta38,csv_file)

 Img1.remove(Img1[0])
 Img2.remove(Img2[0])
 Img3.remove(Img3[0])
 Img4.remove(Img4[0])

 Img11.remove(Img11[0])
 Img22.remove(Img22[0])
 Img33.remove(Img33[0])
 Img44.remove(Img44[0])



 dur1_1=durataFissTsk(csv_file,delta1,TimeT1[0],Img1)
 dur1_2 = durataFissTsk(csv_file, delta5, TimeT1[4],Img11)

 dur2_1=durataFissTsk(csv_file,delta9,TimeT2[0],Img2)
 dur2_2 = durataFissTsk(csv_file, delta13, TimeT2[4],Img22)

 dur3_1=durataFissTsk(csv_file,delta17,TimeT3[0],Img3)
 dur3_2 = durataFissTsk(csv_file, delta21, TimeT3[4],Img33)

 dur4_1=durataFissTsk(csv_file,delta31,TimeT4[0],Img4)
 dur4_2=durataFissTsk(csv_file, delta35, TimeT4[4],Img44)






 return  Img1,Img11,Img2,Img22,Img3,Img33,Img4,Img44,dur1_1,dur1_2,dur2_1,dur2_2,dur3_1,dur3_2,dur4_1,dur4_2






def PiuPazienti(Listfix,n):
    for i in range(len(Listfix)):
        if n==0:
           Listfix[i]=Listfix[i]
        if n>0:
           Listfix[i]=Listfix[i]+Listfix[i]

    return Listfix

def PiuPazientiDur(Listfix1,n):
    for i in range(len(Listfix1)):
     Listfix1[i]=float(Listfix1[i])
     if n==0:
        Listfix1[i]=Listfix1[i]
     if n>0:
        Listfix1[i]=Listfix1[i]+Listfix1[i]

    return Listfix1






for i in range(n):
        sg.popup("Inserire i file del paziente n:", i + 1)
        pathTime = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA TEMPI.TXT del paziente")
        fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
        dataTime = fileTime.values.tolist()
        # print(dataTime)
        csv_file = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FILE FIX.CSV del paziente")
        Taskp1,Taskp11,Taskp2,Taskp22,Taskp3,Taskp33,Taskp4,Taskp44,dura1_1,dura1_2,dura2_1,dura2_2,dura3_1,dura3_2,dura4_1,dura4_2 = RecupImg(dataTime)

        #new
        Taskp1=PiuPazienti(Taskp1,n)
        Taskp2 = PiuPazienti(Taskp2, n)
        Taskp3= PiuPazienti(Taskp3, n)
        Taskp4 = PiuPazienti(Taskp4, n)
        Taskp11 = PiuPazienti(Taskp11, n)
        Taskp22 = PiuPazienti(Taskp22, n)
        Taskp33 = PiuPazienti(Taskp33, n)
        Taskp44 = PiuPazienti(Taskp44, n)

        dura1_1 = PiuPazientiDur(dura1_1, n)
        dura1_2= PiuPazientiDur(dura1_2, n)
        dura2_1 = PiuPazientiDur(dura2_1, n)
        dura2_2 = PiuPazientiDur(dura2_2, n)
        dura3_1 = PiuPazientiDur(dura3_1, n)
        dura3_2 = PiuPazientiDur(dura3_2, n)
        dura4_1 = PiuPazientiDur(dura4_1, n)
        dura4_2 = PiuPazientiDur(dura4_2, n)










print(dura1_1,dura2_1,dura3_1,dura4_1,dura1_2,dura2_2,dura3_2,dura4_2)






data=[dura1_1,dura2_1,dura3_1,dura4_1,dura1_2,dura2_2,dura3_2,dura4_2]
fig, ax = plt.subplots(figsize=(12,8))
bp = ax.boxplot(data,labels=["Task1","Task2","Task3","Task4","Task1_2","Task2_2","Task3_2","Task4_2"])

# Personalizzazione dell'asse y

plt.suptitle("Vengono indicate le fissazioni nella durata di ogni singolo task")
plt.title("Rappresentazione visuale della durata delle fissazioni raggrupare per task(nella prima e seconda visione)",fontsize=9)
plt.ylabel("Tempo(ms)")
plt.xlabel("Task visionato")
plt.title('Boxplot per ogni singolo task')
plt.legend(loc="best")


# Mostra il grafico
fig.savefig('grafic/boxplotsk.png')
plt.show()







