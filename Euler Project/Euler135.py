import math


MAX_N = 50000000

n = [0]*(MAX_N+1)
squares = [0,1,4,9,16]

def quadratic_formula(a,b,c):
    return((-b-math.sqrt(b*b-4*a*c))/2*a)

print("space allocated")

for gap in range(1,int(MAX_N/4)):
    if gap%1000000 == 0:
        print(gap)
    value = gap*2+1
    continued = False
    while True:
        if len(squares) == value:
            squares.append(value*value)
        difference = value**2-(value-gap)**2-(value-2*gap)**2
        if difference > MAX_N:
            value=math.ceil(quadratic_formula(-1,6*gap,-5*gap*gap-MAX_N))

            continue
        if difference<=0:
            break
        n[difference] +=1

        value+=1


print(len(p:=[x[0] for x in enumerate(n) if x[1] == 1]))
