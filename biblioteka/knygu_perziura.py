from prideti_knyga import Biblioteka

def patikrinti_prieinamuma(biblioteka):
    pavadinimas = input("Ivesti knyga: ")
    found = False
    
    for knyga in biblioteka:
        if knyga.pavadinimas.lower() == pavadinimas.lower():
            if knyga.available:
                print("Knyga prienama.")
            else:
                print("KNyga jau paskolinta")
            found = True
            break
    
    if not found:
        print("Knyga nerasta")

         

