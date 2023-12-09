
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

local_max = 0

start = 1_000_000
while True:
    start+=1
    #find first resp...
    if gcd(start,10) == 1:
        #do the long division as they go....
        a = 0
        q = 1
        #start with enough 1's to cover the val... then find the remainder... from there count the number of 1's left unitl remainder = 0
        while q!=0:
            a+=1
            q = (q*10+1)%start
        if a > 1_000_000:
            print(start)
            break
        