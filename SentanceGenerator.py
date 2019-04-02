from pickle import loads
import random
import sys

filename = sys.argv[1]

model = loads(open(filename, 'rb').read())

def nextWord(word):
    cats = {}
    for follower in model[word]:
        if follower[0] not in cats.keys():
            cats[follower[0]] = [follower[1]]
            continue
        cats[follower[0]].append(follower[1])
    cats = list(cats.items())
    cats.sort()
    cats.reverse()
    i = 0
    j = 0
    words = []
    while len(words) < 4:
        if j >= len(cats[i][1]):
            j = 0
            i += 1
        if i >= len(cats):
            break
        words.append(cats[i][1][j])
        j += 1
    return random.choice(words)

def genParagraph(numWords):
    lastWord = nextWord(random.choice(list(model.keys())))
    while not lastWord[0].istitle():
        lastWord = nextWord(random.choice(list(model.keys())))
    
    s = [lastWord + " "]
    while len(s) <= 495 or '.' not in lastWord:
        lastWord = nextWord(lastWord)
        s.append(lastWord + " ")
    return s

def genSentance(startingWord = None):
    if startingWord is None:
        startingWord = random.choice(list(model.keys()))
    s = startingWord + ' '
    word = startingWord
    while word[len(word)-1] != '.':
        word = nextWord(word)
        s += word + ' '
    return s


s = genParagraph(495)
#s = genSentance()
while len(s) != 500:
    s = genParagraph(495)
import pprint
pprint.pprint("".join(s))
print("".join(s))
print (str(len(s)) + " words")
