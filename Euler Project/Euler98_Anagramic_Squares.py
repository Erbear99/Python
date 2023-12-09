words = open('words.txt', 'r').read()

words = [x[1:-1] for x in words.split(',')]

words_with_characters = {}
for word in words:
    chars = ''.join(sorted(word))
    if words_with_characters.get(chars) is None:
        words_with_characters[chars] = [word]
    else:
        words_with_characters[chars].append(word)

anagrams = {x:words_with_characters[x] for x in words_with_characters if len(words_with_characters[x])>1}

#sort anagrams by size of string to match to square nums



generate_squares = []
x = 4
while x**2 < 10**9:
    generate_squares.append(x**2)
    x+=1

square_dict = {}
for square_size in generate_squares:
    chars = ''.join(sorted(str(square_size)))
    if square_dict.get(chars) is None:
        square_dict[chars] = [square_size]
    else:
        square_dict[chars].append(square_size)

square_by_parts = {x:square_dict[x] for x in square_dict if len(square_dict[x])>1}

square_by_size = {}


max_value = 0

for x in square_by_parts:
    previous_val = ''
    previous_count = 0
    identifier = []
    for char in x:
        if char != previous_val:
            if previous_val != '':
                identifier.append(previous_count)
            previous_val = char
            previous_count = 1
        else:
            previous_count+=1
    identifier.append(previous_count)
    identifier = tuple(sorted(identifier))
    if square_by_size.get(identifier) is None:
        square_by_size[identifier] = [square_by_parts[x]]
    else:
        square_by_size[identifier].append(square_by_parts[x])


print(anagrams)
for anagram in anagrams:
    previous_val = ''
    previous_count = 0
    identifier = []
    for char in anagram:
        if char != previous_val:
            if previous_val != '':
                identifier.append(previous_count)
            previous_val = char
            previous_count = 1
        else:
            previous_count+=1
    identifier.append(previous_count)
    identifier = tuple(sorted(identifier))
    if square_by_size.get(identifier) is None:
        continue
    for word in anagrams[anagram]:
        for square_subset in square_by_size[identifier]:
            for pos1, square in enumerate(square_subset):
                valid = True
                lookup = {}
                for pos, char in enumerate(word):
                    if lookup.get(str(square)[pos]) is None:
                        lookup[str(square)[pos]] = char
                    else:
                        if lookup[str(square)[pos]] != char:
                            valid = False
                            break
                if not valid:
                    break
                for pos2, square2 in enumerate(square_subset):
                    if pos2 == pos1:
                        continue
                    #generate new word
                    if ''.join([lookup[x] for x in str(square2)]) in anagrams[anagram]:
                        max_value = max(max_value, square, square2)
                        print(word, ''.join([lookup[x] for x in str(square2)]), square, square2, valid, lookup)

                #confirm that the square works



    print(anagram, anagrams[anagram])
    print(square_by_size.get(identifier))

print(max_value)








