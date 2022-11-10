from tkinter import *
import requests

def nevellenorzes():
    nglNev = nevInput.get("1.0",END)
    nevHossz = len(nglNev)
    if(nevHossz == 1):
        print("Üres!")
    else:
        url = 'https://ngl.link/{nglNev})'
        valasz = (requests.get(url))
        if valasz.status_code == 200:
            print("van ilyen fiók")
        else:
            print("nincs ilyen fiók, vagy várj egy kicsit")
ablak = Tk()
ablak.title("NGL Spammer GUI")
ablak.configure(width=300, height=300)
ablak.resizable(False, False)
nevLbl = Label(ablak, text='NGL Név:')
nevLbl.place(x=10,y=10)
nevInput = Text(width=15, height=1)
nevInput.place(x=70, y=10)
nevGomb = Button(ablak, text="Ellenőrzés", command=nevellenorzes)
nevGomb.place(x=200, y=10)

ablak.mainloop()
