file = open("Day12.txt", 'r')
values = [x.strip() for x in file]

heightmap = []
start = (0,0)
end = (0,0)
for y, line  in enumerate(values):
    temp = []
    for x, char in enumerate(line):
        if char == 'S':
            start = (x,y)
            temp.append(0)
        elif char == 'E':
            end = (x,y)
            temp.append(25)
        else:
            temp.append(ord(char)-ord('a'))
    heightmap.append(temp)

endfound = False

checked_squares = [start]
to_check_squares = [start]
iters = 0
dirs = ((0,1),(0,-1),(1,0),(-1,0))
while not endfound:
    iters+=1
    new_check = []
    for i in to_check_squares:
        #check up down left right
        for dir in dirs:
            new_x = i[0]+dir[0]
            new_y = i[1]+dir[1]
            if new_x < len(heightmap[0]) and new_x >=0 and new_y< len(heightmap) and new_y>=0:
                if (new_x, new_y) not in checked_squares and heightmap[i[1]][i[0]]+1>=heightmap[new_y][new_x]:
                    if (new_x, new_y) == end:
                        endfound = True
                        break
                    else:
                        if (new_x, new_y) not in new_check:
                            new_check.append((new_x,new_y))
        checked_squares.append(i)
    to_check_squares = new_check

print(iters)




checked_squares = [end]
to_check_squares = [end]
iters = 0
endfound = False
dirs = ((0,1),(0,-1),(1,0),(-1,0))
while not endfound:
    iters+=1
    new_check = []
    for i in to_check_squares:
        #check up down left right
        for dir in dirs:
            new_x = i[0]+dir[0]
            new_y = i[1]+dir[1]
            if new_x < len(heightmap[0]) and new_x >=0 and new_y< len(heightmap) and new_y>=0:
                if (new_x, new_y) not in checked_squares and heightmap[i[1]][i[0]]-1 <= heightmap[new_y][new_x]:
                    if heightmap[new_y][new_x] == 0:
                        endfound = True
                        break
                    else:
                        if (new_x, new_y) not in new_check:
                            new_check.append((new_x,new_y))
        checked_squares.append(i)
    to_check_squares = new_check

print(iters)
