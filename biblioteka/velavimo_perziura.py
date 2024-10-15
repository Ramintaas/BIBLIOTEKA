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

knygos = [
    {"title": "knyga 1", "grazinimo data": "2024-10-11"},  # knygu pavyzdys, sarasas
    {"title": "knyga 2", "grazinimo data": "2024-09-12"},
    {"title": "knyga 3", "grazinimo data": "2024-10-15"}
]


pavelavimas = veluojancios_knygos(knygos) # Iskviečiame funkciją
if pavelavimas:
    print("Vėluojančios knygos:", pavelavimas)
else:
    print("Nėra vėluojančių knygų")

