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


        