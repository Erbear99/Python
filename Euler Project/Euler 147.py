# start by just calculating the squares
#2 x 3
width= 47
height = 43


total = 0
for x_gap in range(width):
    for y_gap in range(height):
        number_of_options = (x_gap+1)*(y_gap+1)
        number_of_squares_applicable = (width-x_gap) * (height-y_gap)
        print(number_of_options, number_of_squares_applicable)
        total+=number_of_options * number_of_squares_applicable

#now for diagonals.... but I'll save that for a different day
#different day!!!

#try the 'basic' solution IE find the size of the unique diagonal square, 
#then generate the number of possibilities for that square, for each unique rectangle.
new_total= 0
#generate the sizes of the squares 
diagonal_vert_first_sizing = [1,1]
diagonal_horiz_first_sizing = [1,1]
up_count = 0
while True:
    #add 1 to the vertical up size
    if up_count%2 ==0:
        diagonal_vert_first_sizing[1]+=1
        diagonal_horiz_first_sizing[0]+=1
    else:
        diagonal_vert_first_sizing[0]+=1
        diagonal_horiz_first_sizing[1]+=1
    if (diagonal_vert_first_sizing[0]>width or diagonal_vert_first_sizing[1]> height) and (diagonal_horiz_first_sizing[0]>width or diagonal_horiz_first_sizing[1]> height):
        break
    down_count = 0
    base_horiz = [diagonal_horiz_first_sizing[0],diagonal_horiz_first_sizing[1]]
    base_vert = [diagonal_vert_first_sizing[0],diagonal_vert_first_sizing[1]]
    while True:
        #update horizontal
        #update x first
        #this is where I should count up all the options for the squares...
        if base_horiz[0] <= width and base_horiz[1] <= height:
            #go through options to see how many squares it would cover...
            #start at the base
            for x in range(width-base_horiz[0]+1):
                for y in range(height-base_horiz[1]+1):
                    new_total+=((x+1)*(y+1))

        if base_vert[0] <= width and base_vert[1] <= height:
            for x in range(width-base_vert[0]+1):
                for y in range(height-base_vert[1]+1):
                    new_total+=((x+1)*(y+1))
            


        print(up_count, down_count, base_horiz, base_vert)
        if (up_count+down_count)%2 == 1:
            #update x value
            base_horiz[0]+=1
        if (down_count%2) == 0:
            #update y value
            base_horiz[1]+=1

        if (up_count+down_count)%2 == 0:
            base_vert[0]+=1
        if down_count%2 == 1:
            base_vert[1]+=1


        down_count+=1
        if (base_horiz[0] > width or base_horiz[1] > height) and (base_vert[0]>width or base_vert[1]>height):
            break
        #update vertical
        
    up_count+=1



print(new_total)
print(total)
print(new_total+total)