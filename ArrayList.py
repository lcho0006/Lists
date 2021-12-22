from referential_array import build_array

class arrayList:
    def __init__(self):
        """
        This method initialises the arraylist
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: None
        """
        self.array = build_array(20)
        self.size = 20
        self.currentlen = 0

    def __str__(self):
        """
        This method returns a string representation of the arraylist
        :param: None
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: None
        :postcondition: None
        :return: string representation of arraylist
        """
        string = ""
        for i in range(len(self)):
            string += str(self.array[i])+"\n"
        return string

    def __len__(self):
        """
        This method returns the length of the arraylist
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: length of arraylist
        """
        return self.currentlen

    def __contains__(self, item):
        """
        This method checks if an item is in the arraylist
        :param: item: a string or integer
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: the item is found or not in the list
        :return: True if item is found in the arrayList
        """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def __getitem__(self, index):
        """
        This method returns the value at the index of the arrayList
        :param: index: an integer
        :raises: IndexError if index is out of range
        :complexity: best case o(1), worst case o(1)
        :precondition: there is an index inputted
        :postcondition: the item is returned or the index is out of range
        :return: the item in the arrayList at the index
        """
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        return self.array[index]

    def __setitem__(self, index, item):
        """
        This method sets the value at the index of the arrayList to the item given
        :param: index: an integer
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(1), worst case o(1)
        :precondition: there is an index and item inputted
        :postcondition: the item at the index is set to item or the index is out of range
        :return: None
        """
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        self.array[index] = item

    def __eq__(self, other):
        """
        This method checks if the arrayList is equal to another list
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
            if self.array[i] != other[i]:
                return False
        return True

    def append(self, item):
        """
        This method appends an item to the arrayList
        :param: item: a string or integer
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: The item is added to the end of the arrayList
        :return: None
        """
        self.dynamicCheck1()
        self.array[len(self)] = item
        self.currentlen+=1

    def insert(self, index, item):
        """
        This method inserts an item at any index in arrayList
        :param: index: an integer
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index and item inputted
        :postcondition: The item is added at the index of the arrayList or index is out of range
        :return: None
        """
        if index < 0:
            index  += len(self)
        self.dynamicCheck1()
        self.currentlen+=1
        if index >= len(self):
            raise IndexError("index is out of range")
        currentmax = len(self)
        while currentmax > index:
            self.array[currentmax] = self.array[currentmax-1]
            currentmax -= 1
        self.array[index] = item

    def remove(self, item):
        """
        This method removes an item from the arrayList
        :param: item: a string or integer
        :raises: ValueError if item is not in arrayList
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an item inputted
        :postcondition: The item is removed from the arrayList or item isn't in the arrayList
        :return: None
        """
        index = 0
        found = False
        for i in range(len(self)):
            if self.array[i] == item:
                index = i
                found = True
                break
        if found is False:
            return ValueError("item not found in array")
        self.delete(index)

    def delete(self, index):
        """
        This method deletes an item from any index in arrayList
        :param: item: a string or integer
        :raises: IndexError if index is out of range
        :complexity: best case o(n), worst case o(n)
        :precondition: there is an index inputted
        :postcondition: The item is deleted from the arrayList or index is out of range
        :return: None
        """
        if index < 0:
            index  += len(self)
        if index >= len(self):
            raise IndexError("index is out of range")
        if self.array[index] is None:
            raise IndexError("index is empty")
        while index < len(self) and index < self.size-1:
            self.array[index] = self.array[index+1]
            index += 1
        self.array[index] = None
        self.currentlen-=1
        self.dynamicCheck2()

    def sort(self, reverse):
        """
        This method sorts the arrayList using selection sort
        :param: reverse: True or False
        :raises: None
        :complexity: best case o(n^2), worst case o(n^2)
        :precondition: there is an index inputted
        :postcondition: The arrayList is sorted
        :return: None
        """
        if reverse:
            for i in range(len(self)-1,0,-1):
                minpos=0
                for j in range(1,i+1):
                    if str(self.array[j])<str(self.array[minpos]):
                        minpos = j
                temp = self.array[i]
                self.array[i] = self.array[minpos]
                self.array[minpos] = temp
        else:
            for i in range(len(self)-1,0,-1):
                maxpos=0
                for j in range(1,i+1):
                    if str(self.array[j])>str(self.array[maxpos]):
                        maxpos = j
                temp = self.array[i]
                self.array[i] = self.array[maxpos]
                self.array[maxpos] = temp

    def __iter__(self):
        """
        This method initialises the iteration of the arrayList
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
        This method iterates the arrayList
        :param: None
        :raises: None
        :complexity: best case o(1), worst case o(1)
        :precondition: None
        :postcondition: None
        :return: The value at an index of the arrayList
        """
        self.iteration += 1
        if self.iteration > len(self):
            raise StopIteration
        return self.array[self.iteration-1]

    def dynamicCheck1(self):
        """
        This method checks and adjusts the size of the arrayList
        :param: None
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: None
        :postcondition: The arrayList size is doubled or the same
        :return: None
        """
        if len(self) == self.size:
            self.size*= 2
            temp = []
            for i in range(len(self)):
                temp.append(self.array[i])
            self.currentlen = 0
            self.array = build_array(self.size)
            for i in temp:
                self.append(i)

    def dynamicCheck2(self):
        """
        This method checks and adjusts the size of the arrayList
        :param: None
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: None
        :postcondition: The arrayList size is halved or the same
        :return: None
        """
        if len(self) < (int(self.size/8)) and self.size > 20:
            self.size /= 2
            self.size = int(self.size)
            temp = []
            for i in range(len(self)):
                temp.append(self.array[i])
            self.currentlen = 0
            self.array = build_array(self.size)
            for i in temp:
                self.append(i)

    def readIntoArray(self,filename):
        """
        This method reads a file into the arrayList
        :param: filename: a txt file
        :raises: None
        :complexity: best case o(n), worst case o(n)
        :precondition: There is a valid txt file
        :postcondition: The file is appended by line into the arrayList
        :return: None
        """
        with open(filename) as f:
            for line in f:
                self.append(line.replace("\n",""))
        f.close()
