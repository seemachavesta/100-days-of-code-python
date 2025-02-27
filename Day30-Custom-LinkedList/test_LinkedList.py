import unittest

from linkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a fresh linked list for each test"""
        self.ll = LinkedList()


    def test_insert_at_beginning(self):
        self.ll.insert_at_beginning(10)
        self.assertEqual(self.ll.head.data, 10)

        self.ll.insert_at_beginning(20)
        self.assertEqual(self.ll.head.data, 20)
        self.assertEqual(self.ll.head.next.data, 10)
    
    def test_insert_at_end(self):
        self.ll.insert_at_end(0)
        self.assertEqual(self.ll.head.data, 0)

        self.ll.insert_at_end(30)
        self.assertEqual(self.ll.head.next.data, 30)

    def test_insert_at(self):
        self.ll.insert_values([10, 5, 20, 2])
        self.ll.insert_at(40, 2)
        self.assertEqual(self.ll.get_at(2), 40)

    def test_get_at(self):
        self.ll.insert_values([10, 0, 20, 30])
        self.assertEqual(self.ll.get_at(0), 10)
        self.assertEqual(self.ll.get_at(1), 0)
        self.assertEqual(self.ll.get_at(2), 20)
        self.assertEqual(self.ll.get_at(3), 30)

        with self.assertRaises(Exception):
            self.ll.get_at(5)

    def test_remove_at(self):
        self.ll.insert_values([10, 0, 20, 30])
        self.ll.remove_at(2)
        self.assertEqual(self.ll.get_at(2), 30)


    def test_remove_by_value(self):
        self.ll.insert_values([10, 0, 20, 30])
        self.ll.remove_by_value(0)
        self.assertEqual(self.ll.get_at(1), 20)

        self.ll.remove_by_value(20)
        self.assertFalse(self.ll.find_value(20))


    def test_get_length(self):
        self.ll.insert_values([10, 0, 20, 30])
        self.assertEqual(self.ll.get_length(), 4)

        self.ll.insert_at_end(4)
        self.assertEqual(self.ll.get_length(), 5)

    def test_find_value(self):
        self.ll.insert_values([100, 200, 300])
        self.assertTrue(self.ll.find_value(200))
        self.assertFalse(self.ll.find_value(400))

        
       

    


if __name__ == "__main__":
    unittest.main()
