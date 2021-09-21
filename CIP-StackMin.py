class Node:
    def __init__(self, initdata=""):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Stack():

    def __init__(self):
        self.smallestItemList = []
        self.items = []

    def push(self, item):
        if len(self.items) == 0:
            self.smallestItemList.append(item)
        if item <= self.smallestItemList[0]:
            self.smallestItemList.insert(0, item)
        self.items.append(item)
        print(self.items)

    def pop(self):
        tempItem = self.items.pop()
        if tempItem == self.smallestItemList[0]:
            self.smallestItemList.pop(0)
        return tempItem

    def min(self):
        return self.smallestItemList[0]


stack = Stack()
stack.push(1)
stack.push(1)
stack.push(2)
stack.push(-10)
stack.push(-10)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.min())
