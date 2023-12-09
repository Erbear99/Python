rows = [x.strip() for x in open("AOC2023/Day8.txt").readlines()]

directions = rows[0]
paths = {}
for x in rows[2:]:
    y = x.split(" = ")
    paths[y[0]] = (y[1][1:4], y[1][6:9])


curr_val = 'AAA'
count = 0
found = False
while not found:
    for x in directions:
        if x == 'L':
            curr_val = paths[curr_val][0]
        else:
            curr_val = paths[curr_val][1]
        count+=1
        if curr_val == 'ZZZ':
            found = True
            break
print(count)


#for each node that starts with A, follow it's path and see how many iterations it takes to either end with z, and when a loop occurs
initial_path_to_node = {}
print([x for x in paths if x[-1] == 'A'])
for initial_path in [x for x in paths if x[-1] == 'A']:
    path = {}
    current_position = initial_path
    value = 0
    found = False
    while not found:
        for direction_no, direction in enumerate(directions):
            if direction == 'L':
                current_position = paths[current_position][0]
            else:
                current_position = paths[current_position][1]
            value+=1
            if path.get((current_position, direction_no)) is None:
                path[(current_position, direction_no)] = value
            else:
                found = True
                initial_path_to_node[initial_path] = (path, path[(current_position, direction_no)],value, current_position, direction_no)
                break


#break each of these down into distinct rules
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

total = 1
for initial_path in initial_path_to_node:
    total = compute_lcm(total, int(initial_path_to_node[initial_path][2] - initial_path_to_node[initial_path][1]))
print(total)



