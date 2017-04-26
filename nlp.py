import json

prevLetterOccurances = {}
nextLetterOccurances = {}

with open('words.txt', encoding="utf8") as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            for x in range(0, len(word)-1):
                if(x == 0):
                    #print(word[x], word[x+1])
                    prev = word[x]
                    next = word[x+1]
                    if(prev.isalpha() and next.isalpha()):
                        if(prev not in prevLetterOccurances):
                            prevLetterOccurances[prev] = 1
                        else:
                            prevLetterOccurances[prev] = prevLetterOccurances[prev] + 1
                        if(prev not in nextLetterOccurances):
                            nextLetterOccurances[prev] = {next: 1}
                        else:
                            if(next not in nextLetterOccurances[prev]):
                                nextLetterOccurances[prev][next] = 1
                            else:
                                nextLetterOccurances[prev][next] = nextLetterOccurances[prev][next] + 1
                else:
                    #print(word[x-1:x+1], word[x+1])
                    prev = word[x-1:x+1]
                    next = word[x+1]
                    if(prev.isalpha() and next.isalpha()):
                        if (prev not in prevLetterOccurances):
                            prevLetterOccurances[prev] = 1
                        else:
                            prevLetterOccurances[prev] = prevLetterOccurances[prev] + 1
                        if (prev not in nextLetterOccurances):
                            nextLetterOccurances[prev] = {next: 1}
                        else:
                            if (next not in nextLetterOccurances[prev]):
                                nextLetterOccurances[prev][next] = 1
                            else:
                                nextLetterOccurances[prev][next] = nextLetterOccurances[prev][next] + 1

#print(prevLetterOccurances)
#print(nextLetterOccurances)

frequencies = {}
for prev in nextLetterOccurances:
    frequencies[prev] = {}
    for next in nextLetterOccurances[prev]:
        frequencies[prev][next] = nextLetterOccurances[prev][next]/prevLetterOccurances[prev]

#print(frequencies)

with open("nlpDictionary.txt", 'w') as outfile:
    json.dump(frequencies, outfile)


def getProbabilityVector(letters):
    with open("nlpDictionary.txt") as infile:
        frequencies = json.load(infile)
    letters = letters.lower()
    if(letters.isalpha() == False):
        return []
    elif(letters not in frequencies):
        return []
    else:
        myDict = frequencies[letters]
        myVec = [0.0] * 24
        if('a' in myDict):
            myVec[0] = myDict['a']
        else:
            myVec[0] = 0.0
        if ('b' in myDict):
            myVec[1] = myDict['b']
        else:
            myVec[1] = 0.0
        if ('c' in myDict):
            myVec[2] = myDict['c']
        else:
            myVec[2] = 0.0
        if ('d' in myDict):
            myVec[3] = myDict['d']
        else:
            myVec[3] = 0.0
        if ('e' in myDict):
            myVec[4] = myDict['e']
        else:
            myVec[4] = 0.0
        if ('f' in myDict):
            myVec[5] = myDict['f']
        else:
            myVec[5] = 0.0
        if ('g' in myDict):
            myVec[6] = myDict['g']
        else:
            myVec[6] = 0.0
        if ('h' in myDict):
            myVec[7] = myDict['h']
        else:
            myVec[7] = 0.0
        if ('i' in myDict):
            myVec[8] = myDict['i']
        else:
            myVec[8] = 0.0
        if ('k' in myDict):
            myVec[9] = myDict['k']
        else:
            myVec[9] = 0.0
        if ('l' in myDict):
            myVec[10] = myDict['l']
        else:
            myVec[10] = 0.0
        if ('m' in myDict):
            myVec[11] = myDict['m']
        else:
            myVec[11] = 0.0
        if ('n' in myDict):
            myVec[12] = myDict['n']
        else:
            myVec[12] = 0.0
        if ('o' in myDict):
            myVec[13] = myDict['o']
        else:
            myVec[13] = 0.0
        if ('p' in myDict):
            myVec[14] = myDict['p']
        else:
            myVec[14] = 0.0
        if ('q' in myDict):
            myVec[15] = myDict['q']
        else:
            myVec[15] = 0.0
        if ('r' in myDict):
            myVec[16] = myDict['r']
        else:
            myVec[16] = 0.0
        if ('s' in myDict):
            myVec[17] = myDict['s']
        else:
            myVec[17] = 0.0
        if ('t' in myDict):
            myVec[18] = myDict['t']
        else:
            myVec[18] = 0.0
        if ('u' in myDict):
            myVec[19] = myDict['u']
        else:
            myVec[19] = 0.0
        if ('v' in myDict):
            myVec[20] = myDict['v']
        else:
            myVec[20] = 0.0
        if ('w' in myDict):
            myVec[21] = myDict['w']
        else:
            myVec[21] = 0.0
        if ('x' in myDict):
            myVec[22] = myDict['x']
        else:
            myVec[22] = 0.0
        if ('y' in myDict):
            myVec[23] = myDict['y']
        else:
            myVec[23] = 0.0
        return myVec

