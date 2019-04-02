#!/usr/bin/env python3
filename = input("Enter input file name >>> ")
# filename = "okonkwo.txt"

with open(filename, 'r') as file:
    tmp = file.read().strip().split()
    words = []
    for word in tmp:
        t = []
        for char in word:
#             if char.isalpha() or char == '.':
#                 t.append(char)
            pass
        words.append(word)
        
allWords = list(set(words))
numWords = len(words)
print(len(allWords))
print(len(words))
out = []
model = {}

for word in allWords:
    a = words.index(word)
    indicies = [a]
    try:
        while True:
            a = words.index(word, a + 1)
            indicies.append(a)
    except:
        pass
    followers = []
    
    for i in indicies:
        if i < len(words) - 1:
            followers.append(words[i + 1])
    if len(followers) == 0:
        continue
    freqs = {}
    for wordA in followers:
        if wordA not in freqs.keys():
            freqs[wordA] = 1
        else:
            freqs[wordA] += 1
    l = list(freqs.items())
    l = [(a[1], a[0]) for a in l]
    l.sort()
    l.reverse()
    out.append((len(l), word, l))
    freqs = [(a[1], a[0]) for a in freqs.items()]
    freqs.sort()
    freqs.reverse()
    model[word] = freqs

out.sort()
out.reverse()
# import pprint as pp
# pp.pprint(out)

import pickle
open(filename + ".model", 'wb').write(pickle.dumps(model))

print("Done Parsing")
