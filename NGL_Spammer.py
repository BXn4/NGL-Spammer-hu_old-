import time
import requests
from random import *
from datetime import datetime
import string
import uuid

fiokokszama = 0
jelenlegi = 0
mennyitkuldott = []
kerdesek = []
fiokok = []
fiok = ""
eszkozid = ""

def eszkozidgeneralas():
    eszkozid = uuid.uuid4().hex
    return "-".join([eszkozid[i:i+8] for i in range(0, 32, 8)])
eszkozidgeneralas()
eszkozid = eszkozidgeneralas()

try:
    with open("kerdesek.txt", "r", encoding="UTF-8") as kerdesekolvas:
        kerdesek = [sorok.strip() for sorok in kerdesekolvas]
    with open("fiokok.txt", "r") as fiokokolvas:
        fiokok = [sorok.strip() for sorok in fiokokolvas]
    mennyitkuldott = [0 for _ in range(len(fiokok))]
    fiokokszama = len(fiokok)

except (FileNotFoundError):
  print("Nem található a fájl!")

request = requests.Session()
i = 0
datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("\n[{}] >> Kezdés\n".format(ido))

while True:
  if (i < 2):
    time.sleep(1)
    fiok = fiokok[jelenlegi].strip()
    kerdes = (choice(kerdesek))
    url = f"https://ngl.link/{fiok}"

    fejresz = {
      "Referer": url,
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }
    
    adat = {
    "username": fiok,
    "question": kerdes,
    "deviceId": eszkozid
    }
    mennyitkuldott[jelenlegi] += 1
    print("-> %s (%s) \n[Kérdés] %s" % (fiok,mennyitkuldott[jelenlegi],kerdes) + "\n")
    elkuld = request.post("https://ngl.link/api/submit", headers=fejresz, data=adat)
    #print(elkuld) (Tesztelés)
    i = i + 1

  if (i == 2):
    eszkozidgeneralas()
    print("Következő: -> " + fiokok[jelenlegi + 1])
    jelenlegi += 1
    if jelenlegi == fiokokszama:
      jelenlegi = 0
    datum = datetime.now()
    ido = datum.strftime("%H:%M:%S")
    print("[{}] >> Szünet (2 perc)\n".format(ido))
    time.sleep(120)
    i = 0
