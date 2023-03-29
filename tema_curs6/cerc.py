### 1.Clasa Cerc
class Cerc:
    raza = None
    culoare = None

    #constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    #metoda descriere cerc
    def descriere_cerc(self):
        # printeaza culoare si raza cerc
        print(f"Cercul are raza: {cerc.raza}")
        print(f"Cercul are culoarea: {cerc.culoare}")

    def aria(self):
        aria = 3.14 * self.raza * self.raza
        return aria

    def diametru(self):
        diam_cerc = 2 * self.raza
        return diam_cerc

    def circumferinta(self):
        circumf_cerc = 2 * 3.14 * self.raza
        return circumf_cerc


#initializare
cerc = Cerc(6,"albastru")

# apelam functia
cerc.descriere_cerc()        # pentru culoare si raza
print(cerc.aria())           # pt arie
print(cerc.diametru())       # pt diametru
print(cerc.circumferinta())  #pt circumferinta
