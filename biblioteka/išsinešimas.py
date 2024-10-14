import biblioteka.prideti_knyga as pk

def __init__(self, kiekis)
     self.kiekis = kiekis

def pasiskolinti_knyga(self, title):
        for book in self.knygos:
            if book.title == title:
                if book.kiekis > 0:
                    book.kiekis -= 1
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
        for book in self.knygos:
            print(book)


library = Library()
library.pasiskolinti_knyga("Knyga 1")