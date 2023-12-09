#generate pairs


def gcd(x, y):
    while(y):
       x, y = y, x % y
    return x


maximum_val = 120000

#triples for 120 degree angle triangles
doubles = {}
for m in range(2,400):
    for n in range(1,m):
        if gcd(m,n) == 1 and (m-n)%3 !=0:
            a,b,c = m**2-n**2, 2*m*n+n**2, m**2+m*n+n**2
            if a+b > maximum_val:
                break
            min_len = min(a,b)
            mid_len = max(a,b)
            multiplier = 1
            while multiplier*(a+b)<maximum_val:
                if doubles.get(min_len*multiplier) is None:
                    doubles[min_len*multiplier] = [mid_len*multiplier]
                else:
                    doubles[min_len*multiplier].append(mid_len*multiplier)
                multiplier+=1
triples = set()
total = 0
for p in doubles:
    for r in doubles[p]:
        if doubles.get(r) is not None:
            solutions = [q for q in doubles[p] if q in doubles.get(r)]
            for q in solutions:
                if p+r+q <=maximum_val:
                    triples.add(p+r+q)
                    total+=p+r+q
print(len(set(triples)))
print(sum(triples))