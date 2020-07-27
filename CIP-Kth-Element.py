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
		self.tail = None 
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
			
	def mover(self):
		size = 1

		prevprevious = None
		previous = None     
		current = self.head

		while current.getNext() != None:
			prevprevious = previous
			previous = current
			current = current.getNext()
			size += 1

		if size >= 3:
			prevprevious.setNext(current)
			previous.setNext(self.head)
			self.head = previous

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)    
		temp.setNext(self.head)    
		self.head = temp  
		self.size += 1 


	## append(item) adds a new item as the last item in the list 
	## It needs the item and returns nothing. 
	def append(self, item):
		temp = Node(item)   #create the node we want to append

		if self.isEmpty():
			self.head = temp
		else:
			current = self.head     #get cursor that will march through list
			while current.getNext() != None:    # here is that test again
				current = current.getNext()
			self.tail = current.setNext( temp )     #current now is 'tail'. Cause new node to be new tail
			self.size += 1 ##CHANGE

	## search(item) searches for the item in the list.
	## It needs the item and returns True/False depending on if item is found 
	def search(self, item):
		if self.isEmpty():
			return False
		current = self.head
		while current.getData() != item and current.getNext() != None:
			current = current.getNext()
		return current.getData() == item  

	def remove(self, item):
		if self.size > 0:   #can only remove from a list with items
			if self.head.getData() == item: #if is in the first Node
				self.head = self.head.getNext()
			else:   
				current = self.head  #where we are looking. The person we are looking at
				previous = None    #the 'person' just behind them

				#use same finder-method as .search(), but also update 'previous'
				while current.getData() != item and current.getNext() != None:
					previous = current
					current = current.getNext()

				if current.getData() == item:
					previous.setNext( current.getNext() ) 
					self.size -= 1 ##CHANGE

	def pop(self):
		if self.size == 0:   #could do self.head == None
			return None
		if self.size == 1:
			item = self.head.getData()
			self.head = None
			return item
		
		previous = None     #like remove, we need know who is behind us
		current = self.head

		while current.getNext() != None:   #work our way to the end
			previous = current
			current = current.getNext()
		#current is now 'tail', and previous is 2nd-to-last (and will be new last)
			
		item = current.getData()    #save last 'data' 
		previous.setNext( None)   #make previous the new end = new tail
		self.size -= 1 ##CHANGE
		return item

	def index(self, item):
		current = self.head
		ivalue = 0
		while current.getNext() != None and current.getData() != item:
			current = current.getNext()
			ivalue += 1
		
		if current.getData() == item :
			return ivalue
		else:
			return -1


	def insert(self, pos, item):
		if pos >= self.size:
			self.append(item)

		temp = Node(item)  #what we want to insert
		previous = None   #need 'before' and a 'current' pointers
		current = self.head
		count = 0   #our 'index' counter. want count == pos

		while count < pos: 
			previous = current
			current = current.getNext()
			count += 1
		previous.setNext ( temp )
		temp.setNext( current )
		self.size += 1 ##CHANGE

	def reverse(self):
		if self.size == 0:   
			return None
		if self.size == 1:
			item = self.head.getData()
			self.head = None
			return item
		previous = None
		current = self.head

		while current.getNext() != None:
			previous = current

	def findKthElem(self,kthElm):
		current = self.head
		toLastElem = self.size - kthElm
		currentIndex = 0
		while currentIndex <= self.size and currentIndex != toLastElem:
			current = current.getNext()
			currentIndex += 1
		
		if currentIndex == toLastElem :
			return current.getData()
		else:
			return -1
listThing = LinkList()
for i in range(3,15, 2):
	listThing.add(i)
	print("current nl is", listThing)
print(listThing.findKthElem(3))