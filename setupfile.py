import os
import shutil 
os.system("pip install -r requirements.txt")
os.system("pyinstaller --onefile --windowed gui.py")
shutil.move("dist/gst_gui.exe", "AutoWhatsApp.exe")