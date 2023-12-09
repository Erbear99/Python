
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

list_of_vals = {1:[(1,1)]}
for x in range(2,19):
    print(x)
    new_list = []
    #chooose two numbers
    for i in range(1,int(x/2)+1):
        for yn, yd in list_of_vals[i]:
            for xn,xd in list_of_vals[x-i]:
                numerator = xn*yd+xd*yn
                denominator = xd*yd
                gcd = computeGCD(numerator, denominator)
                new_list.append((int(numerator//gcd), int(denominator//gcd)))
                numerator = xn*yn
                denominator = xn*yd+yn*xd
                gcd = computeGCD(numerator, denominator)
                new_list.append((int(numerator//gcd), int(denominator//gcd)))

    list_of_vals[x] = list(set(new_list))
print(len([n/d*60 for n,d in list(set([j for i in list_of_vals for j in list_of_vals[i]]))]))

#this isn't quite acccurate... becasue sometimes there are multiple "sets" in parrallel or in series...