import webbrowser
import pandas as pd

def open_webpage(url):
    webbrowser.open(url)
    return True

def sendMsg(msg, num):
    open_webpage("https://api.whatsapp.com/send?phone="+num+"&text="+msg)
    return True

def sendMsgs_excel(infile):
    df = pd.read_excel(infile)
    for i in range(len(df)):
        num = str(df.iloc[i,0])
        msg = str(df.iloc[i,1])
        sendMsg(msg, num)
    return True
