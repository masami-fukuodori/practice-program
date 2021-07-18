from selenium import webdriver
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import urllib
import openpyxl
import datetime
import re
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import os
import math
from selenium.webdriver.support.ui import Select
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import messagebox as mb

mercari = 'https://www.mercari.com/jp/'

yahoku = 'https://auctions.yahoo.co.jp/'

surugaya = 'https://www.suruga-ya.jp/'

amazon = 'https://www.amazon.co.jp/'

site_list = [mercari,yahoku,surugaya,amazon]
def to_mercari():
    browser.get(mercari)
    time.sleep(1)
    elem = browser.find_element_by_class_name('sc-GMQeP.cuephK')
    elem.clear()
    elem.send_keys(keyword)
    elem = browser.find_element_by_class_name('sc-exAgwC.bdHDSo')
    elem.click()

def to_yahoku():
    browser.get(yahoku)
    time.sleep(1)
    try:
        elem = browser.find_element_by_name('Close-sc-1nsnvko.eRhJtN')
        elem.click()
    except Exception as ex:
        pass
    elem = browser.find_element_by_xpath('//*[@id="sbn"]/div/div[1]/div/input')
    elem.send_keys(keyword)
    elem = browser.find_element_by_id('acHdSchBtn')
    elem.click()

def to_surugaya():
    browser.get(site_list[2])
    time.sleep(1)
    elem = browser.find_element_by_name('search_word')
    elem.send_keys(keyword)
    elem = browser.find_element_by_id('btn-search')
    elem.click()

def to_amazon():
    browser.get(site_list[3])
    time.sleep(1)
    elem = browser.find_element_by_id('twotabsearchtextbox')
    elem.send_keys(keyword)
    elem = browser.find_element_by_id('nav-search-submit-button')
    elem.click()
    
def browser_open():
    try:
        browser.switch_to.window(browser.window_handles[tab])
    except Exception as ex:
        browser.execute_script("window.open('','_blank');")
        browser.switch_to.window(browser.window_handles[tab])

def search_keyword():
    global en_text
    en_text = en.get()
    global keyword
    global tab
    keyword = en_text
    tab = 0
    browser_open()
    to_mercari()
    tab += 1
    try:
        browser_open()
        to_yahoku()
    except Exception as ex:
        pass
    tab += 1
    browser_open()
    to_surugaya()
    tab += 1
    browser_open()
    to_amazon()

ua = UserAgent()
useragent = ua.random
headers = {"User-Agent":useragent}
browser = webdriver.Chrome()
#browser = webdriver.Chrome(executable_path='C:/Users/m2153/OneDrive/デスクトップ/プログラミング/chromedriver.exe')#,options=options

root = Tk()
root.title('sample')
root.attributes("-topmost", True)
root.geometry("200x100")
lb = Label(text='search')
lb.pack()
en = Entry()
en.pack()
bt = Button(text='search',command=search_keyword)
bt.pack()
root.mainloop()