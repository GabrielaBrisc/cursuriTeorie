# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
#
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict

class TodoList:
    ##atribute
    todo_List = {}

    def adauga_task(self,nume, descriere):
        self.todo_List.update({nume: descriere})

    def finalizează_task(self, nume):
        self.todo_List.pop(nume)

    def afișează_todo_list(self):
        print(self.todo_List.keys())

    def afișează_detalii_suplimentare(self,nume_task):
        if nume_task not in self.todo_List.keys():
            raspuns = input("Doresti sa il adaugi taskul: ")
            if raspuns == "nu":
                print("La revedere")
            else:
                detalii = input("intro detalii task:")
                self.todo_List.update({nume_task: detalii})

        else:
            print({self.todo_List.get(nume_task)})

task = TodoList()
task.adauga_task("Trezirea", "Ne trezim la 10 dimineata")
task.afișează_detalii_suplimentare("Trezirea")
task.finalizează_task("Trezirea")
task.afișează_detalii_suplimentare("Trezirea")
task.afișează_detalii_suplimentare("Trezirea")
