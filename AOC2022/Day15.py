file = open("Day15.txt", 'r')
values = [x.strip() for x in file]

beacons = []
ranges = []
max_row = 2000000
for row in values:
    temp = row.split(" ")
    startx = int(temp[2][2:-1])
    starty = int(temp[3][2:-1])
    endx = int(temp[8][2:-1])
    endy = int(temp[9][2:])
    if endy == max_row:
        beacons.append((endx, endy))
    calc_distance = abs(startx-endx)+abs(starty-endy)

    row_dist = abs(starty-max_row)
    row_start = startx-(calc_distance-row_dist)
    row_end = startx+(calc_distance-row_dist)
    append_val = True

    if row_start<=row_end:
        ranges.append((row_start, row_end))


def sort_order(e):
    return e[0]

ranges.sort(key=sort_order)
total = 0
range_final = None
for range_start, range_end in ranges:
    if range_final is None or range_start > range_final:
        total+= range_end-range_start + 1
        range_final = range_end
    elif range_start <= range_final and range_end> range_final:
        total+= range_end-range_final
        range_final = range_end
print(total-len(set(beacons)))


maxval = 4000000
coordinates = []
for row in values:
    temp = row.split(" ")
    startx = int(temp[2][2:-1])
    starty = int(temp[3][2:-1])
    endx = int(temp[8][2:-1])
    endy = int(temp[9][2:])
    calc_distance = abs(startx-endx)+abs(starty-endy)
    coordinates.append((startx, starty, calc_distance))


#first one needs to go down, second needs to go up

#Determine intersections of beacon radai +1 and then solve based on that.

connections = []

for pos, beacon in enumerate(coordinates):
    for beacon2 in coordinates[pos:]:
        if beacon != beacon2:
            if abs(beacon[0]-beacon2[0])+abs(beacon[1]-beacon2[1]) - (beacon[2]+beacon2[2]) ==2:
                connections.append((beacon, beacon2))


firstval = ()
secondval = ()
for b1, b2 in connections:
    print()
    if b1[2] > b2[2]:
        print("first")
        #move to same x
        b1x = b2[0]
        b1y = b1[1]-(b1[2]-(b2[0]-b1[0]))
        print(b1x,b1y)
        b2x = b2[0]
        b2y = b2[1]+b2[2]
        print(b2x,b2y)
    else:
        print("second")
        #move to same x
        b2x = b1[0]
        b2y = b2[1]-(b2[2] - (b2[0]-b1[0]))
        print(b2x,b2y)
        b1x = b2x
        b1y = b1[1]+b1[2]
        print(b1x,b1y)

firstval = (2925882, 3423709)
secondval = (2459256, 3363121)
print(firstval[0]-secondval[0])
print(firstval[1]-secondval[1])
x = 263607
y = 203019
print(firstval[0]-x, firstval[1]-x)
print(secondval[0]+y, secondval[1]-y)

print(4000000*2662275 + 3160102)
