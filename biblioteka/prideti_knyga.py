
from biblioteka import Biblioteka, Knyga


 

if __name__=="__main__":

    mano_biblioteka=Biblioteka()

    mano_biblioteka.prideti_knyga(Knyga({"pavadinimas":"Mazasis Princas", "autorius":"Exiuperi", "isleidimo_metai":"1943", "zanras":"Romanas","kiekis":2}))
    mano_biblioteka.prideti_knyga(Knyga({"pavadinimas":"Haris Poteris", "autorius":"J.K.Rowling", "isleidimo_metai":"2011", "zanras":"Romanas","kiekis":5}))
    mano_biblioteka.issaugoti_biblioteka()

    mano_biblioteka.visos_knygos()





