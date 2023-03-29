####  FUNCTII

#Definirea functiei (fara parametrii si return)
# def say_hello():
#     print("Hello!")
# # apelare functie (va exe codul din interiorul codului)
# # say_hello()
# # say_hello()
# say_hello # -> daca nu punem paranteze nu se va exe corpul functiei (nu este vazuta functia)

#!!!! Daca o funct nu e apelata, codul din interiorul ei nu va fi exe
#adica functiile ruleaza independent de codul nostru

# # functia say_hello() nu returneaza nimic (NONE)
# print(say_hello()) # apelam functia (de aceea primim un Hello) dar nu returneaza nimic (adica NONE)
# x = say_hello()
# print("x=", x)

#Apelare functie cu parametru
# from utils.utils_file import say_hi_name
# from utils.utils_file import * #importam tot continutul fisiereului
# say_hi_name("Gabi") # -> arunca o eroare say_hi_name() missing 1 required positional argument: 'name'

# say_hi_name_and_age()
# # say_hi_name_and_age("Vali", 40)
# # say_hi_name_and_age(name="Elena",flag=False)
# say_hi_name_and_age("Elena",30)
#
# lista_nume = ["Iulia", "vali","Elena", "Matei"]
# for nume in lista_nume:
#     say_hi_name(nume)
#     say_hi_name_and_age(nume,25)


###  def o fct ce returneaza True daca nr e par si False daca nr e impar
# def check_odd(numar):
#     if numar % 2 ==0:
#         return True
#     else:
#         return False
#
# def say_hello():
#     print("Hello!")
#
# print(say_hello())
# print(check_odd(5))

# def check_odd(numar):
#     if numar % 2 ==0:
#         return f"{numar} este par"
#     else:
#         return f"{numar} este impar"
# x = check_odd(10)
# print(x)

# def check_if_your_no_greater_then_5():
#     x = int(input("Intro un nr: "))
#     if x > 5:
#         return True
#     else:
#         return False
#
# raspuns = check_if_your_no_greater_then_5()
# print(raspuns)

# def cod_dupa_return():
#     print("Inainte de return")
#     return True
#     print("dupa return")
#
# print(cod_dupa_return())
