from biblioteka import Biblioteka, Knyga
from skaitytojo_kortele import Skaitytojo_kortele, Naudotojas


            
if __name__=="__main__":
    mano_biblioteka=Biblioteka().atidaryti_biblioteka()

    mano_biblioteka.visos_knygos()
    mano_biblioteka.perziureti_korteles()
    mano_biblioteka.pasiskolinti_knyga("Mazasis Princas", "5555", "2024-10-14")
    mano_biblioteka.visos_knygos()
    mano_biblioteka.issaugoti_biblioteka()

