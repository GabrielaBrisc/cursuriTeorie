####  2. Clasa Dreptunghi
class Dreptunghi:
    # atribute
    lungime = None
    latime = None
    culoare = None

### Constructor pt toate atributele
    def __init__(self, lungime, latime, culoare):
       self.lungime = lungime
       self.latime = latime
       self.culoare = culoare

###  Metode
    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are lungimea: {dreptunghi.lungime}")
        print(f"Dreptunghiul are latimea: {dreptunghi.latime}")
        print(f"Dreptunghiul are culoarea: {dreptunghi.culoare}")

    def arie_dreptunghi(self):
        aria = self.lungime * self.latime
        print(f"Aria dreptunghiului este:", aria)

    def perimetru_dreptunghi(self):
        perimetru = 2 * (self.lungime + self.latime)
        print(f"Perimetrul dreptunghiului este:", perimetru)

### schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
###Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
###self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
###descrie().
    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare
        print(f"Noua culoare a dreptunghiului este:", noua_culoare)

##instantiem obiectul de tip dreptunghi, (initializam)
dreptunghi = Dreptunghi(5, 6, 'rosie')

##apelam functiile pentru a ne printa/returna interiorul lor
dreptunghi.descrie_dreptunghi()
dreptunghi.arie_dreptunghi()
dreptunghi.perimetru_dreptunghi()

##apelam functia
##schimbare culoare
##am dat param noua_culoare
dreptunghi.schimba_culoarea("Verde")
##verif schimbarea culorii
dreptunghi.descrie_dreptunghi()

