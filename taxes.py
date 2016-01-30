def CV(label):
    return cell_list[label].value

exec(open("cells.py").read())

def add_a_form(name):
    global cell_list
    for i in eval(name).values():
        i.form=name
    cell_list =dict(list(cell_list.items()) + list(eval(name).items()))


exec(open("forms/f1040.py").read())
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

print(cell_list['refund'].name, cell_list['refund'].compute())
print(cell_list['tax_owed'].name, cell_list['tax_owed'].compute())
