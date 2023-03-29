### List ###
"""
-Listele sunt structuri de date built - in Python
-Listele sunt fol pt a stoca mai multe elem intr o sg variabila
-Crearea unei liste se face cu [] sau list()

"""
## Crearea unei liste ##
# lista_goala = []   # - > cream lista cu [] - cea mai usuala varianta
# print(type(lista_goala))
# lista_goala = list() # -> cream o lista cu list()
# print(type(lista_goala))

# lista in lista devine matrice
# lista = ["masina", 42, True, 42, [1, 2, 3]]
# print(lista)

## Caracteristicile unei liste
"""
 Ordonate
 Mutabile - se pot adauga sterge si schimba elem din lista
 Accepta duplicate
 itemii/elem listei sunt indexati (primul index este 0)

"""
#liste ordonate
"""
elem unei liste au o anumita ordine care nu se schimba
daca adaug un elem nou, acesta va fi pus la finalul listei
!!! atentie - exista anum metode in liste care pot schimba ordinea elem in lista 
"""
# masini = ["Audi" , "VW", "BMW", "Skoda" , "Mercedes" ]
# print(masini)

### Accesare elemente
# print("masini[0]=", masini[0])
# print("masini[-1]=", masini[-1])
# print("masini[:4]=", masini[:4])
# print("masini[::-1]=", masini[::-1])
# print("masini[2:5]=", masini[2:5])
# print(masini[6]) # arunca o exceptie

## adaugarea de elem
# masini = ["Audi" , "VW", "BMW", "Skoda" , "Mercedes" ]
# masini = masini + ["Toyota"]
# print(masini)
# # masini = masini + ["Reno", "Dacia"]
# # print(masini)
#
# masini.append(["Toyota", "Reno"])
# masini.append("Audi")
# masini = masini + ["Reno", "Dacia"]
# print(masini)
# print(masini[-1])
# masini.extend(["Volvo", "Pejout"])
# print(masini)
# print(masini[-1])

## modificare ordine
# masini = ["Audi" , "VW", "BMW", "Skoda" , "Mercedes" ]
# masini.insert(1,"Reno")
# masini.insert(len(masini), "Reno") # il pune dupa mercedes, adica dupa ultima pozitie
# print(masini)

### stergerea unui element
# masini = ["Audi" , "VW", "BMW", "Skoda" , "Mercedes", "BMW" ]
#
# # masini.remove("BMW")
# print(masini)
#
# masina_stearsa = masini.pop()   #-> sterge ultima val din lista si o returneaza
# print(masina_stearsa)
# print(masini)
# masini.pop(0)
# print(masini)
#
# masini.clear()
# print(masini)

#schimbare de elemente
# masini = ["Audi" , "VW", "BMW", "Skoda" , "Mercedes", "BMW" ]
# masini[0] = "audi a3"
# print(masini)
#
# ### listele accepta duplicate
#
# masini = ["Audi" ,"Audi", "VW", "BMW", "Skoda" , "Mercedes", "BMW" ]
#
# ##lungimea unei liste
# print(len(masini))



### Dictionare  ###
"""
   -Dict sunt fol pt a stoca elem intr o pereche de key:value 
"""
# Crearea unui Dictionar

# dictionar_gol = {}
# print(type(dictionar_gol))
#
# dictionar_gol = dict()
# print(type(dictionar_gol))

# dictionar = {
#             "nume": "Vlad",
#             "varsta": 27,
#             "tara": "Romania",
#             "limbi_vorbite": ["Romana", "Eng"]
# }
# # dictionar = dict(nume="Vlad", varsta = 27, tara = "Romania", limbi_vorbite = ["Romana", "Eng"])
# print(dictionar)

## Caracteristici
"""
-> ordonate *(incepand cu python vers 3.7 ) (ca la liste)
-> Mutabila (ca la liste)
-> Nu accepta chei duplicate
-> Neindexat -> indecsii sunt inlocuiti cu chei 
"""

## nu accepta chei duplicate
# dictionar = {
#             "nume": "Vlad",
#             "varsta": 27,
#             "tara": "Romania",
#             "tara": "Germania",
#             "limbi_vorbite": ["Romana", "Eng"]
# }
# print(dictionar) # - > valoarea de la cheia "tara" se va lua ultima val atribuita

## Accesare elemenete

# dictionar = {
#             "nume": "Vlad",
#             "varsta": 27,
#             "tara": "Romania",
#             "limbi_vorbite": ["Romana", "Eng"]
# }
# tara_Vlad = dictionar.get("tara")
# print(tara_Vlad)
# #sau
# tara_Vlad_2 = dictionar["tara"]
# print(tara_Vlad_2)
#
# ## accesarea tuturor val dintr un dict
# print(dictionar.values())
#
# ### accesare chei
# print(dictionar.keys())
#
# #items -returneaza toate elem din dictionar( tupla)
# print(dictionar.items())

### SCHIMBAREA UNUI ELEMENT
# dictionar["tara"] = "Germania"
# print(dictionar)
# print(dictionar["tara"])
#
# #SAU
# dictionar.update({"tara":"Franta"})
# print(dictionar)
#
# ### ADUGAREA UNUI ELEMENT
# dictionar["sex"] = "Feminin"
# print(dictionar)
# dictionar.update({"CNP":"1234567891230"})
# print(dictionar)

### Stergerea  unui element din dict
# dictionar.pop("CNP")
# print(dictionar)
# dictionar.popitem() # -> scoate ultima chie:val din dictionar (lifo)
# print(dictionar)
#
# ### stergerea tuturor elem
# # dictionar.clear()
# # print(dictionar)
#
# #### Lungimea
# print(len(dictionar))

### set- uri
"""

"""
# set_gol = set()
# print(type(set_gol))
#
# set_gol = {}
# print(type(set_gol)) # --




#### caracteristici ale set-ului
"""
-> Neordonate
-> Imutabile - nu se pot schimba val, doar adauga sau sterge 
-> nu accepta duplicate
-> neindexat 
"""
# fructe = {"mere", "pere", "cirese"}
# print(fructe)

### fara duplicate
# fructe = {"mere", "pere", "cirese", "mere"}
# print(fructe)
#
# ### adaugarea unui element
# fructe.add("portocale")
# print(fructe)
# fructe.add(12)
# print(fructe)
#
# ### adaugarea unui set in alt set ### atentie nu accepta doar seturi, putem intro si liste si tuple
#
# fructe2 = {"ananas", "banane"}
# fructe.update(fructe2)
# print(fructe)
#
# fructe_lista = ["ananas", "banane"]
# fructe.update(fructe_lista)
# print(fructe)


#### Stergerea unui element
# fructe = {"mere", "pere", "cirese", "mere"}
# fructe.remove("mere") # remove arunca exceptia daca nu gaseste valoarea
# print(fructe)
# fructe.discard("mere") # discard nu arunca exceptie daca val nu exista
# print(fructe)
#
# ### stergerea setului
# print(fructe.clear())
# print(fructe)



###  TUPLE
#Crearea unei tuple
# tupla = ()
# print(type(tupla))
# tupla = tuple()
# print(type(tupla))

### atentie!!!!
# nu_este_tupla = ("string")
# print(type(nu_este_tupla))
# aceasta_este_o_tupla_cu_un_sg_elem = ("String",)
# print(type(aceasta_este_o_tupla_cu_un_sg_elem))
#
# tuple1 = (1,2,3,4,5,1)
# print(tuple1.count(3))
# print(tuple1.index(3))
#
# print(tuple1[0])
# print(tuple1[-1])
# print(tuple1[::-1])
# tuple1[0] = 4

### mic hack
# tuple1 = list(tuple1)
# tuple1 += [4]  # tuple1[0]=4
# tuple1 = tuple(tuple1)
# print(tuple1)

##unpack
# tuple2 =(1,2,3)
# x,y,z = tuple2
# print(x,y,z)