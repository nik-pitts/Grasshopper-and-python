#Dealing with tree data structure in Grasshopper python component.

import rhinoscriptsyntax as rs
# to handle tree data structure using python, must import Grasshopper.DataTree module.
import Grasshopper.DataTree as dt

# Extracting numbers of branches from data structure.
Number_of_branches = x.BranchCount
# convert_tree list will be used when reorganizing python list to grasshopper tree structured data.
convert_tree = dt[object]()

# Step1. Expand tree structure and append the result to python list structure.
gh_to_py_list = []

for i in range(Number_of_branches):
    gh_to_py_list.append(x.Branch(i))

print gh_to_py_list

# Step2. Manipulating data using python syntax and structure.
for list in gh_to_py_list:
    for i in list:
        print i

# Step3. Reorgazning python data to Grasshopper tree structure.
paths = x.Paths
for i in range(Number_of_branches):
    convert_tree.AddRange(gh_to_py_list[i], paths[i])

a = convert_tree
