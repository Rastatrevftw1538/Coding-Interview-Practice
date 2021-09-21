# Given string - reverse it.
# For example
# 'abcd' => 'dcba'


def rev_string(word):
    revdWord = ""
    for letter in word[::-1]:
        revdWord += letter
        # print(revdWord)
    return revdWord


# How do you reverse words in a given sentence without using any library method?
# ‘the wfast fox flew’ => ‘flew fox fast the’


def rev_sent(sentence):
    listOfWords = []
    revdWord = ""
    revdSentence = " "
    for letter in sentence:
        if letter == " ":
            listOfWords.insert(0, revdWord)
            revdWord = ""
        else:
            revdWord += letter
    if revdWord != "":
        listOfWords.insert(0, revdWord)
        revdWord = ""
    return(revdSentence.join(listOfWords))


# How do you check if two strings are anagrams of each other?
# 'foo', 'oof' => true
# 'poox', 'poo' => false
# 'pool', 'opo' => false
# 'stop', 'stip' => false

def anagram_check(word1, word2):
    index = 0
    dictOfLetters = {}
    if len(word1) == len(word2):
        for letter in word1:
            if(letter in dictOfLetters):
                dictOfLetters[letter] += 1
            else:
                dictOfLetters[letter] = 1
        # print(dictOfLetters)
        for letter in word2:
            if letter in dictOfLetters:
                dictOfLetters[letter] -= 1
            else:
                dictOfLetters[letter] = -1
                return False

        for value in dictOfLetters.values():
            if value != 0:
                return False
        return True
    return False


if __name__ == '__main__':
    print(rev_string("apple"))
    print(rev_sent('the fast fox flew'))
    print(anagram_check("foo", "ofo"))  # true
    print(anagram_check("poox", "poo"))  # false
    print(anagram_check("oop", "poo"))  # true
    print(anagram_check("stip", "stap"))  # false
