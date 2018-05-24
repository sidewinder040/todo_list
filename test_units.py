import unittest
import ItemClass as Item

class TestItemClass(unittest.TestCase):
    def setUp(self): 
        self.item = Item.todo_item("test")
    
    def runTest(self):
        self.assertNotEqual(len(self.item.description), 0, "Error - Empty Description")
    def tearDown(self):
        self.item = None

if __name__ == '__main__':
    unittest.main()
