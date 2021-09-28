import stat
import threading
import subprocess
import time
import wget
import zipfile
import platform
import os
def checkng():
    os_name = platform.system()
    if (os_name == 'Linux'):
        print('Please wait ngrok is being installed!!')
        r = wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip')
        with zipfile.ZipFile('ngrok-stable-linux-amd64.zip', 'r') as zip_ref:
            zip_ref.extractall()
            os.chmod('ngrok', stat.S_IXOTH)
    else:
        print("This tool works on linux for time being!!")
def start_php():
    suprocess = subprocess.Popen("php -S 127.0.0.1:80 ", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    suprocess_re = suprocess.stdout.read()
    print(suprocess_re)


def start(choice):
    os.chdir("sites/" + choice)
    t1 = threading.Thread(target=start_php())
    t1.start()
