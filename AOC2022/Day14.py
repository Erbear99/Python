file = open("Day14.txt", 'r')
values = [x.strip() for x in file]


map = [['.' for _ in range(500)] for _ in range(200)]

x_offset = 450
maxy = 167

for x in values:
    line = x.split(" -> ")
    for oper in range(len(line)-1):
        start = [int(z) for z in line[oper].split(",")]
        end = [int(z) for z in line[oper+1].split(",")]
        if start[0] == end[0]:
            for y_change in range(min(start[1], end[1]), max(start[1], end[1])+1):
                map[y_change][start[0]-x_offset] = '#'
        else:
            for x_change in range(min(start[0], end[0]), max(start[0], end[0])+1):
                map[start[1]][x_change-x_offset] = '#'

for x in range(500):
    map[169][x] = '#'

# generate sand
count = 0
sand_piling = True
starting_x = 500-x_offset
starting_y = 0
while sand_piling:
    #move a grain
    x = starting_x
    y = starting_y
    if map[starting_y][starting_x] == '+':
        break
    moving = True
    while moving:
        if map[y+1][x] == '.':
            y+=1
            continue
        if map[y+1][x-1]== '.':
            y+=1
            x-=1
            continue
        if map[y+1][x+1] == '.':
            y+=1
            x+=1
            continue
        else:
            count+=1
            map[y][x] = '+'
            break


print(count)