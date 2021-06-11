#simple code adding valus of list increasing 1 step of index.
#x is a list given by grasshopper.

sum_list= []
n= len(x)
print n

guide = 1

while guide < n+1:
    y=sum(x[0:guide])
    sum_list.append(y)
    guide += 1

a = sum_list
