
#just ensuring that the correct value isn't passed

goal_value = 1000
max_value = 10000
maximum = 0
values = [0]*max_value
addend = 1
position = 1
while position <max_value and values[position]<goal_value:
    maximum = max(maximum, values[position])
    while position < max_value:
        values[position]+=1
        position+=addend
    addend+=1
    position = addend

print(maximum)

print(values[1260])