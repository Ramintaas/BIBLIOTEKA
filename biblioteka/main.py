from datetime import datetime
from biblioteka import Biblioteka, Knyga
from skaitytojo_kortele import Skaitytojo_kortele, Naudotojas
from pasalinti_knyga import pasalinti_knyga

def pasirinkimo_meniu():
    print("Bibliotekos valdymo sistemos meniu:")
    print("1. Atspausdinti knygu sarasa")
    print("2. Ieskoti knygos pagal pavadinima ir autoriu")
    print("3. Registruoti naudotoja")
    print("4. Pasiskolinti knyga")
    print("5. Grazinti knyga")
    print("6. Pridėti nauja knyga į biblioteką")
    print("7. Pašalinti knyga iš bibliotekos")
    print("8. Perziureti veluojancias knygas")
    print("9. Perziureti visas pasiskolintas knygas")
    print("0. Exit")

def atspausdinti_knygu_sarasa(biblioteka):
    biblioteka.visos_knygos()
    input("spausti enter, kad grizti i pradini meniu")

def ieskoti_knygos(mano_biblioteka):
    while True:
        ieskau=input("\nPasirinkite ieskoti pagal:\n1. autoriu\n2. pavadinima \n3. grizti atgal\n")
        if ieskau == "1":
            autorius= input("Iveskite autoriu: ")
            mano_biblioteka.ieskoti_pagal_autoriu(autorius)
        elif ieskau == "2":
            pavadinimas= input("Iveskite knygos pavadinima: 2")
            mano_biblioteka.ieskoti_pagal_pavadinima(pavadinimas)
        elif ieskau == "3":
            return
        else: 
            print("neteisingai ivestas meniu punktas. Bandykite dar karta")
        
            
def registruoti_naudotoja(biblioteka):
    vardas = input("Ivesti naudotojo varda: ")
    naudotojas = Naudotojas(vardas=vardas)
    id=input("Iveskite korteles ID: ")
    kortele = Skaitytojo_kortele(kortelesid=id)  
    naudotojas.registruota_kortele(kortele)
    prideta=biblioteka.prideti_kortele(kortele)
    if prideta: 
        biblioteka.issaugoti_biblioteka()
        input("spausti enter, kad grizti i pradini meniu")
    else:
        sprendimas=input ("Prideti korteles nepavyko, spausti:\n1. grizti atgal \n2. bandyti dar karta\n")
        if sprendimas == "2":
            registruoti_naudotoja(biblioteka)
        else:
            return   

def pasiimti_knyga_namo(mano_biblioteka):
    knygos_pavadinimas = input("Ivesti norimos pasiskolinti knygos pavadinima: ")
    ivesti_id=input("Iveskite korteles ID: ")
    ivesti_grazinimo_data=input("Iveskite grazinimo data: ")
    mano_biblioteka.pasiskolinti_knyga(knygos_pavadinimas, ivesti_id, ivesti_grazinimo_data)
    mano_biblioteka.issaugoti_biblioteka()
    input("spausti enter, kad grizti i pradini meniu")
 


def parnesti_knyga(mano_biblioteka): #grazinti knygas
    kortele_rasta=False
    vartotojo_id=input("iveskite vartotojo ID: ")
    for kortele in mano_biblioteka.korteles:
        if kortele.id == vartotojo_id:
            kortele_rasta=True
            print("pasiskolintos_knygos: ")
            for knyga in kortele.pasiskolintos_knygos:
                print(knyga)
            knygos_pavadinimas = input("Ivesti grazinamos knygos pavadinima: ")
            for knyga in kortele.pasiskolintos_knygos:
                if knyga.pavadinimas.lower()==knygos_pavadinimas.lower():
                    kortele.grazinti_knyga(knyga)
                    mano_biblioteka.issaugoti_biblioteka()

    if not kortele_rasta:
        print(f"vartotojo kortele su ID {vartotojo_id} nerasta")
    input("spausti enter, kad grizti i pradini meniu")

    
def prideti_knyga_i_biblioteka(mano_biblioteka):
    pavadinimas=input("Iveskite knygos pavadinima: ")
    autorius=input("iveskite autoriu: ")
    metai= input("Iveskite isleidimo metus: ")
    zanras= input("iveskite knygos zanra: ")
    kiekis= input("Iveskite knygu kiekis: ")
    mano_biblioteka.prideti_knyga(Knyga({"pavadinimas":pavadinimas, "autorius":autorius, "isleidimo_metai":metai, "zanras":zanras,"kiekis":kiekis}))

    mano_biblioteka.issaugoti_biblioteka()
    input("spausti enter, kad grizti i pradini meniu")

def perziureti_pasiskolintas_knygas(mano_biblioteka): 
    kortele_rasta=False
    vartotojo_id=input("iveskite vartotojo ID: ")
    for kortele in mano_biblioteka.korteles:
        if kortele.id == vartotojo_id:
            kortele_rasta=True
            print("pasiskolintos_knygos: ")
            for knyga in kortele.pasiskolintos_knygos:
                print(knyga)
            
    if not kortele_rasta:
        print(f"vartotojo kortele su ID {vartotojo_id} nerasta")
    input("spausti enter, kad grizti i pradini meniu")


#  pasalinti_knyga_is_bibliotekos():
#     pass

def perziura_veluojanciu_knygu(mano_biblioteka):
    kortele_rasta=False
    vartotojo_id=input("iveskite vartotojo ID: ")
    for kortele in mano_biblioteka.korteles:
        if kortele.id == vartotojo_id:
            kortele_rasta=True
            velavimo_patikrinimas = kortele.velavimo_patikrinimas()
            if velavimo_patikrinimas:
                print("Veluojancios knygos:")
                for knyga in velavimo_patikrinimas:
                        print(knyga)
            else:
                print("nera veluojanciu knygu.")

            
    if not kortele_rasta:
        print(f"vartotojo kortele su ID {vartotojo_id} nerasta")
    input("spausti enter, kad grizti i pradini meniu")

   

if __name__=="__main__":

    mano_biblioteka=Biblioteka().atidaryti_biblioteka()

    while True:
        pasirinkimo_meniu()
        pasirinkimas = input("pasirinkimas (1-9): ")
        
        if pasirinkimas == '1':
            atspausdinti_knygu_sarasa(mano_biblioteka)
        elif pasirinkimas == '2':
            ieskoti_knygos(mano_biblioteka)
        elif pasirinkimas == '3':
            registruoti_naudotoja(mano_biblioteka)
        elif pasirinkimas == '4':
            pasiimti_knyga_namo(mano_biblioteka)
        elif pasirinkimas == '5':
            parnesti_knyga(mano_biblioteka)
        elif pasirinkimas == '6':
            prideti_knyga_i_biblioteka(mano_biblioteka)
        elif pasirinkimas == '7':
            pasalinti_knyga(mano_biblioteka)
            input("spausti enter, kad grizti i pradini meniu")
        elif pasirinkimas == '8':
            perziura_veluojanciu_knygu(mano_biblioteka)
        elif pasirinkimas == '9':
            perziureti_pasiskolintas_knygas(mano_biblioteka)
       
        elif pasirinkimas == '0':
            
            break
        else:
            print("Neteisingas pasirinkimas")
        
    



   