from prideti_knyga import Biblioteka

def __init__(self, kiekis):
     self.kiekis = kiekis

def pasiskolinti_knyga(self, title):
        for knyga in self.knygos:
            if knyga.title == title:
                if knyga.kiekis > 0:
                    knyga.kiekis -= 1
                    print(f"Knyga '{title}' pasiimta išsinešimui.")
                    return
                else:
                    print(f"Knyga '{title}' knygos neprieinama")
                    return
        print(f"Knyga '{title}' nerasta bibliotekoje.")

def parodyti_knygas(self):
        if not self.knygos:
            print("Biblioteka tuščia.")
            return
        for knyga in self.knygos:
            print(knyga)
            
if __name__=="__main__":
        mano_biblioteka=Biblioteka().atidaryti_biblioteka()

biblioteka = Biblioteka()
biblioteka.pasiskolinti_knyga("Knyga 1")

