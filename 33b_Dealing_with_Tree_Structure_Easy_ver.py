import ghpythonlib.treehelpers as th

#Using ghpythonlib.treehelpers, Grasshopper Tree strcuture can easily converted into nested list in python.
#Opposite direction, converting nested list into tree is also possible.
#There are two options for this function. 
#When retrieve_base is set to None, it will return all lists.
#In contrast and when it is default(no condition), it will only return first list of a tree.

a = th.tree_to_list(x,retrieve_base=None)
print a
