import numpy as np
import sys
import re
import json

# wordlist = open('texts.txt', 'r').read()

# corpus = wordlist.split()

# wordDict = {}

# for word1, word2 in zip(corpus[:-1], corpus[1:]):
#   if word1 in wordDict.keys():
#     wordDict[word1].append(word2)
#   else:
#     wordDict[word1] = [word2]

# with open('texts.json', 'w') as outfile:
#     json.dump(wordDict, outfile)

with open('texts.json') as f:
    wordDict = json.load(f)

firstWord = np.random.choice(wordDict.keys())

text = [firstWord]

length = sys.argv[1]

for i in range(int(length)):
  text.append(np.random.choice(wordDict[text[-1]]))

finalText = ' '.join(text)

#this regex grabs the first word after sentence ending punctuation + a space
p = re.compile(r'(?<=[\.\?!]\s)(\w+)')

def cap(match):
    return(match.group().capitalize())

finalText = p.sub(cap, finalText)

finalText = finalText.capitalize() + '.'

print finalText