def gcf(p,q):
    while q!=0:
        p,q = q,p%q
    return p
largest_val = 50
count = 0
for x in range(largest_val+1,(largest_val+1)**2+1):
    xx = x%(largest_val+1)
    xy = x//(largest_val+1)
    gcd = gcf(xx,xy)
    run1 = xx//gcd
    rise1 = xy//gcd
    for y in range(1,x):
        yx = y%(largest_val+1)
        yy = y//(largest_val+1)
        gcd = gcf(yy,yx)
        run2 = yx//gcd
        rise2 = yy//gcd
        zx = xx-yx
        zy = xy-yy


        
print(count)
        




