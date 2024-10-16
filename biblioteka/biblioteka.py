import pickle
from datetime import datetime

class Knyga:
    def __init__(self, knygos_atributai):
        self.autorius = knygos_atributai["autorius"]
        self.pavadinimas = knygos_atributai["pavadinimas"]
        self.isleidimo_metai=knygos_atributai["isleidimo_metai"]
        self.zanras = knygos_atributai["zanras"]
        self.kiekis = knygos_atributai["kiekis"]
    def grazinti_atributus(self):

        self.atributai={
            "autorius":self.autorius, 
            "pavadinimas":self.pavadinimas,
            "isleidimo_metai":self.isleidimo_metai,
            "zanras":self.zanras,
            "kiekis":self.kiekis
        }
        return self.atributai
        

    def __repr__(self):
        return f"Knyga('{self.autorius}', '{self.pavadinimas}', {self.isleidimo_metai}, '{self.zanras}', {self.kiekis})"
    
class   Pasiskolinta_knyga(Knyga):
    def __init__(self, grazinimo_data, pasiskolinimo_data, kiekis, knygos_atributai):
        super().__init__(knygos_atributai)
        self.grazinimo_data=grazinimo_data
        self.pasiskolinimo_data=pasiskolinimo_data
        self.kiekis=kiekis
    def __repr__(self):
        return f"Knyga('{self.autorius}', '{self.pavadinimas}', '{self.isleidimo_metai}',  '{self.kiekis}', '{self.pasiskolinimo_data}', '{self.grazinimo_data}')"  
    
class Biblioteka:
    def __init__(self):
        self.knygos = []
        self.korteles=[]



    def prideti_kortele(self, nauja_kortele):
        jau_egzistuoja=False
        for kortele in self.korteles: 
            if nauja_kortele.id== kortele.id:
                print(f"kortele su id {kortele.id} jau egzistuoja")
                jau_egzistuoja=True
                break
        if not jau_egzistuoja:
            self.korteles.append(nauja_kortele)
            print(f"kortele {nauja_kortele.id} iterpta")
        return not jau_egzistuoja
    

    def atidaryti_biblioteka(self, failo_pavadinimas = "pirmas.pcl"):
        with open(failo_pavadinimas, 'rb') as failas:
            self=pickle.load(failas)
        print(f"biblioteka atidaryta is failo '{failo_pavadinimas}'.")
        return self

        
    def prideti_knyga(self, nauja_knyga): 

        self.knygos.append(nauja_knyga)
        print(f"Knyga '{nauja_knyga.pavadinimas}' pridėta į biblioteką.")

    def visos_knygos(self):
        if not self.knygos:
            print("knygu nera")
        else:
            print("\n visos bibliotekos knygos:")
            for knyga in self.knygos:
                print(knyga)

    def issaugoti_biblioteka(self, failo_pavadinimas = "pirmas.pcl"):
        with open(failo_pavadinimas, 'wb') as failas:
            pickle.dump(self, failas)
        print(f"Knygos išsaugotos faile '{failo_pavadinimas}'.")

    def pasalinti_knyga(self, knyga):
        self.knygos.remove(knyga)

    def pasiskolinti_knyga(self, pavadinimas, korteles_id, grazinimo_diena):
        pasiskolinta=False
        kortele_rasta=False
        for knyga in self.knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                if knyga.kiekis > 0:
                    for kortele in self.korteles:
                        if kortele.id==korteles_id:
                            kortele_rasta=True
                            pasiskolinimo_diena=str(datetime.now().date())
                            pasiskolinta_knyga=Pasiskolinta_knyga(grazinimo_diena, pasiskolinimo_diena, 1, knyga.grazinti_atributus())
                            pasiskolinta=kortele.pasiskolinti_knyga(pasiskolinta_knyga)
                            break
                    if pasiskolinta:
                        knyga.kiekis-=1 
                        print(f"Knyga '{pavadinimas}' pasiimta išsinešimui.")
                        return
                    else: 
                        print(f"knyga {pavadinimas} vartotojui {korteles_id} neisnuomota")
                        if not kortele_rasta: 
                            print(f"kortele {korteles_id} nerasta")
                        return
                else:
                    print(f"Knyga '{pavadinimas}' knygos neprieinama")
                    return
        print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

    def ieskoti_pagal_pavadinima(self, pavadinimas):
        rezultatai = [knyga for knyga in self.knygos if pavadinimas.lower() in knyga.pavadinimas.lower()]
        if rezultatai:
            print("Rastos knygos pagal pavadinimą:")
            for knyga in rezultatai:
                print(knyga)
        else:
            print(f'Knygų su pavadinimu "{pavadinimas}" nerasta.')

    def ieskoti_pagal_autoriu(self, autorius):
        rezultatai = [knyga for knyga in self.knygos if autorius.lower() in knyga.autorius.lower()]
        if rezultatai:
            print("Rastos knygos pagal autorių:")
            for knyga in rezultatai:
                print(knyga)
        else:
            print(f'Knygų autoriaus "{autorius}" nerasta.')
    
    def perziureti_korteles(self): 
        print("viduje esancios korteles:")
        for kortele in self.korteles:
            print(kortele)
    
    def grazinti_knyga(self, grazinama_knyga):
        for knyga in self.knygos:
            if knyga.grazinti_atributus()==grazinama_knyga.grazinti_atributus():
                knyga.kiekis+=1