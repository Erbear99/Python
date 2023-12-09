file = open("p081_matrix.txt", 'r')
matrix = [[int(x) for x in line.strip().split(',')] for line in file]
shortest_path = [[0 for _ in range(80)] for _ in range(80)]
shortest_path[0][0] = matrix[0][0]
position = 0



while position < 158: #sb 159
    position+=1
    x, y = min(position,79), max(0, position-79)
    while y <min(position, 79):
        if y == 0:
            shortest_path[y][x] = matrix[y][x] + shortest_path[y][x-1]
        else:
            shortest_path[y][x] = matrix[y][x] + min(shortest_path[y][x-1], shortest_path[y-1][x])
        x-=1
        y+=1
    shortest_path[y][x] = matrix[y][x] + shortest_path[y-1][x]
print(shortest_path[79][79])
print(shortest_path[78][79])
print(shortest_path[79][78])
print(matrix[79][79])

