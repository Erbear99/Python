file = open("Day9.txt", 'r')

values = [x.strip() for x in file]


head, tail = (0,0), (0,0)
tail_pos = [(0,0)]

for i in values:
    instr = i.split(" ")
    for move in range(int(instr[1])):
        if instr[0] == 'U':
            old_head = head
            head = (head[0],head[1]+1 )
            if abs(tail[0]-head[0])>1 or abs(tail[1]-head[1])>1:
                tail = old_head
                tail_pos.append(old_head)
        if instr[0] == 'D':
            old_head = head
            head = (head[0],head[1]-1 )
            if abs(tail[0]-head[0])>1 or abs(tail[1]-head[1])>1:
                tail = old_head
                tail_pos.append(old_head)
        if instr[0] == 'L':
            old_head = head
            head = (head[0]-1,head[1] )
            if abs(tail[0]-head[0])>1 or abs(tail[1]-head[1])>1:
                tail = old_head
                tail_pos.append(old_head)
        if instr[0] == 'R':
            old_head = head
            head = (head[0]+1,head[1])
            if abs(tail[0]-head[0])>1 or abs(tail[1]-head[1])>1:
                tail = old_head
                tail_pos.append(old_head)
print(len(set(tail_pos)))


tails =  [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
tail_pos = [(0,0)]

for i in values:
    instr = i.split(" ")
    for move in range(int(instr[1])):
        addend = (0,0)
        print(tails)
        if instr[0] == 'U':
            addend = (0,1)
        if instr[0] == 'D':
            addend = (0,-1)
        if instr[0] == 'L':
            addend = (-1,0)
        if instr[0] == 'R':
            addend = (1,0)

        tails[0] = (tails[0][0]+addend[0],tails[0][1]+addend[1])

        for pos, tail in enumerate(tails):
            if pos == 0:
                continue
            horiz_dir= tails[pos-1][0]-tail[0]
            vert_dir = tails[pos-1][1]-tail[1]
            if abs(horiz_dir)>1 or abs(vert_dir)>1:
                if abs(horiz_dir)>0 and abs(vert_dir)>0:
                    horiz_addend = 0
                    vert_addend = 0
                    if horiz_dir < 0: 
                        horiz_addend = -1
                    else:
                        horiz_addend = 1
                    if vert_dir < 0:
                        vert_addend = -1
                    else:
                        vert_addend = 1
                    tails[pos] = (tail[0]+horiz_addend, tail[1]+vert_addend)

                else:
                    if abs(horiz_dir)>0:
                        tails[pos] = (tail[0]+horiz_dir//2, tail[1])
                    else:
                        tails[pos] = (tail[0], tail[1]+vert_dir//2)
                if pos == 9:
                    tail_pos.append(tails[pos])
            else:
                break
print(len(set(tail_pos)))
