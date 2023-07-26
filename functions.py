import webbrowser
import pandas as pd
import pyautogui as pg
import time

def open_webpage(url):
    webbrowser.open(url)
    return True

def sendMsg(msg, num):
    open_webpage("https://api.whatsapp.com/send?phone=91"+num+"&text="+msg)
    time.sleep(2)
    pg.hotkey('enter')

    return True

def sendMsgs_excel(infile):
    df = pd.read_excel(infile)
    for i in range(len(df)):
        num = str(df.iloc[i,0])
        msg = str(df.iloc[i,1])
        sendMsg(msg, num)
    pg.hotkey('alt', 'tab')
    for i in range(len(df)):
        pg.hotkey('ctrl', 'w')
    return True
