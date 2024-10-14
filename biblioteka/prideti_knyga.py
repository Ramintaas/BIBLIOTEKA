import pickle
from datetime import datetime

class Knyga:
    def __init__(self, autorius, pavadinimas, isleidimo_metai, zanras):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.isleidimo_metai=isleidimo_metai
        self.zanras = zanras
        

    def __repr__(self):
        return f"Knyga('{self.autorius}', '{self.pavadinimas}', {self.isleidimo_metai}, '{self.zanras}')"
    
class Biblioteka:
    def __init__(self):
        self.knygos = []
        
    def prideti_knyga(self):
        autorius = input("Įveskite autoriaus vardą: ")
        pavadinimas = input("Įveskite knygos pavadinimą: ")
        isleidimo_metai = int(input("Įveskite išleidimo metus: "))
        zanras = input("Įveskite žanrą: ")

        nauja_knyga = Knyga(autorius, pavadinimas, isleidimo_metai, zanras)
        self.knygos.append(nauja_knyga)
        print(f"Knyga '{nauja_knyga.pavadinimas}' pridėta į biblioteką.")

    def visos_knygos(self):
        if not self.knygos:
            print("knygu nera")
        else:
            print("\n visos bibliotekos knygos:")
            for knyga in self.knygos:
                print(knyga)

    def issaugoti_knygas(self, failo_pavadinimas):
        with open(failo_pavadinimas, 'wb') as failas:
            pickle.dump(self.knygos, failas)
        print(f"Knygos išsaugotos faile '{failo_pavadinimas}'.")

mano_biblioteka=Biblioteka()

mano_biblioteka.prideti_knyga("Mazasis Princas", "Exiuperi", 1943, "Romanas")
mano_biblioteka.prideti_knyga("Haris Poteris", "J.K.Rowling", 2011, "Romanas")

mano_biblioteka.visos_knygos()





