dials = [[[3,4,12,2,5,10,7,16,8,7,8,8],
         [4,6,6,3,3,14,14,21,21,9,9,4],
         [5,6,7,8,9,10,11,12,13,14,15,4],
         [11,14,11,14,11,14,14,11,14,11,14,11]],

         [[1,0,9,0,12,0,6,0,10,0,10,0],
         [3,26,6,0,2,13,9,0,17,19,3,12],
         [9,20,12,3,6,0,14,12,3,8,9,0],
         [7,0,9,0,7,14,11,0,8,0,16,2]],

         [[5,0,10,0,8,0,22,0,16,0,9,0],
         [21,6,15,4,9,18,11,26,14,1,12,0],
         [9,13,9,7,13,21,17,4,5,0,7,8]],

         [[4,0,7,15,0,0,14,0,9,0,12,0],
         [7,3,0,6,0,11,11,6,11,0,6,17]],

         [[3,0,6,0,10,0,7,0,15,0,8,0]]]

dial_combination = [0,0,0,0]

#try every possible combo

while True:
    #update the dial combo to the next one:
    #determine if the given position is accurate.
    valid_solution = True
    for column in range(12):
        #determine what each of the dials would display 
        total = 0
        values = []
        for row in range(4):
            #determine what each of the rows would be
            #Important!!! all dials are turned relative to the base dial
            # row 0 would have to check dials 1, then dial 0
            check_dial = row+1
            found_value = 0
            while found_value ==0:
                if check_dial == 0:
                    found_value = dials[check_dial][row-4][column]
                else:
                    found_value = dials[check_dial][row-4][(column+dial_combination[check_dial-1])%12]
                check_dial-=1
            total+=found_value

        if total != 42:
            valid_solution = False
            break



    if valid_solution:
        print(dial_combination)

    update_position = 0
    updated = False
    while not updated:
        dial_combination[update_position] +=1
        if dial_combination[update_position] == 12:
            dial_combination[update_position] = 0
            update_position+=1
            if update_position == 4:
                break
        else:
            updated = True
    if update_position == 4:
        break
    