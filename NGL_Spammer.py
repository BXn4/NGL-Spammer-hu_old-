import time
import requests
import os
from random import *
from datetime import datetime

global sorok
sorokx = 0
global cel
cel = []
global mennyiszer
mennyiszer = 0
with open("fiokok.txt", "r") as file:
    for line in file:
        # Do something with the line
        cel.append(line)
        sorokx += 1

#.txt fájl beolvasás, és a tartalmának eltárolása
try:
    kerdesek = []
    with open('kerdesek.txt', 'r', encoding="UTF-8") as kerdesolvas:
        sorok = kerdesolvas.readline()
        while sorok:
            kerdesek.append(sorok)
            sorok = kerdesolvas.readline()
        
except (FileNotFoundError):
    print("Nem található a fájl!")

    
request = requests.Session()
i = 0
datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("\n[{}] >> Kezdés\n".format(ido))
global jsor
jsor = 0
while(True):
    if(i < 15):
        time.sleep(1)
        kerdes = (choice(kerdesek))
        url = f"https://ngl.link/{cel[jsor]}"
        fej = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        adat = {
            "question": kerdes
            }
        print("[Kérdés] {}".format(kerdes))
        elkuld = request.post(url, headers=fej, data=adat)
        i = i+1
    if(i == 15):
        datum = datetime.now()
        ido = datum.strftime("%H:%M:%S")
        print("[{}] >> Szünet (2 perc)\n".format(ido))
        time.sleep(120)
        i = 0
        jsor += 1
        if jsor == sorokx:
            jsor = 0
            mennyiszer += 1
            print(mennyiszer)
