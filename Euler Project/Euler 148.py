
total_rows = 10**9

 

lookup = {0:0,1:1,2:3,3:6,4:10,5:15,6:21}

 

row_length = 1

row_size = 1

num_of_vals = 1

while row_length*7<= total_rows:

    row_length*=7

    row_size *=28

 

total_values = 0

 

rows_left = total_rows

while rows_left != 0:

    x = divmod(rows_left, row_length)

 

    total_values+=row_size*lookup[x[0]] * num_of_vals

    rows_left = x[1]

    num_of_vals*=(x[0]+1)

 

    #go down...

    row_length = row_length //7

    row_size = row_size // 28

 

print(total_values)
