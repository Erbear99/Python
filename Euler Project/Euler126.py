#generate the first layer for a bunch of values



cubiod_layers

for x in range(1,100):
    for y in range(1,x+1):
        for z in range(1,y+1):
            print(x,y,z,2*x*y+2*x*z+2*y*z)