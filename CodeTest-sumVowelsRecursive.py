def sumVowelsRecursive (s,num=0,count=0,aCount = 0,eCount = 0,iCount = 0,oCount = 0,uCount = 0):
    letterWeights = { "a": 1, "e" : 2, "i":3, "o":4, "u":5}
    if count < len(s):
        if s[num] in letterWeights:
            if s[num] == "a":
                aCount += 1
            elif s[num] == "e":
                eCount += 1
            elif s[num] == "i":
                iCount += 1
            elif s[num] == "o":
                oCount += 1
            elif s[num] == "u":
                uCount += 1
            return sumVowelsRecursive(s,num+1,count+1,aCount,eCount,iCount,oCount,uCount)
        else:
            return sumVowelsRecursive(s,num+1,count+1,aCount,eCount,iCount,oCount,uCount)
    else:
        return aCount*letterWeights["a"]+eCount*letterWeights["e"]+iCount*letterWeights["i"]+oCount*letterWeights["o"]+uCount*letterWeights["u"]
print(sumVowelsRecursive("Welcome to Indonesia"))
