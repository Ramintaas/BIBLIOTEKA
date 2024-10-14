import pickle
from prideti_knyga import Biblioteka

def pasalinti_knyga(library):
    if not library:
        print("Biblioteka tuscia.")
        return

    pavadinimas = input("Ivesti knyga kuria norim istrinti: ")
    found = False
    
    for knyga in library:
        if knyga.lower() == pavadinimas.lower():
            library.remove(knyga)
            print(f'"{knyga}" knyga istrinta.')
            found = True
            break
    
    if not found:
        print(f'Knygos"{pavadinimas}" nerasta bibliotekoje.')

def isaugoti_library(library, filename='library.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(library, file)
        print(f'Library saved to {filename}')





   
       

