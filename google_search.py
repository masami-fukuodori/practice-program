from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as bs
import datetime
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from IPython.display import display
import PySimpleGUI as sg

#ブラウザを立ち上げる関数
def start_browser():
    ua = UserAgent()
    useragent = ua.random
    headers = {"User-Agent":useragent}
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser

#グーグルの検索窓に入力→検索する関数
def google_search(browser, keyword):
    browser.get("https://google.com/")
    time.sleep(2)
    browser_from = browser.find_element_by_class_name('gLFyf.gsfi')
    browser_from.send_keys(keyword)
    browser_from.send_keys(Keys.ENTER)
    time.sleep(2)

#GUIを立ち上げる関数
def show_window():

    #色テーマの指定
    sg.theme('DarkAmber')
    
    #レイアウト指定
    layout = [
        [sg.Text('Google Search App')],
        [sg.Text('ワード入力：', size=(15,1)), sg.InputText('')],
        [sg.Button('Start Browser', key='-browser-', size=(15,1))],
        [sg.Button('Search', key='-search-', size=(15,1))]
    ]

    #表示
    win = sg.Window('Google Search App', layout=layout, location=(0,0), keep_on_top=True, return_keyboard_events=True)
    #keep_on_top=True→ウインドウが一番上にくる。return_keyboard_events→キーボード入力が有効　参照https://qiita.com/melka-blue/items/33c89a62c2392bbbd450
    
    # イベントループ
    while True:
        event, values = win.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-browser-':
            browser = start_browser()

        elif event == '-search-' or event == '\r':
            keyword = values[0]

            try:
                google_search(browser, keyword)
            except:
                sg.popup('please start browser.', keep_on_top=True)
    browser.close()

#mainの処理

if __name__ == '__main__':
    show_window()
