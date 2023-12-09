passcodes = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

rules = {}
invalid_rules = {}

for passcode in passcodes.split('\n'):
    for character in passcode:
        if rules.get(character)==None:
            rules[character] = {}

    #first letter
    for pos1,l1 in enumerate(passcode):
        for pos2,l2 in enumerate(passcode):
            if pos1!=pos2:
                comparison = ''
                if pos1 < pos2:
                    comparison = '<'
                else: 
                    comparison = '>'
                if rules[l1].get(l2) is None or rules[l1].get(l2) == comparison:
                    rules[l1][l2] = comparison
                else:
                    print(l1,l2)
                    if invalid_rules.get(l1) is None:
                        invalid_rules[l1] = {}
                    invalid_rules[l1][l2] = comparison
for rule in rules:
    print(rule, end ="    ")
    for char in rules[rule]:
        if rules[rule][char] == '<':
            print(char, end=" ")
    print("   <   ", end=" ")
    for char in rules[rule]:
        if rules[rule][char] == '>':
            print(char, end=" ")
    print("   >")

