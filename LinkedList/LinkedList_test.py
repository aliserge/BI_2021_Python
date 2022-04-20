import unittest
from LinkedList import LinkedList

class Test_LinkedList(unittest.TestCase):
    
    def test_init_Nones(self):
        test_list = LinkedList()
        with self.assertRaises(AttributeError):
            test_list.first()
        with self.assertRaises(AttributeError):
            test_list.last()
    
    def test_add(self):
        test_list = LinkedList()
        test_list.add(1)
        self.assertEqual(list(test_list), [1])
        test_list.add(2,0)
        self.assertEqual(list(test_list), [2,1])
        test_list.add(3,2)
        self.assertEqual(list(test_list), [2,1,3])
        
    def test_add_all(self):
        test_list = LinkedList()
        test_list.add_all([1,2,3])
        self.assertEqual(list(test_list), [1,2,3])
        test_list.add_all([0,10], 0)
        self.assertEqual(list(test_list), [0,10,1,2,3])
        test_list.add_all([88,89], 3)
        
    def test_in(self):
        test_list = LinkedList()
        self.assertEqual(1 in test_list, False)
        test_list.add('a')
        self.assertEqual('a' in test_list, True)
        
    def test_getitem(self):
        test_list = LinkedList()
        test_list.add('a')
        self.assertEqual(test_list[0], test_list[-1], 'a')
        test_list.add('b')
        self.assertEqual(test_list[1], 'b')
        
    def test_len(self):
        test_list = LinkedList()
        self.assertEqual(len(test_list), 0)
        test_list.add_all([1,2,3])
        self.assertEqual(len(test_list), 3)
        
    def test_pop(self):
        test_list = LinkedList()
        test_list.add_all([0,1,2,3])
        test_list.pop()
        self.assertEqual(list(test_list),[0,1,2])
        test_list.pop(0)
        self.assertEqual(list(test_list), [1,2])
        
    def test_remove_last(self):
        test_list = LinkedList()
        test_list.add_all([0,1,0,2])
        test_list.remove_last_occurence(0)
        self.assertEqual(list(test_list), [0,1,2])
        test_list.remove_last_occurence(10)
        self.assertEqual(list(test_list), [0,1,2])
        test_list.remove_last_occurence(1)
        self.assertEqual(list(test_list), [0,2])
        

if __name__ == "__main__":
    unittest.main()
