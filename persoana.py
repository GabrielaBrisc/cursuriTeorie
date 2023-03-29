class Persoana:

    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta

    def prezentare(self):
        print(self.nume, self.prenume, self.varsta)
    def varsta_peste_10_ani(self):
        return self.varsta + 10
