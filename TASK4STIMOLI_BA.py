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



pathTime = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA TEMPI.TXT del paziente")
fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
dataTime = fileTime.values.tolist()
# print(dataTime)
csv_file = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FILE FIX.CSV del paziente")

#hypersex
ImgTask4 = []
Time1=[]
Time1_2=[]
riga1=0

#gambling
ImgTask42 = []
Time2=[]
Time2_2=[]
riga2=0

#eating
ImgTask43 = []
Time3=[]
Time3_2=[]
riga3=0


#shopping
ImgTask44 = []
Time4=[]
Time4_2=[]
riga4=0




def Fisstask(time1, time2, time3, csv_filef):
 listTime = []
 listTime.append(time1)
 inter = []
 Timeimg = [time1, time2, time3]
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
 data = dataFrame.iloc[:, [0, 1, 2, 3, 4]].values  # Prendo i valori che mi serviranno
 times = [element for element in data[:, 1]] # 4
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






root = tk.Tk()  # Libreria tkinter


def calcolofissdxsx(time1, time2, time3, riga, csv_file):
 fix = Fisstask(time1, time2, time3, csv_file)
 dataFrame = pd.read_csv(csv_file)
 data = dataFrame.iloc[:, [0, 1, 2, 3, 4]].values
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

 center = (displayHeight * posXPix[riga]) - (displayWidth * posYPix[riga])
 fix.remove(fix[0])
 print(fix)
 sx_fixations = [i for i in fix if posX[riga] <= center]
 dx_fixations = [i for i in fix if posX[riga] > center]

 print("Fissazioni a sinistra:", sx_fixations)
 print("Fissazioni a destra:", dx_fixations)

 return sx_fixations, dx_fixations





#hypersex
for i in dataTime :

    if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4_09/T4_09_BA.jpg") and i[4].endswith("]"):
     ImgTask4.append(i[1])
     Time1.append(i[2])
     Time1_2.append(i[3])
    for x, row in enumerate(dataTime):
     if " 'T4_09/T4_09_BA.jpg'" in row:
      print(f'Riga {x + 1}: {row}')
      print('La riga  è:', x+1)
      riga1=x+1

#gambling
for k in dataTime :

    if k[0] == "['Decision_making_image'" and k[1].startswith(" 'T4_05/T4_05_BA.jpg") and k[4].endswith("]"):
     ImgTask42.append(k[1])
     Time1.append(k[2])
     Time1_2.append(k[3])
    for q, row in enumerate(dataTime):
     if " 'T4_05/T4_05_BA.jpg'" in row:
      print(f'Riga {q + 1}: {row}')
      print('La riga  è:', q+1)
      riga2=q+1


#eating
for t in dataTime :

    if t[0] == "['Decision_making_image'" and t[1].startswith(" 'T4_03/T4_03_BA.jpg") and t[4].endswith("]"):
     ImgTask43.append(t[1])
     Time3.append(t[2])
     Time3_2.append(t[3])
    for y, row in enumerate(dataTime):
     if " 'T4_03/T4_03_BA.jpg'" in row:
      print(f'Riga {y + 1}: {row}')
      print('La riga  è:', y+1)
      riga3=y+1



#shopping
for s in dataTime :

    if s[0] == "['Decision_making_image'" and s[1].startswith(" 'T4_13/T4_13_BA.jpg") and s[4].endswith("]"):
     ImgTask44.append(s[1])
     Time4.append(s[2])
     Time4_2.append(s[3])
    for v, row in enumerate(dataTime):
     if " 'T4_13/T4_13_BA.jpg'" in row:
      print(f'Riga {v + 1}: {row}')
      print('La riga  è:', v+1)
      riga4=v+1

print(riga1)
print(ImgTask4)
print(Time1)
print(Time1_2)


def durataFiss(csv_file,time1,riga1,time2,riga2,time3,riga3,time4,riga4):
 fileFix = pd.read_csv(csv_file, sep=',', engine='python', header=None)
 dataFix = fileFix.values.tolist()
 print(dataFix[1][1])
 duration_stim=[]
 duration_neu=[]


#recupero le durate delle fissazioni che sono presenti nell'intorno di tempo che appare la foto presa in esame
#con numf recupero il numero di fissazioni presenti e la loro relativa durata

 for j, row in enumerate(dataFix):
  for l in range(sum(dx2+sx2)):
   if float(dataFix[riga1+l][1])<=round(time1) and (len(sx2) == 0) :
    dur_stimolo.append(dataFix[riga1+l][2])
   else:duration_neu.append(dataFix[riga1+l][2])
   print(time1)
   print(riga1)
   print(sx2,dx2)

  print(duration_stim,duration_neu)
  return duration_stim,duration_neu






#hpesex time
delta1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga1][2])
delta2=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga1][3])
Hypersex=calcolofissdxsx(delta1,delta1,delta2,riga1,csv_file)#calcolo il num di fissazioni dove è presente la foto hpsex(riga)
sx2=Hypersex[0]
if(len(sx2)==0):sx2.append(0)

dx2=Hypersex[1]
if(len(dx2)==0):dx2.append(0)
print(Hypersex)


#gambling
delta2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga2][2])
delta3=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga2][3])
Gamb=calcolofissdxsx(delta2,delta2,delta3,riga2,csv_file)
sx3=Gamb[0]
if(len(sx3)==0):sx3.append(0)

dx3=Gamb[1]
if(len(dx3)==0):dx3.append(0)
print(Gamb)



#EATING
delta3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga3][2])
delta4=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga3][3])
eat=calcolofissdxsx(delta3,delta3,delta4,riga3,csv_file)
sx4=eat[0]
if(len(sx4)==0):sx4.append(0)

dx4=eat[1]
if(len(dx4)==0):dx4.append(0)
print(eat)


#SHOPPING
delta4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga4][2])
delta5=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga4][3])
shop=calcolofissdxsx(delta4,delta4,delta5,riga4,csv_file)
sx5=shop[0]
if(len(sx5)==0):sx5.append(0)

dx5=shop[1]
if(len(dx5)==0):dx5.append(0)
print(shop)


valorii = [
          int(dx2[0]), int(sx2[0]),
          int(dx3[0]), int(sx3[0]),
          int(dx4[0]), int(sx4[0]),
          int(dx5[0]),int(sx5[0])]

valneutro=[int(sx2[0]),int(sx3[0]),int(sx4[0]),int(sx5[0])]
stimolo=[int(dx2[0]),int(dx3[0]),int(dx4[0]),int(dx5[0])]
valoreneu=sum(valneutro)


float_dur=[]


#durate delle fissazioni in ms
valtime=[delta1,delta2,delta3,delta4]
valtime.sort()
print(valtime)
array_stim,array_neu=durataFiss(csv_file,valtime[0],riga1,valtime[1],riga2,valtime[2],riga3,valtime[3],riga4)
print("durateeeeeeeee")
print(array_stim,array_neu)









dur_stimolo=[]
dur_neutro=[]
q=0
w=0

'''
#recupero la durate delle fissazioni con stimolo
for q in range(sum(stimolo)):
    dur_stimolo.append(float_dur[q])
    print("DURATE STIMOLO")
    print(dur_stimolo)


#recupero la durata delle fissazioni neutre
for w in range(sum(valneutro)):
    if(sum(valneutro)==len(float_dur)):
     dur_neutro.append(float_dur[q+w])
    else:dur_neutro.append(float_dur[q+w+1])

    print("DURATE NEUTRE")
    print(dur_neutro)'''










fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 16, 1))
ax.tick_params(axis='x', which='major', labelsize=10, pad=4)
plt.xticks(rotation=20)
plt.ylim([0,20])

plt.bar("Hypersexuality", valorii[0],label=ImgTask4,color="red")
plt.bar("Gambling", valorii[2],label=ImgTask42,color="blue")
plt.bar("Eating", valorii[4],label=ImgTask43,color="green")
plt.bar("Shopping", valorii[6],label=ImgTask44,color="pink")
plt.bar("Neutra",valoreneu,label="Immagine neutra",color="yellow")
plt.ylabel('Valori fissazioni')
plt.suptitle('Grafico delle frequenze assolute rispetto al task 4 dicotomico',fontweight='bold',size=16)
plt.title(' Il numero di fissazioni fanno riferimento alle foto con BA,dove:la foto neutra è a sx, e la foto con stimolo è a dx',size=10)
plt.legend(loc="best")
fig.savefig('grafic/STIMOLONEU_BA.png')

plt.show()



#BOXPLOT

#passo le durate delle fissazioni con stimolo e neutre
data=[dur_stimolo,dur_neutro]
fig, ax = plt.subplots(figsize=(12,8))
bp = ax.boxplot(data,labels=["Immagine con stimolo","Neutro"])






# Personalizzazione dell'asse y

plt.ylabel("Tempo(ms)",size=9)
plt.suptitle("Boxplot task 4 dicotomico:\nRappresentazione visuale della durata delle fissazioni",size=11,fontweight='bold')
plt.title("Le durate delle fissazioni fanno riferimento alle foto che hanno sigla BA,dove:la foto neutra è a sx, e la foto con stimolo è a dx", transform=ax.transAxes,
        fontsize=10, va='top', ha='center')




# Mostra il grafico
fig.savefig('grafic/boxplotsk4IMG.png')
plt.show()




