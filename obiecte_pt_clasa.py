# from masina import Masina
#
# ## varianta aceasta nu mai e valida deoarece am adaugat constructor
# #care contine 2 param (model, marca)
# audi = Masina()
# print(audi.model)
# print(audi.marca)
# print(audi.culoare)
# print(audi.motor_pornit)
# print(audi.viteza)
# audi.marca = "Mercedes"
# print(audi.marca)
# model R7

# audi = Masina("Audi", "A4")
# # print(audi.marca)
# # print(audi.model)
#
# bmw = Masina(model ="R5",marca= "A4")
# # print(bmw.marca)
# # print(bmw.model)
#
# audi.prezentare_masina()
# bmw.culoare = "negru"
# bmw.prezentare_masina()
#
# audi.start()
# audi.accelereaza(20)
# audi.prezentare_masina()
# audi.accelereaza(45)
# audi.incetineste(30)
# print(audi.motor_pornit)
# audi.stop()
# print(audi.viteza)
# print(audi.motor_pornit)

from persoana import Persoana
from curs_programare import Curs_Programare

curs_Ta = Curs_Programare("It fact","Testare Automata", 15, 12)
curs_Ta.descriere_curs()

diana = Persoana("Covaci","Diana",25)
roman = Persoana("Roman", "I", 120)
curs_Ta.inscriere_student(diana)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.inscriere_student(roman)
curs_Ta.descriere_curs()
curs_Ta.inscriere_student(diana)
curs_Ta2 = Curs_Programare("It fact","Testare Automata", 15, 12)
