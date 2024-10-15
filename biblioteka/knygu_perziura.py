from biblioteka import Biblioteka

def patikrinti_prieinamuma(biblioteka):
    pavadinimas = input("Ivesti knyga: ")
    found = False
    
    for knyga in biblioteka.knygos:
        if knyga.pavadinimas.lower() == pavadinimas.lower():
            if knyga.kiekis>0:

                print("Knyga prienama.")
            else:
                print("KNyga jau paskolinta")
            found = True
            break
    
    if not found:
        print("Knyga nerasta")
    
if __name__=="__main__":
    
    mano_biblioteka=Biblioteka().atidaryti_biblioteka()
    patikrinti_prieinamuma(mano_biblioteka)
         

