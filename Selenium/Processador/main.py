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
url = 'https://www.cpubenchmark.net/cpu_list.php'
print("[main.py] url: "+url)
#createDir('cpus.csv')

driver_url = logIn(url)
data1t = getPerfil(driver_url)
getLink(data1t)

print(url)


#saveData(data1,data2)
#merge_all_to_a_book(glob.glob("data.csv"), "data.xlsx")
driver_url.close()
