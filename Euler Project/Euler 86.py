

#generate pythagorean tripple
pythagorean_tripples = []

def co_prime(p,q):
    while q!=0:
        p,q = q,p%q
    return p == 1

for m in range(2, 70):
    for n in range(1, m):
        if co_prime(m,n) and not (m%2==1 and n%2==1):
            pythagorean_tripples.append((m**2-n**2, 2*m*n, m**2+n**2))


find_num = 1
sum =0 
while sum<1000000:
    find_num+=1
    for x,y,z in pythagorean_tripples:
        #add first being biggest side
        if find_num%x == 0:
            nx = find_num
            ny = y*(nx//x)
            maxval = min(nx + 1, ny)
            minval = ny//2
            if minval< maxval:
                sum+=maxval-minval
        #add second being biggest side
        if find_num%y == 0:
            nx = x*(find_num//y)
            ny = find_num
            maxval = min(ny + 1, nx)
            minval = nx//2 + nx%2
            if minval< maxval:
                sum+=maxval-minval
        

print(find_num, sum)

