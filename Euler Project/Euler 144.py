import math


#take one slope
#see the angle that the normal line makes from that.
#add that angle again to get the actual reflection line ie the slope
#then generate teh position
#start with a slope, each bounce

m  = -19.7/1.4
b = 10.1

#generate the solutions for the equation
def equation_solver(a,b,c):
    return((-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a))

previous_bounce = .007
pos_y = True
number_of_bounces = 0
while number_of_bounces==0 or previous_bounce>.01 or previous_bounce<-.01 or b <0:
    solutions = equation_solver(4+m**2, 2*m*b, b**2-100)
    #Select the new point, generate the new normal line
    new_points = [x for x in solutions if abs(x-previous_bounce)>.001]
    new_y =m*new_points[0]+b

    number_of_bounces+=1
    #we need to find the angle from the slopes
    #new angle
    s1 = math.atan(m)
    s2 = math.atan(new_y/(4*new_points[0]))
    new_slope = math.tan(2*s2-s1)
    #generate new b with x and y
    new_intercept = -new_slope*new_points[0]+new_y
    print(new_slope, new_intercept)
    m,b,previous_bounce= (new_slope, new_intercept, new_points[0])
print(number_of_bounces)