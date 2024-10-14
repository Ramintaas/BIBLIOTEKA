from datetime import datetime
from prideti_knyga import Biblioteka

def pasiimti_nauja(skaitytos_knygos):
    veluojancios_knygos = gauti_veluojancias_knygas(skaitytos_knygos)
    
    if veluojancios_knygos:
        print("Negalite pasiimti naujos knygos, nes turite veluojanciu knygų:")
        for knyga in veluojancios_knygos:
            print(f"- {knyga['title']} (grąžinimo data: {knyga['grazinimo_data']}, terminas: {knyga['nustatyta_data']})")
        return False
    else:
        print("Galite pasiimti naują knyga.")
        return True


skaitytos_knygos = [
    {'title': 'Knyga A', 'isdavimo_data': '2024-09-15', 'grazinimo_data': '2024-09-24', 'nustatyta data': '2024-10-10'}, # Skaitytojo turimos knygos (pvz)
    {'title': 'Knyga B', 'isdavimo_data': '2024-09-20', 'grazinimo_data': '2024-10-05', 'nustatyta data': '2024-10-15'},
    {'title': 'Knyga C', 'isdavimo_data': '2024-09-25', 'grazinimo_data': '2024-10-13', 'nustatyta data': '2024-10-10'}
]


gali_pasiimti = pasiimti_nauja(skaitytos_knygos) # patikrinti ar galima pasiimti knyga. 

if gali_pasiimti:
    print("Naują knyga galima pridėti į sarasa.")
else:
    print("Reikia grazinti senas knygas, tada pasiimti nauja")