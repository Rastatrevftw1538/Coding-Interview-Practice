import math
def Check_Edit(word1,word2):
    edits = 0
    spacesAdded = 0
    editedWord = []
    if len(word1)== len(word2):
        for thing in range(0,len(word1)):
            if word2[thing] != word1[thing]:
                edits += 1
    elif abs(len(word1) - len(word2)) == 1:
        if len(word1) < len(word2):
            wordToUse = word1
        elif len(word1) > len(word2):
            wordToUse = word2
        for thing in range(0,len(wordToUse)+1):
            print(word1[thing]+" "+word2[thing])
            if word2[thing] != word1[thing] and spacesAdded != abs(len(word1) - len(word2)):
                spacesAdded += 1
                edits += 1
                if len(word1) < len(word2):
                    if editedWord == []:
                        for i in word2:
                            editedWord.append(i)
                    editedWord.insert(thing,"#")
                elif len(word1) > len(word2):
                    if editedWord == []:
                        for i in word2:
                            editedWord.append(i)
                    editedWord.insert(thing,"#")
                    word2 = "".join(editedWord)
            if word2[thing] != word1[thing] and spacesAdded == abs(len(word1) - len(word2)):
                edits += 1
    if edits > 1:
            return False
    else:
        return True
print(Check_Edit("pale","ple"))