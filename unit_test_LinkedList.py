from Task3 import linkedList
import unittest

class TestStrinMethods(unittest.TestCase):
    def testLength(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.assertEqual(len(self.Test),1)
        self.Test.append(2)
        self.assertEqual(len(self.Test),2)
        self.Test.append(1)
        self.assertEqual(len(self.Test),3)

    def testContains(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.assertTrue(3 in self.Test)
        self.Test.append(2)
        self.assertTrue(2 in self.Test)
        self.assertFalse(1 in self.Test)

    def testGetItem(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.assertEqual(self.Test[0], 3)
        self.Test.append(3)
        self.assertEqual(self.Test[1], 3)
        with self.assertRaises(IndexError):
            self.assertEqual(self.Test[2], 3)

    def testSetItem(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test[0] = 4
        self.assertEqual(self.Test[0], 4)
        self.Test[0] = 3
        self.assertEqual(self.Test[0], 3)
        with self.assertRaises(IndexError):
            self.Test[3] = 4

    def testEqual(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test.append(4)
        self.Test.append(5)
        self.Test.append(6)
        nlist = [3,4,5,6]
        self.assertTrue(self.Test == nlist)
        self.Test.append(7)
        self.assertFalse(self.Test == nlist)
        nlist2 = [6,6,5,5,3]
        self.assertFalse(self.Test == nlist2)

    def testAppend(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test.append("a")
        self.Test.append(" ")

    def testInsert(self):
        self.Test = linkedList()
        self.Test.insert(0,1)
        self.Test.insert(0,"w")
        with self.assertRaises(IndexError):
            self.Test.insert(5,5)

    def testRemove(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test.append("a")
        self.Test.remove("not found")
        self.Test.remove(3)
        self.Test.remove("a")

    def testDelete(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test.append("a")
        self.Test.delete(0)
        self.Test.delete(0)
        with self.assertRaises(IndexError):
            self.Test.delete(3)

    def testSort(self):
        self.Test = linkedList()
        self.Test.append(3)
        self.Test.append(6)
        self.Test.append(5)
        self.Test.append(6)
        self.Test.append(5)
        nlist = [3,5,5,6,6]
        nlist2 = [6,6,5,5,3]
        self.Test.sort(False)
        for i in range(3):
            self.assertEqual(self.Test[i], nlist[i])
        self.Test.sort(True)
        for i in range(3):
            self.assertEqual(self.Test[i], nlist2[i])
        self.Test = linkedList()
        self.Test.append(1)
        self.Test.append(2)
        self.Test.append(3)
        self.Test.append(4)
        self.Test.append(5)
        nlist3 = [1,2,3,4,5]
        self.Test.sort(False)
        for i in range(5):
            self.assertEqual(self.Test[i], nlist3[i])

if __name__ == '__main__':
    unittest.main()
