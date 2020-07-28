#create a function to find a given node in a singly linked list, also what is the bigO
#create a function to copy a singly linked list, also what is the bigO
#take that singly linked list and let it have a random pointer (like next but it can point to any node in that list or itself or be null)
#create a function to copy that linked list including the random pointer.  what is the bigO

class Node:
     def __init__(self,initdata=""):
          self.data = initdata
          self.next = None
     def getData(self):
          return self.data
     def getNext(self):
          return self.next
     def setData(self,newdata):
          self.data = newdata
     def setNext(self,newnext):
          self.next = newnext
          
class LinkList:
	def __init__(self):
		self.head = None
		self.size = 0 

	def __str__(self):
		if self.size == 0 :
			return "empty"
		
		current = self.head
		mystring = str (current.getData() )
		while current.getNext() != None:
			current = current.getNext()
			mystring +=" -> "
			mystring += str(current.getData())
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
		if self.size == 0:
			return False
		current = self.head
		tempIndex = 0
		while tempIndex != index:
			current = current.getNext()
			tempIndex += 1
		return current.getData()
def copyList(linkListToCopy):
     linkedListCopy = LinkList()
     current = linkListToCopy.head
     temp = Node(current.getData())
     temp.setNext(current.getNext())
     linkedListCopy.head = temp
     linkedListCopy.size += linkListToCopy.size
     return linkedListCopy


listThing = LinkList()
for i in range(3,15, 2):
	listThing.add(i)
	print("current nl is", listThing)
print(listThing.findNode(3))
newThing = copyList(listThing)
print(newThing)