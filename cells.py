cell_list = dict()

class cell():
    def __init__(self, name, line, calc, parents=(None), flag='c', situation=True):
        self.name=name
        self.line=line
        self.parents=parents
        self.calc=calc
        self.done=False
        self.value=0
        self.flag=flag
        self.situation=situation

    def check_done(self):
        print("checking", self.name)
        if (self.situation == False): return True
        out = self.done
        if (not out): return False
        if (self.parents != None):
            for i in self.parents:
                if (not cell_list[i].check_done()): return False
        return True

    def compute(self):
        if (self.done): return self.value

        if (self.parents != None):
            for i in self.parents:
                print(cell_list[i].name, ": computing ", cell_list[i].calc)
                cell_list[i].compute()
            for i in self.parents:
                if (not cell_list[i].check_done()):
                    print("Missing dependency for", self.name, "; need", cell_list[i].name)
                    return False
        self.value = eval(self.calc)
        print(self.name, "is now ", self.value)
        self.done=True
