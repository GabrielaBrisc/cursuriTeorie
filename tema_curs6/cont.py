### Clasa Cont

class Cont:
  ##atribute:
    titular_cont = None
    iban = None
    sold = None
  ##Constructor pt toate atributele:
    def __init__(self, titular_cont, iban, sold):
       self.titular_cont= titular_cont
       self.iban = iban
       self.sold = sold

    #Metode
    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} "
              f"suma de {self.sold}")

    def debitare_cont(self, suma_retrasa):
        self.sold = self.sold + suma_retrasa
        print(f"Suma ramasa dupa retragere este {self.sold}")

    def creditare_cont(self,suma_creditare):
        self.sold = self.sold - suma_creditare
        print(f"Noul sold dupa creditare este {self.sold}")

##instantiem obiectul
cont_1= Cont('Gabi Maria', 'RoBRDE123123', 2500)
cont_1.afisare_sold()
print(cont_1.titular_cont)
print(cont_1.iban)
print(cont_1.sold)
cont_1.debitare_cont(500)
cont_1.creditare_cont(1500)
cont_1.afisare_sold()




