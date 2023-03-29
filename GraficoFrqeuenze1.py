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




pathGaze=sg.popup_get_file(sg.FileBrowse(),title="RECUPERA GAZEDATA")
with gzip.open(pathGaze) as f1:
    time = []
    for data in f1:
     d = json.loads(data)
     timestamp = d.get('timestamp')
     time.append(timestamp)


pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT")
fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
dataTime = fileTime.values.tolist()

#recupero tempi delle immagini della prima parte
delta_sec_7_1=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][2])
delta_sec_7_2=delta_unix_respect_to_video_start(dataTime[0][2], dataTime[7][3])
delta_sec_9_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[9][2])#img croce
delta_sec_9_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[9][3])
delta_sec_11_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[11][2])
delta_sec_11_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[11][3])
delta_sec_13_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][2])
delta_sec_13_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[13][3])
delta_sec_15_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[15][3])


#recupero quelli delle immagini della seconda parte
#SECONDA IMMAGINE
delta_sec_60_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[59][3])
delta_sec_60_2 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[62][2])
delta_sec_62_3 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[64][2])
delta_sec_62_4 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[66][2])
delta_sec_63_1 = delta_unix_respect_to_video_start(dataTime[0][2], dataTime[69][3])




#PRENDO IL NUMERO DI FISSAZIONE DELLE PRIME 4 IMMAGINE
listTime = []
listTime.append(delta_sec_7_1)
inter = []
Timeimg=[delta_sec_7_1,delta_sec_7_2,delta_sec_9_2,delta_sec_11_2,delta_sec_13_2]
print(Timeimg)
num = 5

for i in range(num):

    if i == num - 1:
        helpTime =delta_sec_15_2
    else:
        helpTime = Timeimg[i]
    numTime = (str(listTime[i]) + '-' + str(helpTime))
    listTime.append(helpTime)
    inter.append(numTime)


# dati del grafico fixation
csv_file = 'out/fixation.csv'
dataFrame = pd.read_csv(csv_file)
data = dataFrame.iloc[:, [0, 1, 3, 4]].values               # Prendo i valori che mi serviranno
times = [element for element in data[:, 1]]
time2 = []
smin = 0
numF = []



#calco numFix delle foto
for i in range(1, len(listTime)):
    for x in times:
        if x <= listTime[i]:
            time2.append(x)
            numFix = [int(element) for element in data[smin:len(time2), 1]]

    diff = len(time2) - smin
    smin = smin + diff
    numF.append(len(numFix))
    numFix.clear()
    time2.clear()





#FUNZIONE PER IL CALCOLE DELLE SECONDE FISSAZIONI SULLA SECONDE IMMAGINI
def contaImg2():
    listTime = []
    listTime.append(delta_sec_60_1)
    inter = []
    Timeimg = [delta_sec_60_1,delta_sec_60_2, delta_sec_62_3, delta_sec_62_4]
    print(Timeimg)
    num = 5

    for i in range(num):

        if i == num - 1:
            helpTime = delta_sec_63_1
        else:
            helpTime = Timeimg[i]
        numTime = (str(listTime[i]) + '-' + str(helpTime))
        listTime.append(helpTime)
        inter.append(numTime)

    # dati del grafico fixation
    csv_file = 'out/fixation.csv'
    dataFrame = pd.read_csv(csv_file)
    data = dataFrame.iloc[:, [0, 1, 3, 4]].values  # Prendo i valori che mi serviranno
    times = [element for element in data[:, 1]]
    time2 = []
    smin = 0
    numF2 = []

    # calco numFix delle foto
    for i in range(1, len(listTime)):
        for x in times:
            if x <= listTime[i]:
                time2.append(x)
                numFix2 = [int(element) for element in data[smin:len(time2), 1]]
        diff = len(time2) - smin
        smin = smin + diff
        numF2.append(len(numFix2))
        numFix.clear()
        time2.clear()


    return numF2




# Dettagli del grafico
#Marcatori
Idimg=["Img1","img2","Img3","Img4"]
colors = ["blue","red"]

#Contiene le fissazioni delle seconde immagini
Fix2=contaImg2()
#Fix2[0] = Fix2[0]-(Fix2[0]-diff)
#numF[0]=numF[0]-(numF[0]-diff)
fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12, 8))
numF.remove(numF[0])
Fix2.remove(Fix2[0])
print(numF)
print(Fix2)
#PRIMA IMMAGINE
plt.bar(Idimg[0], numF[0], width=0.3,color=colors[0],label="Prima visione della foto")
plt.bar(0.3, Fix2[0], width=0.3,color=colors[1],label="Seconda visione della foto")

#SECONDA IMMAGINE

plt.bar(Idimg[1], numF[1], width=0.3,color=colors[0])
plt.bar(1.3, Fix2[1], width=0.3,color=colors[1])

#TERZA
plt.bar(Idimg[2], numF[2], width=0.3,color=colors[0])
plt.bar(2.3, Fix2[2], width=0.3,color=colors[1])

#QUARTA
plt.bar(Idimg[3], numF[3], width=0.3,color=colors[0])
plt.bar(3.3, Fix2[3], width=0.3,color=colors[1])
# Annotazioni per ogni barra che restituisce il numero di fissazioni
for i in range(len(numF)):
    plt.annotate(numF[i], (-0.05 + i, numF[i]))
for j in range(len(Fix2)):
    plt.annotate(Fix2[j], ( j+0.2, Fix2[j]))

ytemp = max(numF)
ytemp2 = max(Fix2)
ytempf = [ytemp, ytemp2]

plt.ylim([0, max(ytempf) + 10])
plt.ylabel('Numero di fissazioni')
plt.xlabel('Prime 4 immagini del task 1 nella prima e seconda parte ')
plt.title('Grafico delle Frequenze assolute per ciasuna immagine',fontweight='bold', fontsize=15)
plt.legend(loc="best")
fig.savefig('grafic/graficNumFissazioniImg.png')
plt.show()




