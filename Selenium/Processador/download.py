from urllib2 import Request
import os
import base64
from configs import *
import pprint
from saveData import *
def createDir(name):
    try:
        os.mkdir("./data/"+name)
    except:
        print("[download.py] FileExistsError")

def getLink(driver):
    print(len(driver))
    for data in driver:
        try:
            data1 = data.find_elements_by_css_selector('td')
            if(int(data1[1].text)  > 20000):
                print(data1[0].text)
                link = data1[0].find_element_by_css_selector('a').get_attribute('href').split("=")
                link = 'https://www.cpubenchmark.net/cpu.php?cpu='+link[1]+link[2]
                avaliar(link,data1[0].text)
            #print(data.get_attribute('innerHTML'))
        except:
            print('Table Header')
def avaliar(url,name):
    driver = logIn(url)
    data = driver.find_element_by_css_selector('div.left-desc-cpu')
    #print(data.text)
    data = data.find_elements_by_css_selector('p')
    espec = {
        "Classe": data[0].text.split(" ")[1],
        "Socket":data[1].text.split(" ")[1],
        "Clockspeed":float(data[2].text.split(" ")[1]),
        "Turbo":(data[3].text.split(" ")[2]),
        "Nucleos":int(data[4].text.split(" ")[3]),
        "TDP":float(data[5].text.split(" ")[2]),
        "Link": url,
        "Nome": name
    }
    print(espec)
    
    #print(espec['Clockspeed']>= 3)
    #print(espec['Nucleos'] >=8)
    #print(espec['TDP']<=140)

    if ( (espec['Clockspeed']>= 3) and  (espec['Nucleos'] >=8)  and  (espec['TDP']<=140) ): 
        print('CPU Valida')
        saveData(espec)
 
    driver.close()



    
    