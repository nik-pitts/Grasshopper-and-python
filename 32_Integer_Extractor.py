#when number with no remainder is represented type of float,
#this components only extracts floats with no remainder which can be integer.

int_list = []

for i in x:
    if i.is_integer():
        int_list.append(i)

a = int_list
