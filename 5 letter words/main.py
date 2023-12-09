import time

start = time.time()

word_list = open("words.txt")
dictionaries = []
for word in word_list:
    changedword = word.upper().strip()
    if len(changedword) == 5:
        word_dict = {}
        unique = True
        for letter in changedword:
            if word_dict.get(letter) is None:
                word_dict[letter] = 1
            else:
                unique = False
                break
        if unique:
            dictionaries.append(changedword)


def newlist(possiblewords,wordlist, iter):
    if iter == 5:
        print(possiblewords)
    else:
        for newword in dictionaries:
            if len(set(newword+possiblewords)) == iter*5+5:
                newlist(possiblewords+newword,iter+1)
    

newlist("ABDEL",1)


print(time.time()-start)
print(len(dictionaries))


