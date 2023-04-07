import gzip
import math

import cv2
import matplotlib.pyplot as plt
import csv
import numpy as np
import PySimpleGUI as sg
import pandas as pd
import os
import matplotlib.image as mpimg
import json
import datetime
import tkinter as tk


def convert_unix_to_seconds(unix_timestamp):
 return datetime.datetime.fromtimestamp(unix_timestamp)

def delta_unix_respect_to_video_start(video_start_unix, actual_unix):
 d1 = convert_unix_to_seconds(video_start_unix)
 d2 = convert_unix_to_seconds(actual_unix)
 delta_seconds = round((d2 - d1).total_seconds(), 0)
 return delta_seconds

#!!!!FUNZIONE PER IL CALCOLO DEI tempi delle immagini IN DET INTERVALLO!!!!!
def Fisstask(time1,time2,time3,csv_filef):
    listTime = []
    listTime.append(time1)
    inter = []
    Timeimg = [time1,time2,time3]
    # print(Timeimg)
    num = 2

    for i in range(num):

        if i == num - 1:
            helpTime = time3
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

sum_f1=[]
sum_f2=[]

for i in range(n):
    sg.popup("Inserire i file del paziente n:",i+1)
    pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT del paziente")
    fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
    dataTime = fileTime.values.tolist()
    # print(dataTime)
    csv_file= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA FILE FIX.CSV del paziente")

delta37 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][2])
delta38 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][3])


delta39 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[33][2])
delta40 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[33][3])

delta41 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[34][2])
delta42 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[34][3])

delta43 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[35][2])
delta44 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[35][3])

delta45 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[36][2])
delta46 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[36][3])

root = tk.Tk()  # Libreria tkinter



def calcolofissdxsx(time1, time2, time3,riga, csv_file):


    fix=Fisstask(time1, time2, time3,csv_file)
    dataFrame = pd.read_csv(csv_file)
    data = dataFrame.iloc[:, [0, 1,2,3,4]].values
    posX = [element for element in data[:, 3]]
    posY = [element for element in data[:, 4]]
    displayWidth = root.winfo_screenwidth()
    displayHeight = root.winfo_screenheight()
    print(displayHeight, displayHeight)

    posXPix = []
    posYPix = []
    for x, y in zip(posX, posY):
        posXPix.append(round(x * displayWidth))
        posYPix.append(round(y * displayHeight))

    center=posXPix[riga]-posYPix[riga]
    fix.remove(fix[0])
    print(fix)
    sx_fixations = [i for i  in fix if posX[riga] <= center]
    dx_fixations = [i for i  in fix if posX[riga] > center]

    print("Fissazioni a sinistra:", sx_fixations)
    print("Fissazioni a destra:", dx_fixations)

    return sx_fixations,dx_fixations

#foto 1 sx dx
Img1=calcolofissdxsx(delta37,delta37,delta38,37,csv_file)
sx1=Img1[0]
dx1=Img1[1]
print(sx1,dx1)





'''for j in range(len(sum_array)):
    if i==0:
        count=i+1
        sum_f1.append(sum_array[j])
    elif i==1:
     count=i+2
     sum_f1.append(sum_array[j] + sum_array[j])
    elif i==2:
     sum_f1.append(sum_array[j] + sum_array[j]+sum_array[j])
    elif i == 3:
        sum_f1.append(sum_array[j] + sum_array[j] + sum_array[j]+sum_array[j])
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
        sum_f2.append(sum_array2[j] + sum_array2[j] + sum_array2[j] + sum_array2[j]+sum_array2[j])



#Recupero i nomi delle immagini dei vari task

ImgTask4 = []
for i in dataTime :
  if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4"):
        ImgTask4.append(i[1])


# ImgTask1=[dataTime[7][1],dataTime[9][1],dataTime[11][1],dataTime[13][1]]
# ImgTask2=[dataTime[15][1],dataTime[17][1],dataTime[19][1],dataTime[21][1]]
# ImgTask3=[dataTime[23][1],dataTime[25][1],dataTime[27][1],dataTime[29][1]]
# ImgTask4=[dataTime[31][1],dataTime[33][1],dataTime[35][1],dataTime[37][1]]
#
# ImgTask1_2=[dataTime[63][1],dataTime[66][1],dataTime[68][1],dataTime[70][1]]
# ImgTask2_2=[dataTime[72][1],dataTime[74][1],dataTime[76][1],dataTime[78][1]]
# ImgTask3_2=[dataTime[80][1],dataTime[82][1],dataTime[82][1],dataTime[84][1]]
# ImgTask4_2=[dataTime[90][1],dataTime[92][1],dataTime[94][1],dataTime[96][1]]
#
#
# # print(ImgTask1)
# # print(ImgTask1_2)
# #
# # print("...")
# #
# # print(ImgTask2)
# # print(ImgTask2_2)
# #
# # print("...")
# #
# # print(ImgTask3)
# # print(ImgTask3_2)
# #
# # print("...")
# # print(ImgTask4)
# # print(ImgTask4_2)
#
# # Rimuovi gli apici singoli e gli spazi vuoti
# #LE IMMAGINI DEL TASK 1 PRIMA E SECONDA PARTE ORDINTE
# ImgTask1 = [x.strip("' ").strip() for x in ImgTask1]
# ImgTask1_2 = [x.strip("' ").strip() for x in ImgTask1_2]
#
# #SECONDO TASK
# ImgTask2 = [x.strip("' ").strip() for x in ImgTask2]
# ImgTask2_2 = [x.strip("' ").strip() for x in ImgTask2_2]
#
# #TERZO TASK
# ImgTask3=[x.strip("' ").strip() for x in ImgTask3]
# ImgTask3_2 = [x.strip("' ").strip() for x in ImgTask3_2]
#
# #QUARTO TASK
# ImgTask4=[x.strip("' ").strip() for x in ImgTask4]
# ImgTask4_2=[x.strip("' ").strip() for x in ImgTask4_2]
#
#
#
#
#
#
#
#
#
#
# # Ordina gli array
# ImgTask1.sort()
# ImgTask1_2.sort()
#
# ImgTask2.sort()
# ImgTask2_2.sort()
#
# ImgTask3.sort()
# ImgTask3_2.sort()
#
# ImgTask4.sort()
# ImgTask4_2.sort()

# print(ImgTask1)
# print(ImgTask1_2)
#
# print("...")
# print(ImgTask2)
# print(ImgTask2_2)
#
# print("...")
#
# print(ImgTask3)
# print(ImgTask3_2)
#
# print("...")
# print(ImgTask4)
# print(ImgTask4_2)







#CALCO FISS TASK 1    1 E 2 SECONDA VOLTA





# Dettagli del grafico
#Marcatori

colors = ["blue","red","purple","yellow"]



fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 16, 1))
ax.tick_params(axis='x', which='major', labelsize=10, pad=4)
plt.xticks(rotation=20)


#PRIM0 TASK



plt.bar(ImgTask4[0], sum_f1[0], width=0.3,color=colors[0],label="Prima visione della foto dx")
plt.bar(0.3, sum_f2[0], width=0.3,color=colors[1],label="Seconda visione della foto dx")

plt.bar(ImgTask4[1], sum_f1[1], width=0.3,color=colors[0])
plt.bar(1.3, sum_f2[1], width=0.3,color=colors[1])

plt.bar(ImgTask4[2], sum_f1[2], width=0.3,color=colors[0])
plt.bar(2.3, sum_f2[2], width=0.3,color=colors[1])

plt.bar(ImgTask4[3], sum_f1[3], width=0.3,color=colors[0])
plt.bar(3.3, sum_f2[3], width=0.3,color=colors[1])





# Annotazioni per ogni barra che restituisce il numero di fissazioni
for i in range(len(sum_f1)):
    plt.annotate(sum_f1[i], (-0.19 + i, sum_f1[i]))
for j in range(len(sum_f2)):
    plt.annotate(sum_f2[j], ( j+0.2, sum_f2[j]))

ytemp=max(sum_f1)
ytemp2=max(sum_f2)
ytempf=[ytemp,ytemp2]

plt.ylim([0, max(ytempf)+20])
plt.ylabel('Numero di fissazioni')
plt.xlabel('Immagine')
plt.title('Grafico delle Frequenze assolute relativo al TASK  4',fontweight='bold', fontsize=15)
plt.legend(loc="best")
# print(count)
if count==1:
 name=str(os.path.dirname(pathTime))
 fig.savefig(name+"SingoloPazienteImg"+".png")
elif count>2:
    name = str(os.path.dirname(pathTime))
    fig.savefig(name +"PiùPazientiImg" + ".png")

plt.show()




#SECONDO GRAFICO VAL MAX MIN AVG
#dati grafico linee multiple max,medio,min
#Prima Parte

valmax4=max(sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3])
#Seconda Parte

valmax4_2=max(sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[3])


#array prima e seconda parte

array4=[sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3]]


array4_2=[sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[3]]



#media prima parte

valavg4=sum(array4)/4

#media seconda parte

valavg4_2=sum(array4_2)/4




#valore minimo prima parte

valmin4=min(sum_f1[0],sum_f1[1],sum_f1[2],sum_f1[3])



valmin4_2=min(sum_f2[0],sum_f2[1],sum_f2[2],sum_f2[4])





fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12, 8))

# Dati per il grafico
x = [26,60,90,133,206,236,266,319]  # Valori sull'asse x
y1 = [valmax4,valmax4_2]  # Valori max
y2 = [valmin4,valmin4_2]  # Valori min
y3 = [valavg4,valavg4_2]  # Valori avg

# Creazione del grafico
plt.plot(x, y2,'-o', label='Valore min',colors="purple")
plt.plot(x, y3,'-o', label='Valore avg',colors="green")
plt.plot(x, y1,'-o',label='Valore max',colors="orange")

# Aggiunta di etichette e titolo
plt.xlabel('Tempo(sec)')
plt.ylabel('Valori Fissazioni')
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




'''
'''plt.plot(val[1], valmin1, width=0.3,color=colori[0])
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