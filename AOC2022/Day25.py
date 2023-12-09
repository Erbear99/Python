file = open('Day25.txt', 'r')



sum = 0
for line in file:
    total = 0
    for pos, value in enumerate(line.strip()):
        multiple = 5**(len(line.strip())-(pos+1))
        if value == '2':
            total+=multiple*2
        elif value == '1':
            total+=multiple*1
        elif value == '0':
            total+=multiple*0
        elif value == '-':
            total+=multiple*-1
        elif value == '=':
            total+=multiple*-2
    sum+=total
        

print(sum)