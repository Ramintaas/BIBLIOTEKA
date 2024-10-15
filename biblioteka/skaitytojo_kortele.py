from datetime import datetime
from biblioteka import Biblioteka, Knyga


class Skaitytojo_kortele:
    def __init__(self, kortelesid):
        self.id = kortelesid
        self.priskirtas_naudotojas = None
        self.pasiskolintos_knygos = []

    def __repr__(self):
        return f"id:{self.id},vardas: {self.priskirtas_naudotojas}, pasiskolintos knygos: {self.pasiskolintos_knygos}"

        
    def naudotojas(self, vartotojas):
        self.priskirtas_naudotojas = vartotojas
        print(f"Kortele {self.id} priskirta naudotojui {vartotojas.vardas}")

    def velavimo_patikrinimas(self):
        
        veluojancios_knygos = []
        today = datetime.now().date()

        for knyga in self.pasiskolintos_knygos:
            grazinimo_data = datetime.strptime(knyga.grazinimo_data, "%Y-%m-%d").date()
            if grazinimo_data < today:
                veluojancios_knygos.append(knyga)

        return veluojancios_knygos
    def pasiskolinti_knyga(self, knyga):
        veluojancios_knygos=self.velavimo_patikrinimas()
        if veluojancios_knygos:
            print("pasiskolinti knygos negalima, nes veluojame grazinti sias knygas: ")
            for knyga in veluojancios_knygos:
                print(knyga)
            return False
        else : 
            self.pasiskolintos_knygos.append(knyga)
            return True

    def grazinti_knyga(self, knyga):
        grazinta=False
        for pasiskolinta_knyga in self.pasiskolintos_knygos:
            if pasiskolinta_knyga.grazinti_atributus()==knyga.grazinti_atributus():
                self.pasiskolintos_knygos.remove(pasiskolinta_knyga)
                print(f"knyga {self.pavadinimas} grazinta")
                grazinta=True
        if not grazinta:
            print(f"{self.priskirtas_naudotojas} knygos {knyga.pavadinimas} nepasiskolino")
        
 
class Naudotojas:
    def __init__(self, vardas):
        self.vardas = vardas
        self.kortele = None

    def registruota_kortele(self, kortele):
        if self.kortele is None:
            kortele.naudotojas(self)
            self.kortele = kortele
           
        else:
            print(f"Naudotojas {self.vardas} jau turi kortele")
    def __repr__(self) -> str:
        return f"{self.vardas}"



if __name__=="__main__":

    mano_biblioteka=Biblioteka().atidaryti_biblioteka()
    kortele = Skaitytojo_kortele(kortelesid="5555")  
    naudotojas = Naudotojas(vardas="Tomas")  

    naudotojas.registruota_kortele(kortele) # Priskiriame kortele naudotojui
    mano_biblioteka.prideti_kortele(kortele)
    mano_biblioteka.issaugoti_biblioteka()
    mano_biblioteka.perziureti_korteles()
   

