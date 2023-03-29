### 1. Clasa Factura
## Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# #avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# #Constructor: toate atributele, fara serie
## Metode:
## ● schimbă_cantitatea(cantitate)
# #● schimbă_prețul(pret)
# #● schimbă_nume_produs(nume)
#
# #● generează_factura() - va printa tabelar dacă reușiți
# #Factura seria x numar y
# #Data: generați automat data de azi
# #Produs | cantitate | preț bucată | Total
# #Telefon | 7 | 700 | 49000

from datetime import datetime

class Factura:
    seria = 1234
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    ###Constructor
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        noua_cantitate = cantitate
        print(f"Factura contine o noua cantitate:", noua_cantitate)

    def schimba_pret(self, pret):
        noul_pret = pret
        print(f"Factura contine o noua cantitate:", noul_pret)

    def schimba_nume_produs(self, nume):
        noul_nume = nume
        print(f"Factura contine o noua cantitate:", noul_nume)

    def genereaza_factura(self):
        total = self.pret_buc * self.cantitate
        # print(total)
        print(f"Factura are seria {self.seria} si numarul {self.numar} \n "
              f"{datetime.now().strftime('%Y-%m-%d')} \n {self.nume_produs} {self.cantitate} {self.pret_buc} {total} \n")

factura = Factura(1, 'Telefon', 7, 5000)
factura.schimba_cantitatea(4)
factura.schimba_pret(4500)
factura.schimba_nume_produs('Samsung')
factura.genereaza_factura()
