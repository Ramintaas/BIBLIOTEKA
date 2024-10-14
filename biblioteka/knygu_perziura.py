import biblioteka.prideti_knyga as bk

def patikrinti_prieinamuma(biblioteka):
    title = input("Ivesti knyga: ")
    found = False
    
    for knyga in biblioteka:
        if knyga.title.lower() == title.lower():
            if knyga.available:
                print("Knyga prienama.")
            else:
                print("KNyga jau paskolinta")
            found = True
            break
    
    if not found:
        print("Knyga nerasta")

         

def knygu_perziurejimas(self, failo_pavadinimas):
        with open(failo_pavadinimas, 'wb') as failas:
            pickle.dump(self.knygos, failas)
        print(f"Knygos išsaugotos faile '{failo_pavadinimas}'.")   
