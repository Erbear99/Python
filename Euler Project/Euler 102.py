


triangles = [[int(y) for y in x.split(',')] for x in open('C:/Users/Erik/Programming Projects/Python/Euler Project/p102_triangles.txt', 'r').read().split('\n')]


count = 0
for triangle in triangles:
    # look at three sides
    #side 1
    #check that both the origin and the third value are on the same side
    sides = [False, False, False]
    for side_check in range(3):

        if triangle[(side_check*2)%6] == triangle[(side_check*2+2)%6]: #slope of 0
            if bool(triangle[(side_check*2)%6]< 0) == bool(triangle[(side_check*2)%6]<triangle[(side_check*2+4)%6]):
                sides[side_check] = True
        else:
            #slope and intercept
            slope = (triangle[(side_check*2+1)%6]-triangle[(side_check*2+3)%6])/(triangle[(side_check*2)%6]-triangle[(side_check*2+2)%6])
            intercept = triangle[(side_check*2+1)%6]-slope*triangle[(side_check*2)%6]
            if bool(0<intercept) == bool(triangle[(side_check*2+5)%6]<slope*triangle[(side_check*2+4)%6]+intercept):
                sides[side_check] = True
    print(sides)
    if sides[0] and sides[1] and sides[2]:
        count+=1
        
print(count)