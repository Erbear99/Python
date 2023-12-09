file = open('p096_sudoku.txt','r')
values = [x.strip() for x in file]

puzzles = [[[int(char) for char in values[x*10+y]] for y in range(1,10)] for x in range(50)]
sum = 0
for puzzle in puzzles:
    possibilities = []
    guess_states = []
    while True:
        for y, puzzle_line in enumerate(puzzle):
            line_possibilities = []
            for x, puzzle_val in enumerate(puzzle_line):
                if puzzle_val !=0:
                    line_possibilities.append([])
                else:
                    poss = [1,2,3,4,5,6,7,8,9]
                    for i in range(9):
                        if puzzle[y][i] in poss:
                            poss.remove(puzzle[y][i])
                        if puzzle[i][x] in poss:
                            poss.remove(puzzle[i][x])
                    for addy in range(3):
                        for addx in range(3):
                            if puzzle[y-(y%3)+addy][x-x%3+addx] in poss:
                                poss.remove(puzzle[y-(y%3)+addy][x-x%3+addx])
                    line_possibilities.append(poss)
            possibilities.append(line_possibilities)
        check_pos = 0
        while check_pos<81:
            x = check_pos%9
            y = check_pos//9
            if len(possibilities[y][x]) == 1:
                puzzle[y][x] = possibilities[y][x][0]
                for i in range(9):
                    if puzzle[y][x] in possibilities[i][x]:
                        possibilities[i][x].remove(puzzle[y][x])
                    if puzzle[y][x] in possibilities[y][i]:
                        possibilities[y][i].remove(puzzle[y][x])
                for addy in range(3):
                    for addx in range(3):
                        if puzzle[y][x] in possibilities[y-y%3+addy][x-x%3+addx]:
                            possibilities[y-y%3+addy][x-x%3+addx].remove(puzzle[y][x])
                check_pos = 0
            else:
                #check each possible value to see if it is unique in its row, coumn or square
                for possible_value in possibilities[y][x]:
                    square_values = []
                    row_values=[]
                    column_values=[]
                    for i in range(9):
                        if x!=i and possible_value in possibilities[y][i]:
                            column_values.append((i,y))
                        if y!=i and possible_value in possibilities[i][x]:
                            row_values.append((x,i))
                    for addx in range(3):
                        for addy in range(3):
                            if (y!= (y-y%3+addy) or x!=(x-x%3+addx)) and possible_value in possibilities[y-y%3+addy][x-x%3+addx]:
                                square_values.append((x-x%3+addx,y-y%3+addy )) 
                    if len(square_values) == 0 or len(row_values) == 0 or len(column_values)==0:
                        puzzle[y][x] = possible_value
                        for xx, yy in set(square_values+row_values+column_values):
                            possibilities[yy][xx].remove(possible_value)
                        possibilities[y][x] = []
                        check_pos = 0
                        break
                check_pos+=1

        #check if the puzzle is completed.... if it is break out...
        completed = True
        for line in puzzle:
            for char in line:
                if char == 0:
                    completed = False
            if not completed:
                break
        if completed:
            break

        #2 options if puzzle isn't completed
        #1. there are no possibilities left-- revert to previous state and make a new guess
        #2. there are possibilities left-- take a guess as to updated state
        #go through the possibilities
        possible = True
        first_guess = (-1,-1)
        for y_pos, y_line in enumerate(puzzle):
            for x_pos, x_line in enumerate(y_line):
                if x_line == 0:
                    if len(possibilities[y_pos][x_pos]) == 0:
                        possible = False
                    if first_guess == (-1,-1):
                        first_guess = (x_pos,y_pos)

        if possible:
            #add old position to list of states
            #copy current values

            new_puzzle = [[x for x in line] for line in puzzle]
            new_possibilities = [[[value for value in x] for x in line] for line in possibilities]
            guess_states.append((new_puzzle, new_possibilities, (first_guess, 0)))
            #make a guess
            possibilities[first_guess[1]][first_guess[0]] = [possibilities[first_guess[1]][first_guess[0]][0]]
        else:
            #current state is impossible, revert to old position
            while True:
                puzzle, possibilities, past_guess = guess_states[-1]
                guess_states = guess_states[:-1]
                if len(possibilities[past_guess[0][1]][past_guess[0][0]]) >= past_guess[1]+2:
                    break
            new_puzzle = [[x for x in line] for line in puzzle]
            new_possibilities = [[[value for value in x] for x in line] for line in possibilities]
            guess_states.append((new_puzzle,new_possibilities, (past_guess[0], past_guess[1]+1)))
            possibilities[past_guess[0][1]][past_guess[0][0]] = [possibilities[past_guess[0][1]][past_guess[0][0]][past_guess[1]+1]]
    print(puzzle)
    sum+=puzzle[0][0]*100 + puzzle[0][1]*10 + puzzle[0][2]
    print("new puzzle:    ")

print(sum)
sum = 0
for puzzle in puzzles:
    sum+=puzzle[0][0]*100 + puzzle[0][1]*10 + puzzle[0][2]
    print(puzzle)
print(sum)




