class cell():
    def __init__(self, text, line, calc='0', flag='c', situation=True, name='x', form='1040'):
        self.text=text
        self.line=line
        self.name=name
        self.calc=calc
        self.done=False
        self.value=0
        self.flag=flag
        self.situation=situation
        self.form=form

    def check_done(self):
        #print("checking", self.name)
        if (self.situation == False): return True
        out = self.done
        if (not out): return False
        parents = deps[self.name]
        if (parents != None):
            for i in parents:
                if (i==""): continue
                if (not cell_list[i].check_done()): return False
        return True

    def compute(self):
        if debug: print ("Checking "+self.name, flush=True)
        if self.done:
            if debug: print ("  Got "+str(self.value), flush=True)
            return self.value

        parents = deps[self.name]
        if (parents != None):
            for i in parents:
                if (i==""): continue
                cell_list[i].compute()
            for i in parents:
                if (i==""): continue
                if (not cell_list[i].check_done()):
                    print("Missing dependency for\t", self.name, "; need", cell_list[i].name)
                    return False
        if debug: print ("Computing\t" + self.name + ":\t" +self.calc, flush=True)
        self.value = eval(self.calc)
        if debug: print ("  For ", self.name, " got:\t", str(self.value), flush=True)
        self.done=True
