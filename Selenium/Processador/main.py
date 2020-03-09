# -*- coding: utf-8 -*-
from configs import *
from getPerfil import *
from selenium import webdriver
from download import *
#from getPhotos import *
#from saveData import *
#from pyexcel.cookbook import merge_all_to_a_book
#import glob
#from getInfos import *
escolha = input("Selecione 1 para processadores e 2 para RAM:   ")
if escolha == 1:
    url = 'https://www.cpubenchmark.net/cpu_list.php'
    pontuacaoMin = input("Qual a pontuacao minima? (escreva apenas o numero)   ")
    clockMin = input("Qual clock minimo? (escreva apenas o numero) ")
    nucleosMin = input("Qual a quantidade de nucleos minima? (escreva apenas o numero)   ")
    tdpMin = input("Qual a tdp minima? (escreva apenas o numero)    ")
else:
    url = 'https://www.memorybenchmark.net/ram_list.php'
    latenciaCorte = input("Qual o minimo de latencia? (escreva apenas o numero em ns)   ")
    capMin = input("Qual o minimo de capacidade? (escreva apenas o numero em GB)   ")
    

print("[main.py] url: "+url)
#createDir('cpus.csv')
driver_url = logIn(url)
data1t = getPerfil(driver_url)
if escolha == 1:
    getLinkCPU(data1t,pontuacaoMin,clockMin,tdpMin,nucleosMin)
else:
    getLinkRAM(data1t,latenciaCorte,capMin)

#saveData(data1,data2)
#merge_all_to_a_book(glob.glob("data.csv"), "data.xlsx")
driver_url.close()
