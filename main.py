import matplotlib.pyplot as plt
import csv
import numpy as np
import PySimpleGUI as sg
import pandas as pd
import os
import matplotlib.image as mpimg

#img=mpimg.imread('res/chicca.jpg')
#type(img)

'''plt.rcParams['figure.figsize'] = [12,8]

mq = np.random.randint(100,size=50) # generiamo 50 valori casuali compresi tra 0 e 100
price = np.power(mq,2)*10 # generiamo i valori del prezzo come il quadrato dei metri quadri moltiplicato per 10
noise = np.random.rand(50)*25000 # creiamo un po' di rumore...
price = (price+noise) # ...e aggiungiamolo al prezzo

plt.scatter(mq,price)
plt.show()

plt.title("Rapporto dimensione-valore di monolocali")
plt.xlabel("Dimensione in metri quadri")
plt.ylabel("Valore in euro")
plt.grid()

plt.scatter(mq,price)
plt.show()

mq_center = np.random.randint(100,size=10)
price_center = np.power(mq_center,2)*1.5
noise = np.random.rand(10)*2500
price_center = (price_center+noise)*10

plt.title("Rapporto dimensione-valore di monolocali")
plt.xlabel("Dimensione in metri quadri")
plt.ylabel("Valore in euro")
plt.grid()

plt.scatter(mq, price)
plt.scatter(mq_center, price_center, s=100., c="green")
plt.show()


plt.title("Rapporto dimensione-valore di monolocali")
plt.xlabel("Dimensione in metri quadri")
plt.ylabel("Valore in euro")
plt.grid()

plt.scatter(mq, price, label="appartamenti in periferia") # aggiungiamo un label per i monolocali in centro
plt.scatter(mq_center, price_center, marker="s",  c="green", label="appartamenti in centro") # aggiungiamo un label per i monolocali in centro

plt.legend() # mostriamo la legenda

plt.savefig("res/scatter.png")# esportiamo il grafico in un file chiamato 'scatter.png' all'interno della cartella 'res'

stock_price = np.power(np.arange(30,130),1) + np.random.rand(100)*10
plt.title("Valore del titolo PROFAI per i primi 100 giorni di trading")
plt.xlabel("Giorno")
plt.ylabel("Valore in euro")
plt.grid()
plt.plot(stock_price)
plt.show()'''

#PUPILS STATICS.CSV DA SELEZIONARE

file=sg.popup_get_file(sg.FolderBrowse())

with open(file,'r') as dati:
    for linea in csv.reader(dati):
        print(linea[0])



TotalAverageLeft=float(linea[0])
TotalAverageRight=float(linea[1])
TotalAverageLFandRG=float(linea[2])
MinDiameterLeft=float(linea[3])
MinDiameterRight=float(linea[4])
MaxDiameterLeft=float(linea[5])
MaxDiameterRight=float(linea[6])





plt.rcParams['figure.figsize'] = [12,8]
plt.bar(1,TotalAverageLeft,label="TotalAvarageLeft")
plt.bar(2,TotalAverageRight, label="TotalAverageRight")
plt.bar(3,TotalAverageLFandRG, label="TotalAverageLFandRG")
plt.bar(4,MinDiameterLeft, label="MinDiameterLeft")
plt.bar(5,MinDiameterRight, label="MinDiameterRight")
plt.bar(6,MaxDiameterLeft,label="MaxDiameterLeft")
plt.bar(7,MaxDiameterRight,label="MaxDiameterRight")

plt.title("Confronto dati pupillari")
plt.xlabel("VALORI DEL FILE CSV PUPILS STATISTIC")
plt.ylabel("VALORE PUPILLARE")
plt.legend(loc="upper right")

plt.show()

labels = ["Data Scientist","Android Developer","iOS Developer",
         "Ingegnere Informatico","Web Developer"]

salary = [130, 110, 110, 96, 73]
colors = ["blue","red","green","yellow","purple"]
index = np.arange(len(labels))

plt.bar(index,salary,color=colors)
plt.xticks(index, labels, fontsize=12, rotation=30)

plt.title("Confronto salari professionisti IT")
plt.xlabel("Professione")
plt.ylabel("Salario")

plt.show()

