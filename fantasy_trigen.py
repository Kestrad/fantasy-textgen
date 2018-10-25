import numpy as np
import sys
import re
import json

#construct the trigram dictionary
wordlist = open('texts.txt', 'r').read()

corpus = wordlist.split()

wordDict = {}

# for word1, word2, word3 in zip(corpus[:-2], corpus[1:-1], corpus[2:]):
#   if word1 in wordDict.keys():
#     nextWord = wordDict[word1]
#     if word2 in nextWord.keys():
#       nextWord[word2].append(word3)
#     else:
#       nextWord[word2] = []
#       nextWord[word2].append(word3)
#   else:
#     wordDict[word1] = {word2: [word3]}

# #write the dictionary to a file
# with open('trigrams.json', 'w') as outfile:
#     json.dump(wordDict, outfile)

#read the trigram dictionary from file
with open('trigrams.json') as f:
    wordDict = json.load(f)

#start the text block with a trigram
firstWord = np.random.choice(wordDict.keys())

text = [firstWord]

length = sys.argv[1]

secDict = wordDict[text[-1]]
secWord = np.random.choice(secDict.keys())
thirdWord = np.random.choice(secDict[secWord])

text.append(secWord)
text.append(thirdWord)

#construct the rest of the text block
for i in range(int(length)):
  firstWord = text[-2]
  secWord = text[-1]
  firstDict = wordDict[firstWord]
  thirdWord = np.random.choice(firstDict[secWord])
  text.append(thirdWord)

finalText = ' '.join(text)

#this regex grabs the first word after sentence ending punctuation + a space
p = re.compile(r'(?<=[\.\?!]\s)(\w+)')

def cap(match):
    return(match.group().capitalize())

#in theory this should capitalize the first letter of every sentence
finalText = p.sub(cap, finalText)

finalText = finalText.capitalize() + '.'

print finalText