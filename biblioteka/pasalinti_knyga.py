
from biblioteka import Biblioteka, Knyga

def pasalinti_knyga(library):
    if not library:
        print("Biblioteka tuscia.")
        return

    pavadinimas = input("Ivesti knyga kuria norim istrinti: ")
    found = False
    
    for knyga in library.knygos:
        
        if knyga.pavadinimas.lower() == pavadinimas.lower(): #palyginam ar tai ka ivede vartotojaS YRA vienodas tekstas.

            library.pasalinti_knyga(knyga)
            print(f'"{knyga}" knyga istrinta.')
            found = True
            break
    
    if not found:
        print(f'Knygos"{pavadinimas}" nerasta bibliotekoje.')

if __name__=="__main__":
    mano_biblioteka=Biblioteka().atidaryti_biblioteka()

    pasalinti_knyga(mano_biblioteka)
    mano_biblioteka.issaugoti_biblioteka()





   
       

