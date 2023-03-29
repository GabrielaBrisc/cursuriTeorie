# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina():
    marca = "Audi"
    model = None
    viteza_max = None
    viteza_actuala = 0
    culoare = "gri" #toate masinile au gri by default
    culori_disp = ["rosu", "albastru", "alb", "gri"]
    inmatriculata = False

    #constructor
    def __init__(self, model, viteza_max):
        self.viteza_max = viteza_max
        self.model = model
    #
    def descrie(self):
        print(f"Masina este marca {self.marca} \n"
              f"iar modelul este {self.model} \n"
              f"este de culoare {self.culoare} \n"
              f"aceasta are viteza actuala de {self.viteza_actuala} \n"
              f"este inmatriculata?: {self.inmatriculata} \n"
              f"viteza maxima este de {self.viteza_max} \n")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, new_color):
        if new_color in self.culori_disp:
            print(f"Noua culoare este {new_color}")
        else:
            print("Culoarea nu se afla in paletarul nostru de culori disponibile")

    def accelereaza(self, accelereaza_pana_la):
        if accelereaza_pana_la < 0:
            print("Eroare")
        elif accelereaza_pana_la <= self.viteza_max:
            self.viteza_actuala = self.viteza_max
            return self.viteza_actuala
        else:
            self.viteza_actuala += accelereaza_pana_la

    def franeaza(self, incetineste):
        if self.viteza_actuala > 0:
            self.viteza_actuala -= incetineste
            print({self.viteza_actuala})
        else:
            self.viteza_actuala = 0
        print("viteza este 0")


### initializare
masina = Masina("a3 ", 190)

##apelam functia
masina.descrie()
print(masina.inmatriculare())
masina.descrie()
print(masina.vopseste("negru"))
masina.accelereaza(200)
print(masina.viteza_actuala)
masina.franeaza(200)
print(masina.viteza_actuala)