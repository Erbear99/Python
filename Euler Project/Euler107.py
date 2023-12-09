matrix = [[''if y=='-' else int(y) for y in x.split(',')] for x in open('C:/Users/Erik/Programming Projects/Python/Euler Project/p107_network.txt','r').read().split('\n')]
#each row in the matrix represents a new point 
#each column also represents a row


#start with one row, each "round" select an additional row from the options available in the rows you have
#only keep the best version of each "set"

#generate order of smallest distances since we want to use the smallest distance available

sorted_order = sorted([(val,x,y) for y,row in enumerate(matrix) for x, val in enumerate(row) if x<y and val != ''], key=lambda a: a[0])
#each row has the connections to the other rows sorted from the best at the begining and the worst at the end.
print(sorted_order)


#go through the sorted list and add edges one at a time
list_of_sets = []
number_ownership = {}
total = 0
for value, x ,y in sorted_order:
    x_ownership = number_ownership.get(x)
    y_ownership = number_ownership.get(y)

    if x_ownership is None and y_ownership is None:
        number_ownership[x] = len(list_of_sets)
        number_ownership[y] = len(list_of_sets)
        list_of_sets.append([x,y])
        total+=value
    if x_ownership == y_ownership:
        continue
    else:
        total+=value
    if x_ownership is None and y_ownership is not None:
        number_ownership[x] = y_ownership
        list_of_sets[y_ownership].append(x)
    if y_ownership is None and x_ownership is not None:
        number_ownership[y] = x_ownership
        list_of_sets[x_ownership].append(y)
    if x_ownership is not None and y_ownership is not None and y_ownership != x_ownership:
        #find the minimum of the sets, move all the values over
        minimum = min(y_ownership, x_ownership)
        maximum = max(y_ownership, x_ownership)
        for val in list_of_sets[maximum]:
            list_of_sets[minimum].append(val)
            number_ownership[val] = minimum
        list_of_sets[maximum] = []

print(sum([x[0] for x in sorted_order])-total)
print(total)