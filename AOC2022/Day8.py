file = open("Day8.txt", 'r')

values = [[int(y) for y in x.strip()] for x in file]

visable = []
size = 0
dirs = ((0,1),(0,-1),(1,0),(-1,0))
for y, line in enumerate(values):
    for x, value in enumerate(line):
        found = False
        for direction, dir in enumerate(dirs):
            new_x = x+dir[0]
            new_y = y+dir[1]
            while True:
                if new_y > 98 or new_y <0 or new_x > 98 or new_x <0:
                    found = True
                    break
                if values[new_y][new_x] >= value:
                    break
                new_x+=dir[0]
                new_y+=dir[1]
            if found:
                size+=1
                break
print(size)

max_score = 0

for y, line in enumerate(values):
    for x, value in enumerate(line):
        score = 1
        for  dir in dirs:
            count = 0
            new_x = x+dir[0]
            new_y = y+dir[1]
            while new_x >=0 and new_x <=98 and new_y >=0 and new_y <=98 :
                count+=1
                if values[new_y][new_x] >= value:
                    break
                new_x+=dir[0]
                new_y+=dir[1]
            score*=count
        if score > max_score:
            max_score=score
print(max_score)

            
