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









#!!!!FUNZIONE PER IL CALCOLO DEI tempi delle immagini IN DET INTERVALLO!!!!!
def Fisstask(time1,time2,time3,time4,time5,time6,csv_filef):
    listTime = []
    listTime.append(time1)
    inter = []
    Timeimg = [time1,time2,time3,time4,time5]
    print(Timeimg)
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
    print(Img1)
    print(Img44)
    print(delta1,delta42,delta7,delta48)


    FisstaskP=[Img1[1],Img1[2],Img1[3],Img1[4],Img2[1],Img2[2],Img2[3],Img2[4],Img3[1],Img3[2],Img3[3],Img3[4],Img4[1],Img4[2],Img4[3],Img4[4]]
    FisstaskP2 = [Img11[1], Img11[2], Img11[3], Img11[4], Img22[1], Img22[2], Img22[3], Img22[4], Img33[1], Img33[2], Img33[3], Img33[4], Img44[1], Img44[2], Img44[3], Img44[4]]



    return FisstaskP,FisstaskP2





n=int(sg.popup_get_text("Quanti pazienti vuoi analizzare(grafico immagini)?"))

sum_f1=[]
sum_f2=[]

for i in range(n):
    sg.popup("Inserire i file del paziente n:",i+1)
    pathTime= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA TEMPI.TXT del paziente")
    fileTime = pd.read_csv(pathTime, sep=',', engine='python', header=None)
    dataTime = fileTime.values.tolist()
    csv_file= sg.popup_get_file(sg.FileBrowse(),title="RECUPERA FILE FIX.CSV del paziente")
    sum_array, sum_array2= numFissP(dataTime)

for j in range(len(sum_array)):
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



#RECUPERO LE IMMAGINI E FACCIO IL CONTROLLO
ImgTask1=[dataTime[7][1],dataTime[9][1],dataTime[11][1],dataTime[13][1]]
ImgTask2=[dataTime[15][1],dataTime[17][1],dataTime[19][1],dataTime[21][1]]
ImgTask3=[dataTime[23][1],dataTime[25][1],dataTime[27][1],dataTime[29][1]]
ImgTask4=[dataTime[31][1],dataTime[33][1],dataTime[35][1],dataTime[37][1]]

ImgTask1_2=[dataTime[63][1],dataTime[66][1],dataTime[68][1],dataTime[70][1]]
ImgTask2_2=[dataTime[72][1],dataTime[74][1],dataTime[76][1],dataTime[78][1]]
ImgTask3_2=[dataTime[80][1],dataTime[82][1],dataTime[82][1],dataTime[84][1]]
ImgTask4_2=[dataTime[90][1],dataTime[92][1],dataTime[94][1],dataTime[96][1]]


print(ImgTask1)
print(ImgTask1_2)

print("...")

print(ImgTask2)
print(ImgTask2_2)

print("...")

print(ImgTask3)
print(ImgTask3_2)

print("...")
print(ImgTask4)
print(ImgTask4_2)

# Rimuovi gli apici singoli e gli spazi vuoti
#LE IMMAGINI DEL TASK 1 PRIMA E SECONDA PARTE ORDINTE
ImgTask1 = [x.strip("' ").strip() for x in ImgTask1]
ImgTask1_2 = [x.strip("' ").strip() for x in ImgTask1_2]

#SECONDO TASK
ImgTask2 = [x.strip("' ").strip() for x in ImgTask2]
ImgTask2_2 = [x.strip("' ").strip() for x in ImgTask2_2]

#TERZO TASK
ImgTask3=[x.strip("' ").strip() for x in ImgTask3]
ImgTask3_2 = [x.strip("' ").strip() for x in ImgTask3_2]

#QUARTO TASK
ImgTask4=[x.strip("' ").strip() for x in ImgTask4]
ImgTask4_2=[x.strip("' ").strip() for x in ImgTask4_2]










# Ordina gli array
ImgTask1.sort()
ImgTask1_2.sort()

ImgTask2.sort()
ImgTask2_2.sort()

ImgTask3.sort()
ImgTask3_2.sort()

ImgTask4.sort()
ImgTask4_2.sort()

print(ImgTask1)
print(ImgTask1_2)

print("...")
print(ImgTask2)
print(ImgTask2_2)

print("...")

print(ImgTask3)
print(ImgTask3_2)

print("...")
print(ImgTask4)
print(ImgTask4_2)







#CALCO FISS TASK 1    1 E 2 SECONDA VOLTA





# Dettagli del grafico
#Marcatori

colors = ["blue","red"]



fig, ax = plt.subplots(num='Conteggio Fissazioni', figsize=(12,8))
ax.set_xticks(np.arange(-4, 16, 1))
ax.tick_params(axis='x', which='major', labelsize=3.9, pad=4)


#PRIM0 TASK

plt.bar(ImgTask1[0], sum_f1[0], width=0.3,color=colors[0],label="Prima visione della foto")
plt.bar(0.3, sum_f2[0], width=0.3,color=colors[1],label="Seconda visione della foto")

plt.bar(ImgTask1[1], sum_f1[1], width=0.3,color=colors[0])
plt.bar(1.3, sum_f2[1], width=0.3,color=colors[1])

plt.bar(ImgTask1[2], sum_f1[2], width=0.3,color=colors[0])
plt.bar(2.3, sum_f2[2], width=0.3,color=colors[1])

plt.bar(ImgTask1[3], sum_f1[3], width=0.3,color=colors[0])
plt.bar(3.3, sum_f2[3], width=0.3,color=colors[1])





plt.bar(ImgTask2[0], sum_f1[4], width=0.3,color=colors[0])
plt.bar(4.3, sum_f2[4], width=0.3,color=colors[1])

plt.bar(ImgTask2[1], sum_f1[5], width=0.3,color=colors[0])
plt.bar(5.3, sum_f2[5], width=0.3,color=colors[1])


plt.bar(ImgTask2[2], sum_f1[6], width=0.3,color=colors[0])
plt.bar(6.3, sum_f2[6], width=0.3,color=colors[1])


plt.bar(ImgTask2[3], sum_f1[7], width=0.3,color=colors[0])
plt.bar(7.3, sum_f2[7], width=0.3,color=colors[1])



plt.bar(ImgTask3[0], sum_f1[8], width=0.3,color=colors[0])
plt.bar(8.3, sum_f2[8], width=0.3,color=colors[1])


plt.bar(ImgTask3[1], sum_f1[9], width=0.3,color=colors[0])
plt.bar(9.3, sum_f2[9], width=0.3,color=colors[1])

plt.bar(ImgTask3[2], sum_f1[10], width=0.3,color=colors[0])
plt.bar(10.3, sum_f2[10], width=0.3,color=colors[1])

plt.bar(ImgTask3[3], sum_f1[11], width=0.3,color=colors[0])
plt.bar(11.3, sum_f2[11], width=0.3,color=colors[1])



plt.bar(ImgTask4[0], sum_f1[12], width=0.3,color=colors[0])
plt.bar(12.3, sum_f2[12], width=0.3,color=colors[1])

plt.bar(ImgTask4[1], sum_f1[13], width=0.3,color=colors[0])
plt.bar(13.3, sum_f2[13], width=0.3,color=colors[1])

plt.bar(ImgTask4[2], sum_f1[14], width=0.3,color=colors[0])
plt.bar(14.3, sum_f2[14], width=0.3,color=colors[1])

plt.bar(ImgTask4[3], sum_f1[15], width=0.3,color=colors[0])
plt.bar(15.3, sum_f2[15], width=0.3,color=colors[1])





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
plt.xlabel('Immagine ')
plt.title('Grafico delle Frequenze assolute relativo a una singola immagine',fontweight='bold', fontsize=15)
plt.legend(loc="best")
print(count)
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


print(valmax1,valmax2,valavg1,valavg2,valmin1,valmin2)
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
