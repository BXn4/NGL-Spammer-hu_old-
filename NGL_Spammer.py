import time
import requests
from random import *
from datetime import datetime

fiokoksora = 0
jelenlegi = 0
mennyitkuldott = []
fiok = ""

try:
  kerdesek = []
  fiokok = []
  with open("kerdesek.txt", "r", encoding="UTF-8") as kerdesolvas:
    sorok = kerdesolvas.readline()
    while sorok:
      kerdesek.append(sorok)
      sorok = kerdesolvas.readline()
  with open("fiokok.txt", "r") as file:
    for line in file:
        fiokok.append(line)
        mennyitkuldott.append(0)
        fiokoksora += 1

except (FileNotFoundError):
  print("Nem található a fájl!")

request = requests.Session()
i = 0
datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("\n[{}] >> Kezdés\n".format(ido))

while (True):
  if (i < 10):
    time.sleep(1)
    fiok = fiokok[jelenlegi].strip()
    kerdes = (choice(kerdesek))
    url = f"https://ngl.link/{fiok}"

    fejresz = {
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    adat = {"question": kerdes}
    mennyitkuldott[jelenlegi] += 1
    print("-> %s (%s) \n[Kérdés] %s" % (fiok,mennyitkuldott[jelenlegi],kerdes))
    elkuld = request.post(url, headers=fejresz, data=adat)
    i = i + 1

  if (i == 10):

    print(fiokok[jelenlegi])
    jelenlegi += 1

    if jelenlegi == fiokoksora:
      jelenlegi = 0

    datum = datetime.now()
    ido = datum.strftime("%H:%M:%S")
    print("[{}] >> Szünet (2 perc)\n".format(ido))
    time.sleep(120)
    i = 0
