import rhinoscriptsyntax as rs
import Grasshopper.DataTree as dt

#step 1. Expand tree structure and append the results to python list.
n_of_branches = x.BranchCount
gh_to_py_listlist = []

for i in range(n_of_branches):
    gh_to_py_listlist.append(x.Branch(i)) 
    # x.Branch(i) = A list in each branch
    # Append lists to prepared python list

#step 2. Manipulating data and storing
new_list = []
for list in gh_to_py_listlist: 
    list = [2*i for i in list] #Manipulating original data
    new_list.append(list)
        

#step 3. Reorganizing python list to Grasshopper tree structure.
convert_list = dt[object]()
paths = x.Paths
for i in range(n_of_branches):
    convert_list.AddRange(new_list[i], paths[i])
    
a = convert_list
