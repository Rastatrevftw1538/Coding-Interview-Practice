#create a function to find a given node in a singly linked list, also what is the bigO
#create a function to copy a singly linked list, also what is the bigO
#take that singly linked list and let it have a random pointer (like next but it can point to any node in that list or itself or be null)
#create a function to copy that linked list including the random pointer.  what is the bigO
import random
class Node:
     def __init__(self,initdata=""):
          self.data = initdata
          self.next = None
          self.randNext = None
     def getData(self):
          return self.data
     def getNext(self):
          return self.next
     def setData(self,newdata):
          self.data = newdata
     def setNext(self,newnext):
          self.next = newnext
     def getRandNext(self):
          return self.randNext
          
class LinkList:
	def __init__(self):
		self.head = None
		self.size = 0 

	def __str__(self):
		if self.size == 0 :
			return "empty"
		
		current = self.head
		mystring = str (current )
		while current.getNext() != None:
			current = current.getNext()
			mystring +=" -> "
			mystring += str(current)
		return mystring
	def add(self,item):
		temp = Node(item)    
		temp.setNext(self.head)    
		self.head = temp  
		self.size += 1 
	def append(self, item, head=None):
			temp = Node(item)   #create the node we want to append

			if self.isEmpty():
				self.head = temp
			else:
				current = self.head     #get cursor that will march through list
				while current.getNext() != None:    # here is that test again
					current = current.getNext()
				self.size += 1 ##CHANGE

	def findNode(self, index,current=None):
		current = self.head
		tempIndex = 0
		while tempIndex != index and current != None:
			current = current.getNext()
			tempIndex += 1
		return current
	def setRandNext(self,node):
		randNum = random.randint(0,self.size)
		if randNum == self.size:
			node.randNext = None
		else:
			node.randNext = self.findNode(randNum)

def copyList(linkListToCopy):
     linkedListCopy = LinkList()
     current = linkListToCopy.head
     temp = Node(current.getData())
     tempNext = current.getNext()
     linkedListCopy.head = temp
     linkedListCopy.size += 1
     while linkedListCopy.size != linkListToCopy.size:
          temp = Node(current.getData())
          tempNext = current.getNext()
          temp.setNext(Node(tempNext.getData()))
          temp = temp.getNext()
          current = current.getNext()
          linkedListCopy.size += 1
          
     # what happens when you try to copy an empty list?
     # what happens when it is a list of size 1?
     # what happens when you try to copy a list with size 3?
     # what is the difference between current, temp and tempNext?
     
     return linkedListCopy


listThing = LinkList()
for i in range(3,15, 2):
	listThing.add(i)
print("current", listThing)
print(listThing.findNode(3).getData())
newThing = copyList(listThing)
print("Copy",newThing)
'''for x in range(0,newThing.size):
     newThing.setRandNext(newThing.findNode(x))
     print(newThing.findNode(x))'''