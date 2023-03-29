class Curs_Programare():

    def __init__(self, companie, nume, durata, nr_locuri):
        self.companie = companie
        self.nume = nume
        self.durata =durata
        self.nr_locuri = nr_locuri
        self.studenti = []

    def descriere_curs(self):
        print(f"{self.companie} - {self.nume} - {self.durata} zile")
        print("-"*30)
        if len(self.studenti) > 0:
            for student in self.studenti:
                print(f"{student.nume} {student.prenume}")
        else:
            print(f"Nu sunt studenti inscrisi")
    def inscriere_student(self, student):
        if self.get_nr_locuri_disponibile() > 0:
            self.studenti.append(student)
        else:
            print("Nu mai sunt locuri disponibile")

    def get_nr_locuri_disponibile(self):
        return self.nr_locuri - len(self.studenti)