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


valori=[]

for i in range(n):
    sg.popup("Inserire i file del paziente n:",i+1)
    pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT del paziente")
    fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
    dataTime = fileTime.values.tolist()
    # print(dataTime)
    csv_file= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA FILE FIX.CSV del paziente")

#recuper le immagini
delta37 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][2])
delta38 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[31][3])

#prima parte
delta39 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[33][3])
delta40 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[35][3])

delta41 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[35][3])
delta42 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[37][3])

delta43 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[37][2])
delta44 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[38][3])





#seconda parte
delta45 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[90][2])
delta46 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[90][3])

delta47 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[92][3])
delta48 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[94][3])

delta49 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[94][3])
delta50 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[96][3])

delta51 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[96][2])
delta52 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[97][3])



root = tk.Tk()  # Libreria tkinter


#calcolo la posizione e il numero di fissazioni
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
#PRIMA PARTE
#foto 1 sx dx
Img1=calcolofissdxsx(delta37,delta37,delta38,31,csv_file)

sx1=Img1[0]
if(len(sx1)==0):sx1.append(0)

dx1=Img1[1]
if(len(dx1)==0):sx1.append(0)
print(sx1,dx1)



#foto 2 sx dx
Img2=calcolofissdxsx(delta39,delta39,delta40,33,csv_file)
sx2=Img2[0]
if(len(sx2)==0):sx2.append(0)

dx2=Img2[1]
if(len(dx2)==0):dx2.append(0)

print(sx2,dx2)

#foto 3 sx dx
Img3=calcolofissdxsx(delta41,delta41,delta42,35,csv_file)

sx3=Img3[0]
if(len(sx3)==0):sx3.append(0)

dx3=Img3[1]
if(len(dx3)==0):dx3.append(0)
print(sx3,dx3)


#foto 4 sx dx
Img4=calcolofissdxsx(delta43,delta43,delta44,38,csv_file)

sx4=Img4[0]
if(len(sx4)==0):sx4.append(0)

dx4=Img4[1]
if(len(dx4)==0):dx4.append(0)
print(sx4,dx4)



#SECONDA PARTEEE
#foto 1 sx dx
Img5=calcolofissdxsx(delta45,delta46,delta46,90,csv_file)

sx5=Img5[0]
if(len(sx5)==0):sx5.append(0)

dx5=Img5[1]
if(len(dx5)==0):dx5.append(0)
print(sx5,dx5)

#foto 2 sx dx
Img6=calcolofissdxsx(delta47,delta47,delta48,92,csv_file)

sx6=Img6[0]
if(len(sx6)==0):sx6.append(0)

dx6=Img6[1]
if(len(dx6)==0):dx6.append(0)
print(sx6,dx6)

#foto 3 sx dx
Img7=calcolofissdxsx(delta49,delta49,delta50,94,csv_file)

sx7=Img7[0]
if(len(sx7)==0):sx7.append(0)

dx7=Img7[1]
if(len(dx7)==0):dx7.append(0)
print(sx7,dx7)


#foto 4 sx dx
Img8=calcolofissdxsx(delta51,delta51,delta52,96,csv_file)

sx8=Img8[0]
if(len(sx8)==0):sx8.append(0)

dx8=Img8[1]
if(len(dx8)==0):dx8.append(0)
print(sx8,dx8)



'''sum_array=[Img1[1],Img2[1],Img3[1],Img4[1]]
sum_array2=[Img5[1],Img6[1],Img7[1],Img8[1]]'''

valorii = [int(dx1[0]), int(sx1[0]), int(dx5[0]), int(sx5[0]),
          int(dx2[0]), int(sx2[0]), int(dx6[0]), int(sx6[0]),
          int(dx3[0]), int(sx3[0]), int(dx7[0]), int(sx7[0])
         ,int(dx4[0]), int(sx4[0]), int(dx8[0]), int(sx8[0])]



for j in range(len(valorii)):
    if i==0:
        count=i+1
        valori.append(valorii[j])
    elif i==1:
     count=i+2
     valori.append(valorii[j] + valorii[j])
    elif i==2:
     valori.append(valorii[j] + valorii[j]+valorii[j])
    elif i == 3:
        valori.append(valorii[j] + valorii[j] + valorii[j]+valorii[j])
    elif i == 4:
        valori.append(valorii[j] + valorii[j] + valorii[j] + valorii[j]+valorii[j])





#Recupero i nomi delle immagini dei vari task

ImgTask4 = []
for i in dataTime :
  if i[0] == "['Decision_making_image'" and i[1].startswith(" 'T4"):
        ImgTask4.append(i[1])






#CALCO FISS TASK 1    1 E 2 SECONDA VOLTA





# Dettagli del grafico
#Marcatori

colors = ["blue","red"]



fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 16, 1))
ax.tick_params(axis='x', which='major', labelsize=5, pad=4)
plt.xticks(rotation=20)
plt.ylim([0,30])

#PRIM0 TASK

etichette = [ImgTask4[0], ImgTask4[0]+"sx1_1",ImgTask4[0]+"dx2_1",ImgTask4[0]+"sx2_1",
             ImgTask4[1],ImgTask4[1]+"sx1_2", ImgTask4[1]+"dx2_2", ImgTask4[1]+"sx2_2",
             ImgTask4[2],ImgTask4[2]+"sx1_3", ImgTask4[2]+"dx2_3", ImgTask4[2]+"sx2_3",
             ImgTask4[3],ImgTask4[3]+"sx1_4",ImgTask4[3]+"dx2_4",ImgTask4[3]+"sx2_4"]
valori = [int(dx1[0]), int(sx1[0]), int(dx5[0]), int(sx5[0]),
          int(dx2[0]), int(sx2[0]), int(dx6[0]), int(sx6[0]),
          int(dx3[0]), int(sx3[0]), int(dx7[0]), int(sx7[0])
         ,int(dx4[0]), int(sx4[0]), int(dx8[0]), int(sx8[0])]

# Creazione dell'istogramma
plt.bar(etichette[0], valori[0],label="Fiss.Immagine dx prima e seconda parte",color="blue",width=0.7)
plt.bar(etichette[1], valori[1],label="Fiss.Immagine sx prima e seconda parte",color="red",width=0.7)
plt.bar(etichette[2], valori[2],color="blue",width=0.7)
plt.bar(etichette[3], valori[3],color="red",width=0.7)

plt.axvline(x=3.5, color='red', linestyle='--', label="Divosore Immagine")

plt.bar(etichette[4], valori[4],color="blue",width=0.7)
plt.bar(etichette[5], valori[5],color="red",width=0.7)
plt.bar(etichette[6], valori[6],color="blue",width=0.7)
plt.bar(etichette[7], valori[7],color="red",width=0.7)

plt.axvline(x=7.5, color='red', linestyle='--')

plt.bar(etichette[8], valori[8],color="blue",width=0.7)
plt.bar(etichette[9], valori[9],color="red",width=0.7)
plt.bar(etichette[10], valori[10],color="blue",width=0.7)
plt.bar(etichette[11], valori[11],color="red",width=0.7)

plt.axvline(x=11.5, color='red', linestyle='--')

plt.bar(etichette[12], valori[12],color="blue",width=0.7)
plt.bar(etichette[13], valori[13],color="red",width=0.7)
plt.bar(etichette[14], valori[15],color="blue",width=0.7)
plt.bar(etichette[15], valori[15],color="red",width=0.7)








#plt.ylim([0, max(ytempf)+20])
plt.ylabel('Numero di fissazioni')
plt.xlabel('Immagini del task 4')
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

valmax4=max(valori[1],valori[2],valori[4],valori[5],valori[8],valori[9],valori[12],valori[13])
#Seconda Parte

valmax4_2=max(valori[2],valori[3],valori[6],valori[7],valori[10],valori[11],valori[14],valori[15])


#array prima e seconda parte

array4=[valori[1],valori[2],valori[4],valori[5],valori[8],valori[9],valori[12],valori[13]]


array4_2=[valori[2],valori[3],valori[6],valori[7],valori[10],valori[11],valori[14],valori[15]]



#media prima parte

valavg4=sum(array4)/8

#media seconda parte

valavg4_2=sum(array4_2)/8




#valore minimo prima parte

valmin4=min(valori[1],valori[2],valori[4],valori[5],valori[8],valori[9],valori[12],valori[13])



valmin4_2=min(valori[2],valori[3],valori[6],valori[7],valori[10],valori[11],valori[14],valori[15])





fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12, 8))

# Dati per il grafico
x = [206,319]  # Valori sull'asse x
y1 = [valmax4,valmax4_2]  # Valori max
y2 = [valmin4,valmin4_2]  # Valori min
y3 = [valavg4,valavg4_2]  # Valori avg

# Creazione del grafico
plt.plot(x, y2,'-o', label='Valore min',color="purple")
plt.plot(x, y3,'-o', label='Valore avg',color="green")
plt.plot(x, y1,'-o',label='Valore max',color="orange")

# Aggiunta di etichette e titolo
plt.xlabel('Tempo(sec)')
plt.ylabel('Valori fissazioni')
plt.title('Grafico a linee multiple delle Immagini del task 4(dx,sx)')
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




