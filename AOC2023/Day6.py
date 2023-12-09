import math

rows = [x.strip() for x in open("AOC2023/Day6.txt").readlines()]

times = [x for x in rows[0].split(" ") if x != '']
distances = [x for x in rows[1].split(" ") if x != '']
pairings = [(int(times[x]), int(distances[x])) for x in range(1,len(times))]
print(pairings)
#determine the number of ways you can win each race and then mulitiply together

total = 1
for pairing in pairings:
    time = pairing[0]
    distance = pairing[1]

    #how many seconds does the button need to be held to pass the distance
    count = 0
    for i in range(time):
        velocity = i
        dist = velocity * (time-i)
        if dist > distance:
            count+=1
    total*= count
print(total)

time = ''.join(times[1:])
distance = ''.join(distances[1:])



#use quadratic formula
a = -1
b = int(time)
c = -int(distance)

sol1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
sol2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

#determine the lesser value to see if it holds true
first_bound = int(min(sol1, sol2))
second_bound = int(max(sol1, sol2))


print(second_bound-first_bound)