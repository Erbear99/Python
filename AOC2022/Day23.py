file = open("Day23.txt", 'r')

elf_locations = {(x,y):(x,y) for y, line in enumerate(file) for x, val in enumerate(line) if val == '#'}
num_of_elves = len(elf_locations)

directions  = [[(0,-1), (-1,-1), (1,-1)], [(0,1), (-1,1), (1,1)], [(-1,0), (-1,1), (-1,-1)], [(1,0), (1,1), (1,-1)]]
round = 0
while True:
    round+=1
    new_locations = {}
    colisions = []
    moved = False
    for elf in elf_locations:
        temp_map = {(elf[0]+x,elf[1]+y):elf_locations.get((elf[0]+x,elf[1]+y)) for x in range(-1,2) for y in range(-1,2) if (x!=0 or y!=0) and elf_locations.get((elf[0]+x,elf[1]+y)) is not None}
        if len(temp_map) > 0:
            found = False
            for d1,d2,d3 in directions:
                if temp_map.get((elf[0]+d1[0], elf[1]+d1[1])) is None and temp_map.get((elf[0]+d2[0], elf[1]+d2[1]))  is None and temp_map.get((elf[0]+d3[0], elf[1]+d3[1])) is None:
                    found = True
                    moved = True
                    if new_locations.get((elf[0]+d1[0],elf[1]+d1[1])) is None:
                        new_locations[(elf[0]+d1[0],elf[1]+d1[1])] = elf
                    else:
                        new_locations[elf] = elf
                        if (elf[0]+d1[0],elf[1]+d1[1]) not in colisions:
                            colisions.append((elf[0]+d1[0],elf[1]+d1[1]))
                    break
            if not found:
                new_locations[elf] = elf
        else:
            new_locations[elf] = elf
    
    for colision in colisions:
        original_pos = new_locations[colision]
        del new_locations[colision]
        new_locations[original_pos] = original_pos
    directions = directions[1:]+[directions[0]]
    elf_locations = new_locations
    if not moved:
        print(round)
        break
    if round == 10:
        maxx,maxy, minx,miny = 0,0,0,0
        for x,y in elf_locations:
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
            
        print((maxx-minx+1) * (maxy-miny+1) - num_of_elves)


#get max x ,minx, maxy, miny

