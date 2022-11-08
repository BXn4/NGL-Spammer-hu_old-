import time
import requests
import os
from random import *
from colorama import Fore, Back, Style
from datetime import datetime

#.txt fájl beolvasás, és a tartalmának eltárolása
print("A txt fájl beolvasása, kérlek várj!")
try:
    kerdesek = []
    with open('kerdesek.txt', 'r', encoding="UTF-8") as kerdesolvas:
        sorok = kerdesolvas.readline()
        while sorok:
            kerdesek.append(sorok)
            sorok = kerdesolvas.readline()
        os.system('cls')
        
except (FileNotFoundError):
    print("Nem található a fájl!")

    
request = requests.Session()
ngl_nev = input("NGL név: ")
i = 0
datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print(Fore.YELLOW + "[{}]".format(ido)+ Fore.WHITE + " >> Kezdés\n")
while(True):
    if(i < 15):
        time.sleep(1)
        kerdes = (choice(kerdesek))
        url = f"https://ngl.link/{ngl_nev}"
        fej = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        adat = {
            "question": kerdes
            }
        print(Fore.BLUE + "[Kérdés] " + Fore.WHITE + "{}".format(kerdes))
        elkuld = request.post(url, headers=fej, data=adat)
        i = i+1
    if(i == 15):
        datum = datetime.now()
        ido = datum.strftime("%H:%M:%S")
        print(Fore.GREEN + "[{}]".format(ido) + Fore.WHITE +" >> Szünet (2 perc)\n")
        time.sleep(120)
        i = 0
