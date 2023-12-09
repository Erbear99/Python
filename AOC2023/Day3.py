rows = [[y for y in x.strip()] for x in open("AOC2023/Day3.txt").readlines()]

height = len(rows)
width = len(rows[0])

curr_x = 0
curr_row = 0
total = 0
gear_ratio = {}
while curr_row <height:
    if rows[curr_row][curr_x] in "0123456789":
        #get the total of the number
        current_number = ""
        while curr_x < width and rows[curr_row][curr_x] in "0123456789":
            current_number+=rows[curr_row][curr_x]
            curr_x+=1
        #check the surrounding digits for symbols
        valid = False
        for y in range(curr_row-1, curr_row+2):
            for x in range(curr_x-len(current_number)-1, curr_x+1):
                if y>0 and y< height and x>0 and x<width:
                    if rows[y][x] not in ".0123456789":
                        if rows[y][x] == '*':
                            if gear_ratio.get((x,y)) is None:
                                gear_ratio[(x,y)] = [int(current_number)]
                            else:
                                gear_ratio[(x,y)].append(int(current_number))
                        valid = True
        if valid:
            total+=int(current_number)
    else:
        curr_x+=1
    if curr_x == width:
        curr_x = 0
        curr_row +=1

print(total)
print(sum([gear_ratio[x][0]*gear_ratio[x][1] for x in gear_ratio if len(gear_ratio[x]) == 2]))

