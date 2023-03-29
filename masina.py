### schita(unei masini) a unei realitati din lumea inconjuratoare

class Masina:
    # atribute default
    marca = None
    model = None
    culoare = "alb"
    motor_pornit = False
    viteza = 0

    #constructor - o met care ne obliga sa dam valori parametrilor
    #mentionati intre () atunci cand cream obiecte
    def __init__(self, marca, model):
        #self.marca este atributul obiectului instantiat
        #marca este param fctiei
        #prin el va veni val pe care o dam cand cream obiectul
        self.marca = marca
        self.model = model

    #metoda - are self
    def prezentare_masina(self):
        if self.motor_pornit:  # <=> self.motor_pornit == True
            stare_motor = "pornit"
        else:
            stare_motor = "oprit"
        print(f"Masina {self.marca}, cu modelul {self.model}, "
              f"are culoarea {self.culoare} si are motorul "
              f"{stare_motor} cu viteza de {self.viteza}")

    def start(self):
        self.motor_pornit =True
    def stop(self):
        self.motor_pornit = False
        self.viteza = 0

    def accelereaza(self, val_accelerare):
        if self.motor_pornit == True: # <=> self.motor_pornit
            self.viteza += val_accelerare
            print(f"Masina a ajuns la {self.viteza} km/h")
        else:
            print("nu se poate accelera deoarece nu e pornit motorul ")

    def incetineste(self, incetineste_cu):
         if self.motor_pornit == True and self.viteza >0:
             if self.viteza > incetineste_cu:
                self.viteza -= incetineste_cu
             else:
                self.viteza = 0
             print(f"masina a ajuns la {self.viteza} km/h")
         else:
              print("nu putem incetini pt ca motorul ")


#instantiem un ob de tipul Masina()
masina_1 = Masina("audi","a3")
print(masina_1.model)
print(masina_1.culoare)
# putem modif un atribut
masina_1.model = "R7"
print(masina_1.model)
