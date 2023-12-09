file = open("Day24.txt", 'r')

#bredth first search
#generate blizzards and their directions
values = [line.strip() for line in file]
height = len(values)-2
width = len(values[0])-2

leftblizzards = {(x-1, y-1):direction for y, line in enumerate(values) for x,direction in enumerate(line) if direction == '<'}
rightblizzards = {(x-1, y-1):direction for y, line in enumerate(values) for x,direction in enumerate(line) if direction == '>'}
upblizzards = {(x-1, y-1):direction for y, line in enumerate(values) for x,direction in enumerate(line) if direction == '^'}
downblizzards = {(x-1, y-1):direction for y, line in enumerate(values) for x,direction in enumerate(line) if direction == 'v'}




possibilities = [(0, -1)]
notfound = True
moves = 0
while notfound:
    moves+=1
    new_options = []
    #do each of five options
    for px, py in possibilities:
        if leftblizzards.get((px,py)) is None and rightblizzards.get((px,py)) is None and upblizzards.get((px,py)) is None and downblizzards.get((px,py)) is None:
            if px == width-1 and py == height-1:
                print(moves)
                notfound = False
                break
            #move up
            new_options.append((px,py))
            if py>0:#move up
                new_options.append((px,py-1))
            if py <(height-1):#move down
                new_options.append((px,py+1))
            if px>0 and py!=-1:#move left
                new_options.append((px-1, py))
            if px<(width-1) and py!=-1:#move right
                new_options.append((px+1,py))
    #update blizzards
    new_left = {}
    for bx,by in leftblizzards:
        new_left[((bx-1)%width,by)] = '<'
    leftblizzards = new_left
    new_right = {}
    for bx,by in rightblizzards:
        new_right[((bx+1)%width,by)] = '>'
    rightblizzards = new_right
    new_up = {}
    for bx,by in upblizzards:
        new_up[(bx,(by-1)%height)] = '^'
    upblizzards = new_up
    new_down = {}
    for bx,by in downblizzards:
        new_down[(bx,(by+1)%height)] = 'v'
    downblizzards = new_down
    possibilities = set(new_options)


possibilities = [(width-1, height)]
notfound = True
while notfound:
    moves+=1
    new_options = []
    #do each of five options
    for px, py in possibilities:
        if leftblizzards.get((px,py)) is None and rightblizzards.get((px,py)) is None and upblizzards.get((px,py)) is None and downblizzards.get((px,py)) is None:
            if px == 0 and py == 0:
                notfound = False
                break
            #move up
            new_options.append((px,py))
            if py>0:#move up
                new_options.append((px,py-1))
            if py <(height-1):#move down
                new_options.append((px,py+1))
            if px>0 and py!=-1 and py!=height:#move left
                new_options.append((px-1, py))
            if px<(width-1) and py!=-1 and py!=height:#move right
                new_options.append((px+1,py))
    #update blizzards
    new_left = {}
    for bx,by in leftblizzards:
        new_left[((bx-1)%width,by)] = '<'
    leftblizzards = new_left
    new_right = {}
    for bx,by in rightblizzards:
        new_right[((bx+1)%width,by)] = '>'
    rightblizzards = new_right
    new_up = {}
    for bx,by in upblizzards:
        new_up[(bx,(by-1)%height)] = '^'
    upblizzards = new_up
    new_down = {}
    for bx,by in downblizzards:
        new_down[(bx,(by+1)%height)] = 'v'
    downblizzards = new_down
    possibilities = set(new_options)



            
possibilities = [(0, -1)]
notfound = True
while notfound:
    moves+=1
    new_options = []
    #do each of five options
    for px, py in possibilities:
        if leftblizzards.get((px,py)) is None and rightblizzards.get((px,py)) is None and upblizzards.get((px,py)) is None and downblizzards.get((px,py)) is None:
            if px == width-1 and py == height-1:
                print(moves)
                notfound = False
                break
            #move up
            new_options.append((px,py))
            if py>0:#move up
                new_options.append((px,py-1))
            if py <(height-1):#move down
                new_options.append((px,py+1))
            if px>0 and py!=-1 and py!=height:#move left
                new_options.append((px-1, py))
            if px<(width-1) and py!=-1 and py!=height:#move right
                new_options.append((px+1,py))
    #update blizzards
    new_left = {}
    for bx,by in leftblizzards:
        new_left[((bx-1)%width,by)] = '<'
    leftblizzards = new_left
    new_right = {}
    for bx,by in rightblizzards:
        new_right[((bx+1)%width,by)] = '>'
    rightblizzards = new_right
    new_up = {}
    for bx,by in upblizzards:
        new_up[(bx,(by-1)%height)] = '^'
    upblizzards = new_up
    new_down = {}
    for bx,by in downblizzards:
        new_down[(bx,(by+1)%height)] = 'v'
    downblizzards = new_down
    possibilities = set(new_options)

