file = open("Day18.txt", 'r')
values = [[int(z) for z in x.strip().split(',')] for x in file]
claimed_vals = []
sides =0

dirs = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
maxx=0
val_start = ()
for x,y,z in values:
    count = 6
    if x>maxx:
        val_start = (x+1,y,z)
        maxx = x
    for dx,dy,dz in dirs:
        if (x+dx, y+dy, z+dz) in claimed_vals:
            count-=2
    sides+=count
    claimed_vals.append((x,y,z))

print(sides)

values_checked = [val_start]
val_to_check = [val_start+(0,)]
total_exposed_sides = 0

while len(val_to_check) > 0:
    new_vals = {}
    for x,y,z,distance in val_to_check:
        #check for sides 
        non_exposed_sides = []
        exposed_sides = 0
        for dx,dy,dz in dirs:
            if (dx+x, dy+y, dz+z) in claimed_vals:
                exposed_sides+=1
            else:
                non_exposed_sides.append((dx+x, dy+y, dz+z))
        total_exposed_sides +=exposed_sides
        if exposed_sides == 0:
            if distance<=1:
                for x in non_exposed_sides:
                    if x not in values_checked and (new_vals.get(x) is None or new_vals.get(x) >distance):
                        new_vals[x] = distance+1
        else:
            for x in non_exposed_sides:
                if x not in values_checked:
                    new_vals[x] = 0
    val_to_check = [x+(new_vals[x],) for x in new_vals]
    values_checked = values_checked+[x for x in new_vals]

print(total_exposed_sides)

                    