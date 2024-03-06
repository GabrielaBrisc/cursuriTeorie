# print("Hello World")

#comentarii = linii din codul sursa care nu sunt extecutate (menite pentru adnotari/explicatii)
# comentariu pe o sg linie
# pentru comentarii pe mai multe linii folosim """ """ sau ''' ''.

""" 
  Zona de comentariu extinsa fol ghilimele
  x= 5
  y= 10
"""

'''
   Zona de comentariu extinsa fol ghilimele
  x= 5
  y= 10
  print("Al doilea hello"
'''

#variabile
"""
1. o variabila este o zona de mem rezervata in sistem care poate stoca info 
2. poate fi modificata
3. variabila este creata doar dupa ce i se asigneaza o valoare
   variabila = 5
4. reguli de denumire
  -nu pot contine spatii
  -nu pot sa fie denumite cu nume rezervat (nu putem avea o variabila cu numele de print)
  -trebuie sa fie unice
  -nu pot incepe cu un nr dar pot contine nr in numele lor eg: variabila5 (incorect: 5variabila)
  -denumirea e case sensitive (o var numita camelCase nu e aceeasi cu camelcase
5. Conventii in python:
 -pt nume de clase: pascalCase (addTwoNumbers)
 -pt nume de var/methode: snake_case
 -pt constante: NUME_CONSTANTE
 
Constantele sunt spatii de mem care nu isi schimba valoarea
!!! In Python exista doar ca si concept ideea de constanta
"""

# declarare si initializare de variabile
# model_masina = "v60"
# model_Masina = "v10"
# print(model_masina)
# print(model_Masina)

#constante
# NUME_MASINA = "Dacia"
# print(NUME_MASINA)
# NUME_MASINA = "Audi"
# print(NUME_MASINA)
#
#Modificarea tipului de date
# model_masina = "v60"
# print(type(model_masina))
# model_masina = 330
# print(type(model_masina))
# model_masina = "330"
# print("1. ",type(model_masina))
# model_masina = int("330")
# print("2. ",type(model_masina))
# # #
# print("a+b ca string =", "a" + "b")
# print("3+3 ca int =", 3+3)
# print("3+3 ca string =", "3" + "3")
#de la nr la string poti face trecerea, invers nu

#b = int("a") -> Nu se poate face cast (trecerea de la un tip la altul) la int
# v = "3"+"3" #si asa e str doar ca le uneste, nu le aduna (33)
v =str(3 + 3)
print(v)
print("Cast de la int la string: ",type(v))

# x,y,z = "Luni", "Marti", 3
# print(x,y,z)
# x =y = z = "Sambata"
# print(x,y,z)


### TIPURI DE DATE
"""
 1. Un tip de date este o info care ii spune sist ce tip de info putem stoca intr o var
 2. Cele mai fol tipuri de date
   -int (intreg) - > poate stoca doar valori intregi (fara virgula)
   -float -> poate stoca val zecimale (16 -> 16.0)
   -bool - > poate stoca text (sir de caractere)
   
 """
# a = 3    #int
# b = 5.5  #float
# c = False #bool
# d = "String" #string
#
# print(type(a),type(b),type(c),type(d))

### FUNCTIA PRINT###
"""
print() = funtie python care ne ajuta sa afisam ce ii dam intre paranteze in consola
"""
# nume = "Gabi"
# varsta = 22
# print("Ma numesc" + nume + "si am varsta de " + str(varsta))
# print(f"Ma numesc {nume} si am varsta de {varsta}") #varianta recomandata

### FUNCTIA INPUT###
"""
IntPUT() = funtie python care ne ajuta sa afisam ce ii dam intre paranteze in consola
"""
# nume = input("Introduceti nume: ")
# print(nume)
# # varsta = input("Introduceti varsta: ")
# # print(varsta)
# # print(type(varsta))
# varsta = int(input("Introduceti varsta: "))
# print(varsta)
# print(type(varsta))


### ASSERT ###

# a= 1
# assert a == 1
# print("a e egal 1")
# assert  a == 2
# print("aici nu mai ajunge rularea")


# user_password = input("Password: ")
# expecte_password = "parola123"
# assert user_password == expecte_password, "Parola incorecta"
# print("Correct password")

### STRING ###
"""
  - fiecare caracter are un index
  - primul caract are indexul 0
  - putem taia (slice) un string fol urmat sintaxa
  my_str[start_pos:end_pos:step]
"""

exemple = "Februarie"
print(len(exemple))
# print(exemple[0]) #F
# print(exemple[1]) #e
# print(exemple[2:5]) #bru
# print(exemple[-1]) #e
# print(exemple[-3:-1]) #ri
print(exemple[::-1])  #eiraurbeF
print(exemple[1::])  #ebruarie

#Index             0  1  2  3  4  5  6  7  8
#caracter          F  e  b  r  u  a  r  i  e
# Negative index: -9 -8 -7 -6 -5 -4 -3 -2 -1

# print(exemple.count("e"))
# print(exemple.replace("e", "7"))
# print(exemple.upper())
#
# new_exemple = exemple.replace("e", "7")
# print(new_exemple)

# () - fol cand apelam functii
# [] - fol pt liste, slice. eg lista: lista= [1,2,3,4]
# {} - fol pt dictionare/set-uri
