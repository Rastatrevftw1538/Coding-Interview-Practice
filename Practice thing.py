#Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)

class MyQueue():
    def __init__(self):
        self.items = []
        self.st1 = Stack()
        self.st2 = Stack()

    def isEmpty(self):
        return self.items == []

    def pushQueue(self, item):
        self.tempItems = []
        self.st1.push(item)
        if len(self.st1) > 1:
            for i in range(len(st1)):
                self.st2 = self.tempItems.push(self.st1.pop())
        self.items = self.st2
        
        #self.newQueue.insert(-1,item)
    def popQueue(self):
        if len(self.items) > 1:
            '''for i in range(len(st1)):
                self.st2.push(self.st1.pop())
                self.items.append(st2.push())
            popped = self.st2.pop()
            for i in range(len(st2)):
                self.st2.pop()
                self.st1.push()'''
            return self.items.pop(-1) 
        elif len(self.items) == 0:
            return self.items.pop()
    def __str__(self):
        temp = MyQueue()
        stringy = ""
        while not self.isEmpty():
            a = self.popQueue()
            temp.pushQueue(a)
            stringy = str(a) + stringy
        while not temp.isEmpty():
            self.pushQueue(temp.popQueue())
            
        return "["+stringy+")\n"    

queueUno = MyQueue()
queueUno.pushQueue("1")
queueUno.pushQueue("2")
queueUno.pushQueue("3")
queueUno.pushQueue("4")

print(queueUno)
