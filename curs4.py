"""
Structuri repetitive = blocuri de cod care se vor exe in mod repetitiv pana cand o anum cond nu mai e respectata
Iterarie = proces prin care un bloc de cod este exe in cadrul structurii repetitive
"""

#####   WHILE / WHILE ELSE
"""
while = cat timp = conditia ne permite executarea unui bloc de cod cat timp o cond e adevarata
 - Contorul de control al structurii repetitive trebuie declarat in afara structurii repetitive si
  modificat in interiorul blocului de cod
  !!! Daca nu modif val contorului in interiorul structurii repetitive vom crea un loop (ciclu) infinit
"""

# i = 0
# while i <= 3:
#     print(f'Valoarea lui i inainte de incrementare: {i}')
#     i += 1
# print('done')

"""
While-ul de mai sus se itereaza astfel: 
i  = 0 => i <=3 ? DA -> se exe codul din interiorul ciculului 
i  = 1 => i <=3 ? DA -> se exe codul din interiorul ciculului 
i  = 2 => i <=3 ? DA -> se exe codul din interiorul ciculului 
i  = 3 => i <=3 ? DA -> se exe codul din interiorul ciculului 
i  = 4 => i <=3 ? NU -> se iese din cicul
"""

#exemplu ciclu infinit
# i = 0
# while i <= 3:
#     print(f'Valoarea lui i inainte de incrementare: {i}')
#     i -= 1
# print('done')

### Exemplu cu break
#
# i = 0
# while i <=10:
#     print(f'Valoarea lui i este {i}')
#     if i == 5:
#         pass
#         # break
#     i += 1
# print('done')

# i = 0
# while i <= 3 :
#     print(f'Valoarea lui i este {i}')
#     if i == -10:
#         break
#     i -= 1
# print('done')

# while True:
#     print("Infinit")

"""
Fol WHILE ELSE (referinta la exemplul de mai sus)
WHILE = tipul structurii repetitive
i <= 3 : cond care se evalueaza
else: setul de instr care se va exe dupa ce se iese din structura repetitiva
"""

# i = 0
# while i <= 20:
#     print(f'i = {i}')
#     i += 1
# else:
#     print(f'i nu mai este mai mic sau egal cu 20, i={i}')
# print('Done')

"""
Debugging = Depanare = procesul prin care gasim si rezolvam prb in cod (bugs)
                     = punem pauza in cod ca sa vedem cum se parcurge codul pas cu pas
                    
"""

#### Parcurgerea listelor cu while
# lista_fructe = ["mere", "pere", "banane", "struguri"]
#  i = 0
#  while i < len(lista_fructe):
#      print(f'fructe = {lista_fructe[i]}')
#      i += 1
#     print("am iesit din while")
#
"""
Exercitiu:
Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show the names in your list
Q to quit 
"""
# names = []
# ALLOW_COMMANDS = ['a', 'r', 's', 'q']
# continue_loop = True
#
# while continue_loop: #se va iesi din while atunci cand continue_loop = False
#     command = input("Intro comanda ['A', 'R', 'S', 'Q']:").lower()
#
#     if command in ALLOW_COMMANDS:
#         if command == 'a':
#             name = input("Intro un nume pt a-l adauga: ")
#             names.append(name) # SAU names = names +name
#         elif command == 'r':
#             name = input("Introdu un nume pt a-l sterge: ")
#             names.remove(name)
#         elif command == 's':
#             print(f"Lista actuala este: {names}")
#         else:
#             continue_loop = False #putem fol si break
#     else:
#         print(f"Intro o comanda valida, alegeti intre ['A', 'R', 'S', 'Q']")


#### FOR / FOR ELSE
"""
range -> functie care defineste un interval 
     range(A,B,C)
     A = de unde incepem. daca nu punem nimic, atunci e default 0 ex: range(4) <=> 0,1,2,3
     B = pana unde mergem. daca nu punem, atunci va fi limita superioara - 1  ex: range(4) <=> 0,1,2,3
     C = pasul care este optional (default = 1)
"""
# for i in range(3,12): #(A,B)
#     print(i)

for i in range(4,0,-2):
    print(i)

# for i in range(12,2,-1):
#     print(i)
#
# for i in range(33):  #B
#     print(i)

# FOR EACH - lista
# for i in [3,4,6,"mere",7,True]:
#     print(i)
#
# #FOR
# lista = [3,4,6,"mere",7,True]
# for i in range(len(lista)):
#     print(lista[i])

###
###Calc primele nr pare pana la 101
# suma = 0
# for i in range(0,102,2):
#     print(i)
#     suma +=i
# print(suma)

### Inverseaza textul fol for
# text = "Ana are mere"
# text_inversat = ""
# print(len(text))
# for i in range(11,-1,-1):  #(len(text)-1,-1,-1):
#     text_inversat += text[i] #text[::-1]
# else:
#     print("A terminat range ul ")
# print(text_inversat)

"""
Ex: avem o lista de culori: ["roz","albastru","rosu","alb","galben"]
Parcurg lista iar cand ajung la val alb, dau skip
"""
# lista_culori = ["roz","albastru","rosu","alb","galben"]

# for culoare in lista_culori:
#     if culoare == "alb":
#         continue
#     print(culoare)
# for culoare in lista_culori:
#     if culoare == "alb":
#         break ### se opreste la rosu
#     print(culoare)

"""
avem lista de mai sus. stergem din lista toate nonculorile(alb, gri, negru)
"""
# for culoare in lista_culori:
#     if culoare == "alb":
#         lista_culori.remove(culoare) #("alb")
#         print(f"{culoare} este o nonculoare")
# print(lista_culori)

### Cum iteram cheie valoare intr un dinctionar?
# note_elevi = {
#     "Andrei":10,
#     "Elena": 8,
#     "Maria":10,
# }
# print(note_elevi.items())
#
# for elev,nota in note_elevi.items():
#     print(f"{elev} a luat nota {nota}")
#
### cum iteram printr un dictionar in dictionar etc

dict1 = {
    "HR":{
        "1":{
            "Andrei": 4532,
            "Marian": 2456,
            "Florin":15695
        },
        "2":{
            "Iulia": 5465,
            "Georgiana": 455,
            "Luca": 452,
        }
    }
}
print(dict1.items())

for cheie, valoare in dict1.items():
    # print(cheie, valoare)
    for cheie_dinhr, valori_din_hr in valoare.items():
        print(cheie_dinhr, valori_din_hr)
        for cheie_din_1_2, valori_din_1_2 in valori_din_hr.items():
            print(cheie_din_1_2, valori_din_1_2)
