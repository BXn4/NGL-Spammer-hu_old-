import time
import requests
from random import *
from datetime import datetime
import uuid

fiokokszama = 0
jelenlegi = 0
i = 0
mennyitkuldott = []
kerdesek = []
fiokok = []
neverhave = []
haromwords = []
nevek = []
tbh = []
kissmarryblocklist = []
tizperde = []
fiok = ""
eszkozid = ""
szavak = ""
mit = ""
gameslugkuld = ""
request = requests.Session()

def eszkozidgeneralas():
    eszkozid = uuid.uuid4().hex
    return "-".join([eszkozid[i:i+8] for i in range(0, 32, 8)])

def haromnevgeneralas():
  for k in range(3):
    szavak = (choice(nevek))
    kissmarryblocklist.append(szavak.replace('\n', ''))

eszkozidgeneralas()
eszkozid = eszkozidgeneralas()

try:
    with open("szovegek/kerdesek.txt", "r", encoding="UTF-8") as olvas:
        kerdesek = [sorok.strip() for sorok in olvas]
    with open("szovegek/neverhave.txt", "r", encoding="UTF-8") as olvas:
        neverhave = [sorok.strip() for sorok in olvas]
    with open("szovegek/3words.txt", "r", encoding="UTF-8") as olvas:
        haromwords = [sorok.strip() for sorok in olvas]
    with open("szovegek/nevek.txt", "r", encoding="UTF-8") as olvas:
        nevek = [sorok.strip() for sorok in olvas]
    with open("szovegek/tbh.txt", "r", encoding="UTF-8") as olvas:
        tbh = [sorok.strip() for sorok in olvas]
    with open("szovegek/dealbreaker.txt", "r", encoding="UTF-8") as olvas:
        tizperde = [sorok.strip() for sorok in olvas]
    with open("fiokok.txt", "r") as olvas:
        fiokok = [sorok.strip() for sorok in olvas]
    mennyitkuldott = [0 for _ in range(len(fiokok))]
    fiokokszama = len(fiokok)

except (FileNotFoundError):
  print("Nem található a fájl!")

datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("\n[{}] >> Kezdés\n".format(ido))

while True:
  if (i < 10):
    time.sleep(1)
    fiok = fiokok[jelenlegi].strip()
    if '/' in fiok:
      if "neverhave" in fiok:
        fiok = fiok.split("/")[0]
        mit = "Neverhave"
        gameslugkuld = "neverhave"
        szavak = ("Én még sohasem " + choice(neverhave))
        neverHave = szavak.replace('\n', '')
        kerdes = neverHave
        szavak = ""
      if "crush" in fiok:
        fiok = fiok.split("/")[0]
        mit = "Crush"
        gameslugkuld = "yourcrush"
        szavak += (choice(nevek))
        crush = szavak.replace('\n', '')
        kerdes = crush
        szavak = ""
      if "shipme" in fiok:
        fiok = fiok.split("/")[0]
        mit = "Shipme"
        gameslugkuld = "shipme"
        szavak += (choice(nevek))
        shipme = szavak.replace('\n', '')
        kerdes = shipme
        szavak = ""
      if "tbh" in fiok:
        fiok = fiok.split("/")[0]
        mit = "TBH"
        gameslugkuld = "tbh"
        szavak = choice(tbh)
        tbhKuld = szavak.replace('\n', '')
        kerdes = tbhKuld
        szavak = ""
      if "dealbreaker" in fiok:
        fiok = fiok.split("/")[0]
        mit = "10/10"
        gameslugkuld = "dealbreaker"
        szavak = choice(tizperde)
        tizperdeKuld = szavak.replace('\n', '')
        kerdes = tizperdeKuld
        szavak = ""
      if "kissmarryblock" in fiok:
        fiok = fiok.split("/")[0]
        haromnevgeneralas()
        if any(kissmarryblocklist.count(i) > 1 for i in kissmarryblocklist):
          haromnevgeneralas() 
        else:
          mit = "KMB"
          gameslugkuld = "kissmarryblock"
          for k in range(3):
            if k == 2:
              szavak += f"{kissmarryblocklist[k]}"
            else:
              szavak += f"{kissmarryblocklist[k]}, "
          kerdes = szavak
          kissmarryblocklist = []
          szavak = ""
          haromnevgeneralas()
      if "3words" in fiok:
        gameslugkuld = "3words"
        fiok = fiok.split("/")[0]
        mit = "3 Words"
        szavak += (choice(haromwords) + ", " + choice(haromwords) + ", " + choice(haromwords))
        haromszo = szavak.replace('\n', '')
        kerdes = haromszo
        szavak = ""
    else:
      mit = "Kérdés"
      kerdes = choice(kerdesek)
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
    "deviceId": eszkozid,
    "gameSlug": gameslugkuld,
    "referrer": ""
    }
    mennyitkuldott[jelenlegi] += 1
    print("-> %s (%s) \n[%s] %s" % (fiokok[jelenlegi],mennyitkuldott[jelenlegi],mit,kerdes) + "\n")
    elkuld = request.post("https://ngl.link/api/submit", headers=fejresz, data=adat)
    i = i + 1

  if (i == 10):
    eszkozidgeneralas()
    jelenlegi += 1
    if jelenlegi == fiokokszama:
      jelenlegi = 0
    datum = datetime.now()
    print("Következő: -> " + fiokok[jelenlegi])
    ido = datum.strftime("%H:%M:%S")
    print("[{}] >> Szünet (2 perc)\n".format(ido))
    time.sleep(120)
    i = 0
