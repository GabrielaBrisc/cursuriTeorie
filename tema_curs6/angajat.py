### 3 Clasa Angajat

class Angajat:
    nume = None
    prenume = None
    salariu = None

    ###Constructorul pt atribute
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    ### Metodele:
    def descrie_angajat(self):
        print(f"Angajatul se numeste {self.nume} {self.prenume} "
              f"si are salariul de {self.salariu}")

    def nume_complet(self):
        print(f"Numele complet al angajatului este: {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f"Salariul lunar al angajatului este: {self.salariu}")

    def salariu_anual(self):
        salar_per_an = self.salariu *12
        print(f"Salariul anual al angajatului este: {salar_per_an}")

    def marire_salariu(self,procent):
        # salar_nou = 0
        marire = self.salariu * (procent/100)
        salar_nou = self.salariu + marire
        print(f"Salariul nou al angajatului este:",salar_nou)

### Instantiem un ob de tip Angajat
angajat_1 = Angajat('Brisc', 'Gabriela', 3500)

### apelam metodele
angajat_1.descrie_angajat()
angajat_1.nume_complet()
angajat_1.salariu_lunar()
angajat_1.salariu_anual()
angajat_1.marire_salariu(10)



