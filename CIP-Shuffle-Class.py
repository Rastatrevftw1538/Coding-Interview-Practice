from random import randint


class Solution:

    def __init__(self, array):
        self.origArray = array
        self.newArray = []

    def shuffle(self):
        countOfNums = 0
        self.newArray = []
        while countOfNums < len(self.origArray):
            randomNum = randint(0, len(self.origArray) - 1)
            num = self.origArray[countOfNums]
            self.newArray.insert(randomNum, num)
            countOfNums += 1
        return "Shuffled to", self.newArray

    def reset(self):
        self.newArray = self.origArray
        return "Reset to", self.newArray


def main():
    arrayThing = Solution([1, 2, 3, 4, 5, 6, 7])
    print(arrayThing.shuffle())
    print(arrayThing.shuffle())
    print(arrayThing.shuffle())
    print(arrayThing.reset())
    print(arrayThing.shuffle())


if __name__ == "__main__":
    main()
