
lookup = {(0,1,1,1,1):1}

for i in range(1):
    new_lookup = {}
    #run a batch
    for envelope in lookup:
        quantity = lookup[envelope]
        #pick each piece in the bag, and go through the process of cutting it
        for pos, value in enumerate(envelope):
            if value > 0:
                new_envelope = tuple((x+quantity if True else 3) for pos, x in envelope)
                


            
                
