from selenium import webdriver
from download import *

def getPerfil(driver):
    print()
    print("---------------------------START GETPERFIL-----------------------------")
    print()

    data = driver.find_element_by_xpath('//table[@id="cputable"]').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
    name = data[1].find_elements_by_tag_name('td')[0].text
    print(data[0])
    print("[getPerfil.py] Nome : " + name)
    

    print("---------------------------END GETPERFIL-----------------------------")
    print()
    return data
