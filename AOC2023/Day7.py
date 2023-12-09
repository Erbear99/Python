rows = [x.strip() for x in open("AOC2023/Day7.txt").readlines()]


five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

score = 0
for row in rows:
    hand, score = row.split(" ")
    #determine the rank
    letters = {}
    
    for letter in hand:
        if letters.get(letter) is None:
            letters[letter] = 1
        else:
            letters[letter]+=1
    found = False
    set_of_three = False
    pairs = 0
    for letter in letters:
        if letters[letter] == 5:
            five_of_a_kind.append((hand, score))
            found = True
            break
        if letters[letter] == 4:
            four_of_a_kind.append((hand, score))
            found = True
            break
        if letters[letter] == 3:
            set_of_three = True
        if letters[letter] == 2:
            pairs+=1
    if found:
        continue
    if set_of_three and pairs == 1:
        full_house.append((hand, score))
        continue
    if set_of_three:
        three_of_a_kind.append((hand, score))
        continue
    if pairs == 2:
        two_pair.append((hand, score))
        continue
    if pairs == 1:
        one_pair.append((hand, score))
        continue
    high_card.append((hand, score))
            

def ranking_hands(elem):
    #generate a number based on the hand:
    value = 0
    for pos, char in enumerate(elem[0]):
        if char=='2':
            value+=13**(4-pos)*0
        elif char=='3':
            value+=13**(4-pos)*1
        elif char=='4':
            value+=13**(4-pos)*2
        elif char=='5':
            value+=13**(4-pos)*3
        elif char=='6':
            value+=13**(4-pos)*4
        elif char=='7':
            value+=13**(4-pos)*5            
        elif char=='8':
            value+=13**(4-pos)*6
        elif char=='9':
            value+=13**(4-pos)*7
        elif char=='T':
            value+=13**(4-pos)*8
        elif char=='J':
            value+=13**(4-pos)*9
        elif char=='Q':
            value+=13**(4-pos)*10           
        elif char=='K':
            value+=13**(4-pos)*11
        elif char=='A':
            value+=13**(4-pos)*12
    return value



high_card.sort(key=ranking_hands)
one_pair.sort(key=ranking_hands)
two_pair.sort(key=ranking_hands)
three_of_a_kind.sort(key=ranking_hands)
full_house.sort(key=ranking_hands)
four_of_a_kind.sort(key=ranking_hands)
five_of_a_kind.sort(key=ranking_hands)

ordered_hands = high_card+one_pair+two_pair+three_of_a_kind+full_house+four_of_a_kind+five_of_a_kind
score = 0
for pos, hand in enumerate(ordered_hands):
    score+=int(hand[1])*(pos+1)
print(score)





five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

score = 0
for row in rows:
    hand, score = row.split(" ")
    #determine the rank
    letters = {}
    jokers = 0
    for letter in hand:
        if letter == 'J':
            jokers+=1
        elif letters.get(letter) is None:
            letters[letter] = 1
        else:
            letters[letter]+=1

    
    set_of_three = False
    set_of_four = False
    set_of_five = False
    pairs = 0
    for letter in letters:
        if letters[letter]+jokers == 5:
            set_of_five = True
        if letters[letter]+jokers == 4:
            set_of_four = True
        if letters[letter] == 3:
            set_of_three = True
        if letters[letter] == 2:
            pairs+=1
    if set_of_five or jokers == 5:
        five_of_a_kind.append((hand, score))
        continue
    if set_of_four:
        four_of_a_kind.append((hand, score))
        continue
    if (set_of_three and pairs == 1) or (pairs==2 and jokers ==1):
        full_house.append((hand, score))
        continue
    if set_of_three or jokers == 2 or (jokers == 1 and pairs >= 1):
        three_of_a_kind.append((hand, score))
        continue
    if pairs == 2 or (pairs == 1 and jokers == 1):
        two_pair.append((hand, score))
        continue
    if pairs == 1 or jokers == 1:
        one_pair.append((hand, score))
        continue
    high_card.append((hand, score))
            

def ranking_hands2(elem):
    #generate a number based on the hand:
    value = 0
    for pos, char in enumerate(elem[0]):
        if char=='2':
            value+=13**(4-pos)*1
        elif char=='3':
            value+=13**(4-pos)*2
        elif char=='4':
            value+=13**(4-pos)*3
        elif char=='5':
            value+=13**(4-pos)*4
        elif char=='6':
            value+=13**(4-pos)*5
        elif char=='7':
            value+=13**(4-pos)*6            
        elif char=='8':
            value+=13**(4-pos)*7
        elif char=='9':
            value+=13**(4-pos)*8
        elif char=='T':
            value+=13**(4-pos)*9
        elif char=='Q':
            value+=13**(4-pos)*10           
        elif char=='K':
            value+=13**(4-pos)*11
        elif char=='A':
            value+=13**(4-pos)*12
    return value



high_card.sort(key=ranking_hands2)
one_pair.sort(key=ranking_hands2)
two_pair.sort(key=ranking_hands2)
three_of_a_kind.sort(key=ranking_hands2)
full_house.sort(key=ranking_hands2)
four_of_a_kind.sort(key=ranking_hands2)
five_of_a_kind.sort(key=ranking_hands2)


ordered_hands = high_card+one_pair+two_pair+three_of_a_kind+full_house+four_of_a_kind+five_of_a_kind
score = 0
for pos, hand in enumerate(ordered_hands):
    score+=int(hand[1])*(pos+1)
print(score)
    
