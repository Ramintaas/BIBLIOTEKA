from datetime import datetime
from prideti_knyga import Biblioteka

def veluojanti(isdavimo_data_str, grazinimo_data_str, numatyta_data_str):
    isdavimo_data = datetime.strptime(isdavimo_data_str, '%Y-%m-%d')
    grazinimo_data = datetime.strptime(grazinimo_data_str, '%Y-%m-%d')
    numatyta_data = datetime.strptime(numatyta_data_str, '%Y-%m-%d')

    if grazinimo_data > numatyta_data:
        return True, (grazinimo_data - numatyta_data).days  # Graziname vėlavimo dienas
    else:
        return False, 0
    

isdavimo_data = '2024-10-01'
grazinimo_data = '2024-10-14'
numatyta_data = '2024-10-10'

velavimas, pavelavimo_dienos = jei_velavimas(isdavimo_data, grazinimo_data, numatyta_data)

if velavimas:
    print(f"Knyga veluoja {pavelavimo_dienos} dienomis.")
else:
    print("Knyga nėra veluojanti.")

def issaugoti_veluojancias(self, failo_pavadinimas):
        with open(failo_pavadinimas, 'wb') as failas:
            pickle.dump(self.knygos, failas)
        print(f"Knygos išsaugotos faile '{failo_pavadinimas}'.")

