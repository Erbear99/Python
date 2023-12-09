monopoly_board = [0]*40
monopoly_board[0] = 1
possibilities = 1
dice = ((2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,5),(9,4),(10,3),(11,2),(12,1))
dice_total = 36

for i in range(1000):
    new_board = [0]*40
    for pos, i in enumerate(monopoly_board):
        if pos == 30:
            new_board[10]+=new_board[30]
            new_board[30] = 0
        else:
            for new_pos, number in dice:
                new_board[(pos+new_pos) %40] += number*i
    monopoly_board = new_board
    possibilities*=dice_total
print([round(x/possibilities,3) for x in monopoly_board])


