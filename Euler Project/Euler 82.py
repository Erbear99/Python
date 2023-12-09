file = open("p082_matrix.txt", 'r')
matrix = [[int(x) for x in line.strip().split(',')] for line in file]
shortest_path = [[0 for _ in range(80)] for _ in range(80)]
shortest_path[0][0] = matrix[0][0]
for pos, line in enumerate(matrix):
    shortest_path[pos][0] = line[0]


position = 0
while position< 79:
    position +=1
    for y in range(80): #generate the shortest distance for each location
        minimum = -1
        for starter_y in range(80):
            path=shortest_path[starter_y][position-1]
            for ys in range(min(starter_y, y), max(starter_y, y)+1):
                path+=matrix[ys][position]
            if path < minimum or minimum == -1:
                minimum = path
        shortest_path[y][position] = minimum

minimum = -1
for x in shortest_path:
    if x[79] < minimum or minimum == -1:
        minimum = x[79]
print(minimum)