#!/usr/bin/env python3
import sys
filename = sys.argv[1]

with open(filename, 'r') as file:
    words = file.read().strip().split()

allWords = set(words)
numWords = len(words)
print(len(allWords))
print(len(words))

model = {}

# Find indicies of occurances
for i,word in enumerate(words):
    if word in model:
        followers = model[word]
    else:
        followers = []
    if i + 1 < numWords:
        followers.append(words[i+1])
    else:
        continue
    model[word] = followers
    


for word in model.keys():
    followers = model[word]
    freqs = {}
    for wordA in followers:
        if wordA not in freqs:
            freqs[wordA] = 1
        else:
            freqs[wordA] += 1
    freqs = [(a[1], a[0]) for a in freqs.items()]
    freqs.sort(reverse = True)
    model[word] = freqs

import pickle
open(filename + ".model", 'wb').write(pickle.dumps(model))

print("Done Parsing")
