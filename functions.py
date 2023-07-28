import webbrowser
import pandas as pd
import pyautogui as pg
import time

def open_webpage(url):
    webbrowser.open(url)
    return True

def sendMsg(msg, num):
    open_webpage("https://api.whatsapp.com/send?phone=91"+num+"&text="+((str(msg)).replace('\\n', '%0A')))

    time.sleep(2)
    print("Sending message to "+num+"...")
    pg.press('enter')
    print("Message sent to "+num+"!")

    return True

def sendImg(imgpath, msg, num):
    open_webpage("https://api.whatsapp.com/send?phone=91"+num+"&text="+msg)
    time.sleep(5)
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('shift', 'tab')
    pg.hotkey('enter')
    pg.hotkey('enter')
    time.sleep(3)
    pg.typewrite(imgpath)
    time.sleep(2)
    pg.hotkey('enter')
    time.sleep(1)
    pg.hotkey('enter')

    return True

def sendMsgs_excel(infile):
    df = pd.read_excel(infile)
    for i in range(len(df)):
        num = str(df.iloc[i,0])
        msg = str(df.iloc[i,1])
        sendMsg(msg, num)
        time.sleep(1)
    pg.hotkey('alt', 'tab')
    for i in range(len(df)):
        pg.hotkey('ctrl', 'w')
    return True

if __name__ == "__main__":
    # path = 'C:\\Users\\Prasanna\\Pictures\\QuEd.jpg'
    # sendImg(path, 'automated bulk image', '9930147179')
    pass
