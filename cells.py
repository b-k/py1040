def CV(label):
    return cell_list[label].value

class cell():
    def __init__(self, name, line, calc, parents, flag='c', situation=True):
        self.name=name
        self.form=None
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

#2014 tax rate schedules
def tax_calc(inval):
    if inval < 9075: return .1*907.50
    if inval < 36900: return 907.50  + .15*(inval-9075)
    if inval < 89350: return 5081.25 + .25*(inval-36900)
    if inval < 186350: return 18193.75 + .28*(inval-89350)
    if inval < 405100: return 45353.75 + .33*(inval-186350)



cell_list = dict()

f1040 = dict(
taxable_income = cell('taxable income', 55, '1', (None)),
tax = cell('tax', 56, "tax_calc(CV('taxable_income'))", ('taxable_income',)),
withheld = cell('withheld', 57, 'withheld_fed', (None), 'u'),
owed = cell('taxes owed', 58, 'CV("tax")-CV("withheld") if (CV("withheld") < CV("tax")) else 0', ('withheld', 'tax'))
)


def add_a_form(name):
    global cell_list
    for i in eval(name).values():
        i.form=name
    cell_list =dict(list(cell_list.items()) + list(eval(name).items()))

add_a_form('f1040')

def setup_inform():
    f = open("inform.py", "w")
    for i in cell_list.values():
        if (i.flag=='u'):
            f.write(
"""
#%s
%s = 0
""" % (i.name, i.calc))
    f.close



import pathlib, sys
if (not pathlib.Path("inform.py").exists()):
    setup_inform()
    print("Have generated inform.py. Please fill it in and rerun this script.")
    sys.exit(1)

from inform import *

print(cell_list['owed'].name, cell_list['owed'].compute())
