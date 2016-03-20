def CV(label):
    return cell_list[label].value

exec(open("cells.py").read())

def add_a_form(name):
    global cell_list
    cell_list =dict(list(cell_list.items()) + list(eval(name).items()))


def setup_inform(print_out):
    if not print_out:  #Just adjust the calcs
        for i in cell_list.items():
            if (i[1].flag.find('u')>-1):
                i[1].calc="%s" %(i[0],)
        return

    f = open("inform.py", "w")
    for i in cell_list.items():
        if (i[1].flag.find('u')>-1):
            f.write(
"""
#%s
%s = 0
""" % (i[1].name, i[0]))
    f.close



def print_a_form(name, inlist):
    print(">>>>>>>>>> %s <<<<<<<<<" %(name,))
    out=list()
    for i in inlist.keys():
        if (show_optional_zeros or cell_list[i].value != 0 or cell_list[i].flag.find('o')==-1) and cell_list[i].line>0:
            out.append((cell_list[i].line, cell_list[i].name, cell_list[i].value))
    out.sort()
    max_len = 0
    for i in out:
    	max_len = max(max_len, len(i[1]))
    for i in out:
    	print("%4g | %*s | %g" %( i[0], max_len, i[1], i[2]))

def clear_done_flags(start):
    cell_list[start].done=False
    parents = cell_list[start].parents
    if (parents != None):
        for i in parents:
            clear_done_flags(i)

def print_the_tree(starting_cell, level=0):
    if level==0:
        clear_done_flags(starting_cell)
    print("%s├ %s=%g" % ("│   "*level, starting_cell, CV(starting_cell)))
    parents = cell_list[starting_cell].parents
    if (parents != None):
        print("%s├───┐" % ("│   "*level))
        for i in parents:
            if (cell_list[i].situation and not cell_list[i].done):
                print_the_tree(i, level+1)
                cell_list[i].done=True

def get_maxcell(starting_cell, maxsofar=0, level=0):
    maxsofar = max(maxsofar, cell_list[starting_cell].value)
    parents = cell_list[starting_cell].parents
    if (parents != None):
        for i in parents:
            maxsofar = max(maxsofar, get_maxcell(i, maxsofar, level+1))
    return maxsofar

def print_to_graphviz(starting_cell, f, maxval, level=0):
    parents = cell_list[starting_cell].parents
    if (parents != None):
        for i in parents:
            f.write("%s [height=%g] -> %s [height=%g]\n" % (i, 72*cell_list[i].value/maxval, starting_cell, 72*cell_list[starting_cell].value/maxval))
            print_to_graphviz(i, f, maxval, level+1)

# The main routine: build interview and inform, calculate taxes, print

# The main routine: build interview and inform, calculate taxes, print
status="no interview yet"

import pathlib, sys
from shutil import copyfile
if (not pathlib.Path("interview.py").exists()):
    copyfile("forms/interview_template.py", "interview.py")
    print("Have generated interview.py. Please fill it in and rerun this script.")
    sys.exit(1)

exec(open("interview.py").read())
if (status=="no interview yet"):
    print("Please follow the steps in interview.py and rerun this script.")
    sys.exit(1)

from interview import *

import os
import pdb
for f in os.listdir('forms'):
    #pdb.set_trace()
    fsplit=f.partition('.')
    if f=='interview_template.py' or fsplit[2]!="py": continue
    exec(open("forms/"+f).read())
    add_a_form(fsplit[0])

if (not pathlib.Path("inform.py").exists()):
    setup_inform(print_out=True)
    print("Have generated inform.py. Please fill it in and rerun this script.")
    sys.exit(1)

from inform import *
setup_inform(print_out=False)

cell_list['refund'].compute()
cell_list['tax_owed'].compute()
print_a_form("Form 1040", f1040)
if itemizing:
    print_a_form("Schedule A", schedule_a)
if have_rr:
    print_a_form("Schedule E", schedule_e)
    print_a_form("Form 8582", f8582)

#print("\n")
#print_the_tree('refund')
f=open("graph.dot", "w")
#f.write("digraph {")
maxval=get_maxcell('refund')
print("MAXVAL: %g" %(maxval,))
print_to_graphviz('refund', f, maxval)
#f.write("}")
f.close()
