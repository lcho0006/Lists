class node:
    def __init__(self,value,link=None):
        self.value = value
        self.next = link

    def __str__(self):
        return str(self.value)

class linkedList:
    def __init__(self):
        """
        This method initialises the linkedList
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: None
        """
        self.head = None
        self.count = 0

    def __str__(self):
        """
        This method returns a string representation of the linkedList
        :param: None
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: None
        :postcondition: None
        :return: string representation of linkedList
        """
        string = "List: ("+str(len(self))+") "
        current = self.head
        while not (current is None):
            string += " -> " + str(current)
            current = current.next
        string += ""
        return string

    def __len__(self):
        """
        This method returns the length of the linkedList
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: length of linkedList
        """
        return self.count

    def getNode(self,index):
        """
        This method returns the node at the index of the linkedList
        :param: index: an integer
        :raises: StopIteration if node doesnt exist at index
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index inputted
        :postcondition: the node is found or not in the linkedList
        :return: The node at index
        """
        current = self.head
        if index >= len(self) or index < 0:
            raise StopIteration("Node doesn't exist at this index")
        currentPos = 0
        while not current is None and currentPos<index:
            current = current.next
            currentPos += 1
        return current

    def __contains__(self, item):
        """
        This method checks if an item is in the linkedList
        :param: item: a string or integer
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: the item is found or not in the list
        :return: True if item is found in the linkedList
        """
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False

    def __getitem__(self, index):
        """
        This method returns the value at the index of the linkedList
        :param: index: an integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index inputted
        :postcondition: the item is returned or the index is out of range
        :return: the item in the linkedList at the index
        """
        current = self.head
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        currentPos = 0
        while currentPos<index:
            current = current.next
            currentPos += 1
        return current.value

    def __setitem__(self, index, item):
        """
        This method sets the value at the index of the linkedList to the item given
        :param: index: an integer
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index and item inputted
        :postcondition: the item at the index is set to item or the index is out of range
        :return: None
        """
        current = self.head
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        currentPos = 0
        while currentPos<index:
            current = current.next
            currentPos += 1
        current.value = item

    def __eq__(self, other):
        """
        This method checks if the linkedList is equal to another list
        :param: other: another list
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: there is a valid list inputted
        :postcondition: The lists are equal or not equal
        :return: True if the lists are equal
        """
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def append(self, item):
        """
        This method appends an item to the linkedList
        :param: item: a string or integer
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: The item is added to the end of the linkedList
        :return: None
        """
        self.insert(len(self),item)

    def insert(self,index,item):
        """
        This method inserts an item at any index in linkedList
        :param: index: an integer
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index and item inputted
        :postcondition: The item is added at the index of the linkedList or index is out of range
        :return: None
        """
        if index < 0:
            index  += len(self)
        if index > len(self):
            raise IndexError("index is out of range")
        if index==0:
            self.head = node(item,self.head)
        else:
            someNode = self.getNode(index-1)
            someNode.next = node(item, someNode.next)
        self.count+=1

    def remove(self, item):
        """
        This method removes an item from the linkedList
        :param: item: a string or integer
        :raises: ValueError if item is not in linkedList
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: The item is removed from the linkedList or item isn't in the linkedList
        :return: None
        """
        index = 0
        found = False
        for i in range(len(self)):
            if self[i] == item:
                index = i
                found = True
                break
        if found is False:
            return ValueError("item not found in array")
        self.delete(index)

    def delete(self,index):
        """
        This method deletes an item from any index in linkedList
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index inputted
        :postcondition: The item is deleted from the linkedList or index is out of range
        :return: None
        """
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        if index==0:
            self.head = self.head.next
        else:
            before = self.getNode(index - 1)
            itemToRemove = before.next
            before.next = itemToRemove.next
        self.count-=1

    def sort(self, reverse):
        """
        This method sorts the linkedList using selection sort
        :param: reverse: True or False
        :raises: None
        :complexity: best case o(n^2), worst case o(n^2)
        :precondition: there is an index inputted
        :postcondition: The linkedList is sorted
        :return: None
        """
        if reverse:
            for i in range(len(self)-1,0,-1):
                minpos=0
                for j in range(1,i+1):
                    if self[j]<self[minpos]:
                        minpos = j
                temp = self[i]
                self[i] = self[minpos]
                self[minpos] = temp
        else:
            for i in range(len(self)-1,0,-1):
                maxpos=0
                for j in range(1,i+1):
                    if self[j]>self[maxpos]:
                        maxpos = j
                temp = self[i]
                self[i] = self[maxpos]
                self[maxpos] = temp

    def __iter__(self):
        """
        This method initialises the iteration of the linkedList
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: self
        """
        self.iteration = 0
        return self

    def __next__(self):
        """
        This method iterates the linkedList
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: The value at an index of the linkedList
        """
        self.iteration += 1
        if self.iteration > len(self):
            raise StopIteration
        return self[self.iteration-1]

    def readIntoArray(self,filename):
        """
        This method reads a file into the linkedList
        :param: filename: a txt file
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: There is a valid txt file
        :postcondition: The file is appended by line into the linkedList
        :return: None
        """
        with open(filename) as f:
            for line in f:
                self.append(line.replace("\n",""))
        f.close()
