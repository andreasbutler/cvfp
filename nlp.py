prevLetterOccurances = {}
nextLetterOccurances = {}

with open('words.txt') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            for x in range(0, len(word)-1):
                if(x == 0):
                    #print(word[x], word[x+1])
                    prev = word[x]
                    next = word[x+1]
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