list = []
for i in range(1,56):
    list.append((100003-200003*i+300007*i**3)%1000000 -500000)
for i in range(56,4000001):
    list.append((list[i-25]+list[i-56]+1000000)%1000000 - 500000)


max_val = 0
#height and width decision
horizontal_sum = 0
vertical_sum = 0

for i in range(2000):
    horizontal_sum = 0
    vertical_sum = 0
    for j in range(2000):
        horizontal_sum += list[i*2000+j]
        vertical_sum += list[j*2000+i]
        horizontal_sum = max(horizontal_sum, 0)
        vertical_sum = max(vertical_sum, 0)
        max_val = max(horizontal_sum, vertical_sum, max_val)

#do the diagonal calculation
#go down the left wall (top wall) then down the bottom wall (right wall)
diagonal_up_left_sum = 0
diagonal_up_down_sum = 0
diagonal_down_left_sum = 0
diagonal_down_up_sum = 0

max_diag = 0
for i in range(2000):
    #define the first point to be a value on the line...
    diagonal_up_left_sum = 0
    diagonal_up_down_sum = 0
    diagonal_down_left_sum = 0
    diagonal_down_up_sum = 0
    #diagonal_up_left
    for j in range(i+1):
        diagonal_up_left_sum += list[2000*(i-j)+j]
        diagonal_up_left_sum = max(diagonal_up_left_sum,0)
        max_diag = max(diagonal_up_left_sum, max_diag)

    #diagonal_up_down
    for j in range(i+1):
        diagonal_up_down_sum += list[4000000-((i-j)+1)-2000*j]
        diagonal_up_down_sum = max(diagonal_up_down_sum,0)
        max_diag = max(diagonal_up_down_sum, max_diag)
    #diagonal_down_left
    for j in range(i+1):
        diagonal_down_left_sum += list[4000000-2000*((i-j)+1)+j]
        diagonal_down_left_sum = max(diagonal_down_left_sum,0)
        max_diag = max(diagonal_down_left_sum, max_diag)

    #diagonal_down_up
    for j in range(i+1):
        diagonal_down_up_sum += list[1999-(i-j)+2000*j]
        diagonal_down_up_sum = max(diagonal_down_up_sum,0)
        max_diag = max(diagonal_down_up_sum, max_diag)


print(max_val,max_diag)




