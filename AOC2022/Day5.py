file = open("Day5.txt", 'r')

values = [x.strip() for x in file]
count = 0
initial_positions = [[],[],[],[],[],[],[],[],[]]
for i in range(7,-1,-1):
    for pos, i in enumerate(values[i].split(" ")):
        if i != '[#]':
            initial_positions[pos].append(i[1])
print(initial_positions)

for i in values[10:]:
    move = i.split(" ")
    print(move)
    number = int(move[1])
    from_pos = int(move[3]) -1
    to = int(move[5]) -1
    for _ in range(number):
        initial_positions[to].append(initial_positions[from_pos][-1])
        initial_positions[from_pos] = initial_positions[from_pos][:-1]

print(initial_positions)
print([i[-1]for i in initial_positions])



initial_positions = [[],[],[],[],[],[],[],[],[]]
for i in range(7,-1,-1):
    for pos, i in enumerate(values[i].split(" ")):
        if i != '[#]':
            initial_positions[pos].append(i[1])
print(initial_positions)

for i in values[10:]:
    move = i.split(" ")
    print(move)
    number = int(move[1])
    from_pos = int(move[3]) -1
    to = int(move[5]) -1

    initial_positions[to] = initial_positions[to] + initial_positions[from_pos][-number:]
    initial_positions[from_pos] = initial_positions[from_pos][:-number]

print(initial_positions)
print([i[-1]for i in initial_positions])