


pyramid_layer = [[0,0],
                 [0,1,0],
                 [0,0,0,0]]


for i in range(30):
    print(i)
    next_layer = [[0,0]]
    for y in range(i+2):
        new_layer = [0]
        for x in range(y+1):
            new_layer.append((pyramid_layer[y][x]+pyramid_layer[y][x+1]+pyramid_layer[y+1][x+1])%100)
        new_layer.append(0)
        next_layer.append(new_layer)
    next_layer.append([0 for x in range(i+5)])
    pyramid_layer = next_layer
    
    for row in pyramid_layer:
        print(row)