from datetime import datetime
from prideti_knyga import Biblioteka

def veluojancios_knygos(knygos):
    veluojancios_knygos = []
    today = datetime.now().date()

    for knyga in knygos:
        grazinimo_data = datetime.strptime(knyga["grazinimo data"], "%Y-%m-%d").date()
        if grazinimo_data < today:
            veluojancios_knygos.append(knyga["title"])

    return veluojancios_knygos


pavelavimas = rasti_veluojancias_knygas(veluojancios_knygos) # Iskviečiame funkciją
if pavelavimas:
    print("Vėluojančios knygos:", pavelavimas)
else:
    print("Nėra vėluojančių knygų")

