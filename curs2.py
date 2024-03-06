#OPERATORI DE ATRIBUIRE
"""
atribuire = asignagre = proces prin care salvam info la adr de mem identif cu un nume al variabilei
"""
"""
= --> x = 5 (x ia val 5)
+= --> x += 4 <=> x = x+4
-= --> x -= 4 <=> x = x-4
*= --> x += 4 <=> x = x*4
/= --> x += 4 <=> x = x / 4
"""

# print("*"*5,"Operatori de atribuire","*"*5)
x = 5
print("x =",x)
x += 3
print("x += 3: ", x)
x -= 4
print("x -= 4: ", x)
x = 10
print("x= 10: ", x)
x /= 10
print("x /= 10: ", x)

# #OPERATORII ARITMETICI
# """
# + adunare --> x+y
# - scadere --> x-y
# * inmultire --> x * y
# /impartire  --> x/ y
# // floor division --> x//y rotunjeste rezultatul la cel mai apropiat nr intreg inferior
# % modulo --> x%y returneaza restul impartirii
# ** Exponential --> x**y
# """
# print("*"*5,"Operatori aritmetici","*"*5)
#
# x = 10
# y = 5
# print(f"{x}+{y}=",x+y)
# print(f"x-y=",x-y)
# print(f"xy=",x*y)
# print(f"x/y=",x/y)
# print(f"x//y=",x//y)
# print(f"x%y=",x%y)
# print(f"x**y=",x**y)
# x = 7
# y = 3
# print(f"{x}/{y}=",x/y)
# print(f"x//y=",x//y)
# print(f"x%y=",x%y)

###Operatori logici
# print("*"*5,"Operatori logici","*"*5)
# x = 2
# print("and -->",x > 5 and x < 10 ) # ( False and True => False)
# print("or -->",x > 5 or x < 10) # ( False or True => True)
# print("not -->",not(x > 5 or x < 10)) # ( not(False or True) => not(True) => False)
# # NOT > AND > OR
# print(not(x > 5) or x < 10 and x == 3) # (not(False) or True and False) --> True or True and False => True or False => True
# print(not(x < 5))

#------------------------------------------------------------------------------#
#### Operatorii de comparare ####
"""
== --> Equal                        --> x == y (Verifica daca x este egal cu y) !!! Nu este tot una cu x = y ( x IA valoarea lui y)
!= --> Not Equal                    --> x != y (Verifica daca x este diferit de y)
 --> Greater then                 --> x > y (Verifica daca x este mai mare ca y)
<  --> Less then                    --> x < y (Verifica daca x este mai mic ca y)
>=  --> Greater then or equal to    --> x >= y (Verifica daca x este mai mare sau egal cu y)
<=  --> Less then or equal to       --> x <= y (Verifica daca x este mai mic sau egal cu y)
"""
# print("*"*5,"Operatori de comparare","*"*5)
# x = 2
# y = 13
# print(f"{x}=={y}",x==y)
# print(f"{x}!={y}",x!=y)
# print(f"{x}>{y}",x>y)
# print(f"{x}<{y}",x<y)
# print(f"{x}>={y}",x>=y)
# print(f"{x}<={y}",x<=y)
# print("-"*10)
# x = 13
# y = 13
# print(f"{x}>{y}",x>y)
# print(f"{x}<{y}",x<y)
# print(f"{x}>={y}",x>=y)
# print(f"{x}<={y}",x<=y)
#
# """ Flow control  """
# nota_de_trecere = 4.5
# nota = float(input("Intro nota: "))
#
# if nota > nota_de_trecere:
#     print(f"felicitari, ai luat nota {nota}")
# else:
#     print(f"ne pare rau ai picat cu nota {nota}")
# #------------------------------------------------------------------------------#
# #### Flow Control ####
# print("*"*5,"Flow Control","*"*5)
# print("*"*3,"If Simplu","*"*3)
#
# nota_de_trecere = 4.5
# # nota = float(input("Introduce-ti nota: "))
# nota = 6
#
# if nota >= nota_de_trecere:
#     print(f"Felicitari, ai luat nota {nota}")
# print("Am trecut de if")
#
# print("*"*3,"If else","*"*3)
#
# if nota >= nota_de_trecere:
#     print(f"Felicitari, ai luat nota {nota}")
# else:
#     print(f"Ne pare rau dar ai picat examenul cu nota {nota}")
#
# print("*"*3,"If elif ... else","*"*3)
#
# optiune = input("Alege o optiune [0,1,2]: ")
#
# if optiune == 0:
#     print("ai ales 0")
# elif optiune == 1:
#     print("ai ales 1")
# elif optiune == 2:
#     print("ai ales 2")
# else:
#     print("Nu ai ales nici o optiune valida")


