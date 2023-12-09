file = open("Day17.txt", 'r')
wind = [x.strip() for x in file][0]
windval = 0

rocks = [[['#', '#', '#', '#']], [['.','#','.'],['#','#','#'],['.','#','.']], [['#','#','#'],['.','.','#'],['.','.','#']], [['#'],['#'],['#'],['#']], [['#','#'],['#','#']]]
#tetris simulation!!!


tetris_silo = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]


for round in range(2022):
    rock = rocks[round%5]
    starting_x = 2
    starting_y = len(tetris_silo)-4 #referring to the bottom left corner

    for _ in range(3):
        #push rock dir if you can
        if wind[windval%len(wind)] == '<':
            if starting_x > 0:
                starting_x-=1
        else:
            if starting_x+len(rock[0])<7:
                starting_x+=1
        windval+=1

    while starting_y >= 0:
        #jet of gas pushes it
        if wind[windval%len(wind)] == '<':
            #try to shift left
            if starting_x > 0:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx-1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x -=1
        else:
            if starting_x+len(rock[0])<7:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx+1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x +=1
        windval+=1

        #tries to fall
        valid_move = True
        for posy, line in enumerate(rock):
            for posx, value in enumerate(line):
                if (starting_y+posy-1)<0 or (value == '#' and tetris_silo[starting_y+posy-1][starting_x+posx] == '#'):

                    valid_move = False
        if valid_move:
            starting_y-=1
        else:
            for posy, line in enumerate(rock):
                for posx, value in enumerate(line):
                    if value == '#':
                        tetris_silo[starting_y+posy][starting_x+posx] = '#'
            if starting_y + len(rock)+4 > len(tetris_silo):
                new_highest = (starting_y + len(rock)+4) - len(tetris_silo)
                for _ in range(new_highest):
                    tetris_silo.append(['.','.','.','.','.','.','.'])
            break


print(len(tetris_silo)-4)

pattern = {}
num_of_new_rounds = 0
length_of_silo = 0
length_at_time = 0
for round in range(2022,100000):
    rock = rocks[round%5]
    starting_x = 2
    starting_y = len(tetris_silo)-4 #referring to the bottom left corner

    for _ in range(3):
        #push rock dir if you can
        if wind[windval%len(wind)] == '<':
            if starting_x > 0:
                starting_x-=1
        else:
            if starting_x+len(rock[0])<7:
                starting_x+=1
        windval+=1

    while starting_y >= 0:
        #jet of gas pushes it
        if wind[windval%len(wind)] == '<':
            #try to shift left
            if starting_x > 0:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx-1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x -=1
        else:
            if starting_x+len(rock[0])<7:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx+1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x +=1
        windval+=1

        #tries to fall
        valid_move = True
        for posy, line in enumerate(rock):
            for posx, value in enumerate(line):
                if (starting_y+posy-1)<0 or (value == '#' and tetris_silo[starting_y+posy-1][starting_x+posx] == '#'):

                    valid_move = False
        if valid_move:
            starting_y-=1
        else:
            for posy, line in enumerate(rock):
                for posx, value in enumerate(line):
                    if value == '#':
                        tetris_silo[starting_y+posy][starting_x+posx] = '#'
            if starting_y + len(rock)+4 > len(tetris_silo):
                new_highest = (starting_y + len(rock)+4) - len(tetris_silo)
                for _ in range(new_highest):
                    tetris_silo.append(['.','.','.','.','.','.','.'])
            break
    if round%5 == 4:
        if pattern.get(windval%len(wind)) is None:
            pattern[windval%len(wind)] = (len(tetris_silo), round)
        else:
            amount_grown = len(tetris_silo) - pattern[windval%len(wind)][0]
            num_of_rounds = round-pattern[windval%len(wind)][1]
            length_of_silo = (((1000000000000-1) - round)//num_of_rounds) * amount_grown + len(tetris_silo)-4
            num_of_new_rounds = ((1000000000000-1) - round)%num_of_rounds
            length_at_time = len(tetris_silo)
            break




for round in range(num_of_new_rounds):
    rock = rocks[round%5]
    starting_x = 2
    starting_y = len(tetris_silo)-4 #referring to the bottom left corner

    for _ in range(3):
        #push rock dir if you can
        if wind[windval%len(wind)] == '<':
            if starting_x > 0:
                starting_x-=1
        else:
            if starting_x+len(rock[0])<7:
                starting_x+=1
        windval+=1

    while starting_y >= 0:
        #jet of gas pushes it
        if wind[windval%len(wind)] == '<':
            #try to shift left
            if starting_x > 0:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx-1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x -=1
        else:
            if starting_x+len(rock[0])<7:
                valid_move = True
                for posy, line in enumerate(rock):
                    for posx, value in enumerate(line):
                        if value == '#' and tetris_silo[starting_y+posy][starting_x+posx+1] == '#':
                            valid_move = False
                if valid_move:
                    starting_x +=1
        windval+=1

        #tries to fall
        valid_move = True
        for posy, line in enumerate(rock):
            for posx, value in enumerate(line):
                if (starting_y+posy-1)<0 or (value == '#' and tetris_silo[starting_y+posy-1][starting_x+posx] == '#'):

                    valid_move = False
        if valid_move:
            starting_y-=1
        else:
            for posy, line in enumerate(rock):
                for posx, value in enumerate(line):
                    if value == '#':
                        tetris_silo[starting_y+posy][starting_x+posx] = '#'
            if starting_y + len(rock)+4 > len(tetris_silo):
                new_highest = (starting_y + len(rock)+4) - len(tetris_silo)
                for _ in range(new_highest):
                    tetris_silo.append(['.','.','.','.','.','.','.'])
            break


print(length_of_silo + (len(tetris_silo)-length_at_time))