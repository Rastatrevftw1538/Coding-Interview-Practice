def StringComp(word=str()):
    compWord = ""
    sameLet = ""
    passedLet = ""
    numOfLet = 0
    for i in word:
        sameLet = i
        if numOfLet == 0:
            sameLet = i
            numOfLet += 1
            passedLet = sameLet
        else:
            if i == passedLet:
                numOfLet += 1
            else:
                compWord += passedLet + str(numOfLet)
                passedLet = sameLet
                numOfLet = 1
    compWord += passedLet + str(numOfLet)
    if len(word) >= len(compWord):
        return compWord
    else:
        return word


def main():
    print(StringComp("bbbaaacccCCCCC"))


main()
