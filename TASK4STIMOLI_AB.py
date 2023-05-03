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


n=int(sg.popup_get_text("Quanti pazienti vuoi analizzare(grafico immagini)?"))


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


dur1_1=[]
dur1_2=[]
dur2_1=[]
dur2_2=[]
dur3_1=[]
dur3_2=[]
dur4_1=[]
dur4_2=[]




valorii = []
valneutro = []
stimolo = []
valoreneu = 0
dur_stimolo=[]
dur_neutro=[]

dxx2=[]
sxx2=[]
dxx3=[]
sxx3=[]
dxx4=[]
sxx4=[]
dxx5=[]
sxx5=[]








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

 center = (displayHeight*posXPix[riga]) - (displayWidth*posYPix[riga])
 fix.remove(fix[0])
 print(fix)
 sx_fixations = [i for i in fix if posX[riga] <= center]
 dx_fixations = [i for i in fix if posX[riga] > center]

 print("Fissazioni a sinistra:", sx_fixations)
 print("Fissazioni a destra:", dx_fixations)

 return sx_fixations, dx_fixations


def durataFiss(csv_file, time1, line,dx,sx):
 fileFix = pd.read_csv(csv_file, sep=',', engine='python', header=None)
 dataFix = fileFix.values.tolist()
 duration_stim = []
 duration_neu = []
 parameter_to_find = int(time1)
 print(time1)


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



  for l in range(sum(dx + sx)):
    if (sum(sx) == 0):
     duration_neu.append(dataFix[line + l][2])
    else:
     duration_stim.append(dataFix[line + l][2])
  print(time1)
  print(line)
  print(sx, dx)
  print("VALORIIIIII")
  print(duration_stim, duration_neu)
  return duration_stim, duration_neu








def RecupImg(dataTime):
 # hypersex
 for i in dataTime:

  if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4_09/T4_09_AB.jpg") and i[4].endswith("]"):
   ImgTask4.append(i[1])
   Time1.append(i[2])
   Time1_2.append(i[3])
  for j, row in enumerate(dataTime):
   if " 'T4_09/T4_09_AB.jpg'" in row:
    print(f'Riga {j + 1}: {row}')
    print('La riga  è:', j + 1)
    riga1 = j + 1

 # gambling
 for k in dataTime:

  if k[0] == "['Decision_making_image'" and k[1].startswith(" 'T4_05/T4_05_AB.jpg") and k[4].endswith("]"):
   ImgTask42.append(k[1])
   Time1.append(k[2])
   Time1_2.append(k[3])
  for j, row in enumerate(dataTime):
   if " 'T4_05/T4_05_AB.jpg'" in row:
    print(f'Riga {j + 1}: {row}')
    print('La riga  è:', j + 1)
    riga2 = j + 1

 # eating
 for t in dataTime:

  if t[0] == "['Decision_making_image'" and t[1].startswith(" 'T4_03/T4_03_AB.jpg") and t[4].endswith("]"):
   ImgTask43.append(t[1])
   Time3.append(t[2])
   Time3_2.append(t[3])
  for j, row in enumerate(dataTime):
   if " 'T4_03/T4_03_AB.jpg'" in row:
    print(f'Riga {j + 1}: {row}')
    print('La riga  è:', j + 1)
    riga3 = j + 1

 # shopping
 for s in dataTime:

  if s[0] == "['Decision_making_image'" and s[1].startswith(" 'T4_13/T4_13_AB.jpg") and s[4].endswith("]"):
   ImgTask44.append(s[1])
   Time4.append(s[2])
   Time4_2.append(s[3])
  for j, row in enumerate(dataTime):
   if " 'T4_13/T4_13_AB.jpg'" in row:
    print(f'Riga {j + 1}: {row}')
    print('La riga  è:', j + 1)
    riga4 = j + 1

 print(riga1)
 print(ImgTask4)
 print(Time1)
 print(Time1_2)

 # hpesex time
 delta1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga1][2])
 delta2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga1][3])
 Hypersex = calcolofissdxsx(delta1, delta1, delta2, riga1, csv_file)
 sx2 = Hypersex[0]
 if (len(sx2) == 0): sx2.append(0)

 dx2 = Hypersex[1]
 if (len(dx2) == 0): dx2.append(0)
 print(Hypersex)

 # gambling
 delta2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga2][2])
 delta3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga2][3])
 Gamb = calcolofissdxsx(delta2, delta2, delta3, riga2, csv_file)
 sx3 = Gamb[0]
 if (len(sx3) == 0): sx3.append(0)

 dx3 = Gamb[1]
 if (len(dx3) == 0): dx3.append(0)
 print(Gamb)

 # EATING
 delta3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga3][2])
 delta4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga3][3])
 eat = calcolofissdxsx(delta3, delta3, delta4, riga3, csv_file)
 sx4 = eat[0]
 if (len(sx4) == 0): sx4.append(0)

 dx4 = eat[1]
 if (len(dx4) == 0): dx4.append(0)
 print(eat)

 # SHOPPING
 delta4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga4][2])
 delta5 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[riga4][3])
 shop = calcolofissdxsx(delta4, delta4, delta5, riga4, csv_file)
 sx5 = shop[0]
 if (len(sx5) == 0): sx5.append(0)

 dx5 = shop[1]
 if (len(dx5) == 0): dx5.append(0)
 print(shop)

 line1 = ""
 line2 = ""
 line3 = ""
 line4 = ""

 dura1_1,dura1_2 = durataFiss(csv_file, delta1, line1, dx2, sx2)
 dura2_1,dura2_2 = durataFiss(csv_file, delta2, line2, dx3, sx3)
 dura3_1,dura3_2 = durataFiss(csv_file, delta3, line3, dx4, sx4)
 dura4_1,dura4_2 = durataFiss(csv_file, delta4, line4, dx5, sx5)

 dura1_1=PiuPazientiDur(dura1_1,n)
 dura1_2=PiuPazientiDur(dura1_2,n)

 dura2_1 = PiuPazientiDur(dura2_1, n)
 dura2_2 = PiuPazientiDur(dura2_2, n)

 dura3_1 = PiuPazientiDur(dura3_1, n)
 dura3_2 = PiuPazientiDur(dura3_2, n)

 dura4_1 = PiuPazientiDur(dura4_1, n)
 dura4_2 = PiuPazientiDur(dura4_2, n)

 return sx2, dx2, sx3, dx3, sx4, dx4, sx5, dx5, dura1_1,dura1_2,dura2_1,dura2_2,dura3_1,dura3_2,dura4_1,dura4_2


def PiuPazientiDur(Listfix1, n):
 for i in range(len(Listfix1)):
  Listfix1[i] = float(Listfix1[i])
  if n == 1:
   Listfix1[i] = Listfix1[i]
  if n > 2:
   Listfix1[i] = Listfix1[i] + Listfix1[i]

 return Listfix1





for i in range(n):
        sg.popup("Inserire i file del paziente n:", i + 1)
        pathTime = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA TEMPI.TXT del paziente")
        fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
        dataTime = fileTime.values.tolist()
        # print(dataTime)
        csv_file = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FILE FIX.CSV del paziente")
        sxx2, dxx2, sxx3, dxx3, sxx4, dxx4, sxx5, dxx5,dur1_1,dur1_2,dur2_1,dur2_2,dur3_1,dur3_2,dur4_1,dur4_2=RecupImg(dataTime)













        valorii = [
          int(dxx2[0]), int(sxx2[0]),
          int(dxx3[0]), int(sxx3[0]),
          int(dxx4[0]), int(sxx4[0]),
          int(dxx5[0]), int(sxx5[0])]

        valneutro = [int(dxx2[0]), int(dxx3[0]), int(dxx4[0]), int(dxx5[0])]
        stimolo = [int(sxx2[0]), int(sxx3[0]), int(sxx4[0]), int(sxx5[0])]



        valoreneu = sum(valneutro)

        # durate delle fissazioni in ms

        print("durateeeeeeeee")


























#FUNZIONI PER RECUPERARE LE DURATE NETURE E CON STIMOLO DI OGNI IMMAGINE DICOTOMICA
#prendiamo la riga e il tempo, per prendere la durate delle fix che si sono verifcate quando c'è stata la foto







fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 16, 1))
ax.tick_params(axis='x', which='major', labelsize=10, pad=4)
plt.xticks(rotation=20)


plt.bar("Hypersexuality", stimolo[0],label=ImgTask4[0],color="red")
plt.bar("Gambling", stimolo[1],label=ImgTask42[0],color="blue")
plt.bar("Eating", stimolo[2],label=ImgTask43[0],color="green")
plt.bar("Shopping", stimolo[3],label=ImgTask44[0],color="pink")
plt.bar("Neutra",valoreneu,label="Immagine neutra",color="yellow")
plt.ylabel('Valore totale delle fissazioni')
plt.suptitle('Grafico delle frequenze assolute rispetto al task 4 dicotomico',fontweight='bold',fontsize=16)
plt.title('Il valore totale delle fissazioni fa riferimento alle foto con AB,dove:la foto neutra è a dx, e la foto con stimolo è a sx',fontsize=10)
plt.legend(loc="best")
fig.savefig('grafic/STIMOLONEU_AB.png')

plt.show()

dur_stimolo=dur1_1+dur2_1+dur3_1+dur4_1
dur_neutro=dur1_2+dur2_2+dur3_2+dur4_2


#BOXPLOT

data=[dur_stimolo,dur_neutro]
fig, ax = plt.subplots(figsize=(12,8))
bp = ax.boxplot(data,labels=["Immagini con stimolo","Neutre"])

# Personalizzazione dell'asse y

plt.ylabel("Tempo(ms)",size=9)
plt.suptitle("Boxplot task 4 dicotomico:\nRappresentazione visuale della durata delle fissazioni",size=11,fontweight='bold')
plt.title("Le durate delle fissazioni fanno riferimento alle foto che hanno la sigla AB,dove:la foto neutra è a dx, e la foto con stimolo è a sx", transform=ax.transAxes,
        fontsize=10, va='top', ha='center')



# Mostra il grafico
fig.savefig('grafic/boxplotsk4IMG.png')
plt.show()




