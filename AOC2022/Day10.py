file = open("Day10.txt", 'r')

values = [x.strip() for x in file]
cycle = 1
register = 1
cycles = [20,60, 100, 140, 180, 220]
total = 0
for x in values:
    instr = x.split(" ")
    if instr[0] == 'noop':
        cycle+=1
        if cycle in cycles:
            total+=cycle*register
            print(total)
    else:
        cycle+=1
        if cycle in cycles:
            total+=cycle*register
            print(total)
        cycle+=1
        register+=int(instr[1])
        if cycle in cycles:
            total+=cycle*register
            print(total)

print(total)


cycle = 0
register = 1
cycles = 40
for x in values:
    instr = x.split(" ")
    if instr[0] == 'noop':
        if abs((cycle%40)-register)<=1:
            print('#', end='')
        else:
            print('.', end='')
        if (cycle+1) %cycles== 0:
            print("")
        cycle+=1
    else:
        if abs((cycle%40)-register)<=1:
            print('#', end='')
        else:
            print('.', end='')
        if (cycle+1) %cycles== 0:
            print("")
        cycle+=1
        if abs((cycle%40)-register)<=1:
            print('#', end='')
        else:
            print('.', end='')
        if (cycle+1) %cycles== 0:
            print("")
        cycle+=1
        register+=int(instr[1])
