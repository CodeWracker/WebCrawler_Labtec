# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

'''
    Não consegui fazer usando o beautifulsoup
'''
def logIn(url):
    print('')
    print("Opening: "+ url)
    print('')

    '''
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    '''
    driver = webdriver.Firefox()

    driver.get(url)
    #print(driver)
    
    print('')
    print("-END CONFIG-")
    print('')
    return driver