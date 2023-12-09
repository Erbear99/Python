

minimum_multiplications = {1:0}

possibilities = [[1]]

multiplications = 0
while possibilities:
    multiplications +=1
    pbv2 = []
    for possible in possibilities:
        for x in possible:
            total = possible[-1]+x
            if total > 200 or minimum_multiplications.get(total) is not None and minimum_multiplications.get(total)<multiplications:
                continue
            pbv2.append([x for x in possible]+[total])
            minimum_multiplications[total] = multiplications
    possibilities = pbv2
    

print(sum([minimum_multiplications[x] for x in range(1,201)]))