rows = [x.strip() for x in open("AOC2023/Day4.txt").readlines()]

total = 0
scorecard_points = {}
new_cards_won = {}
card = 1
for line in rows:
    numbers = line.split(':')
    winners, actual_numbers = numbers[1].split('|')

    total_numbers = (len([x for x in actual_numbers.split(' ') if len(x)>=1 and x in winners.split(" ")]))
    if total_numbers > 0:
        total+=2**(total_numbers-1)
    scorecard_points[card] = total_numbers
    new_cards_won[card] = 1
    card+=1
print(total)

total_cards_won = 0
for i in scorecard_points:
    #process the cards
    #then update the total
    for j in range(scorecard_points[i]):
        new_cards_won[i+j+1] += new_cards_won[i]
    total_cards_won+=new_cards_won[i]

print(total_cards_won)
    