import unittest
import ItemClass as Item


class TestItemClass(unittest.TestCase):

    def setUp(self): 
        self.item = Item.todoItem("Test Item", 3)
    
    def runTest(self):
        # A description should not be empty.
        self.assertNotEqual(len(self.item.description), 0, "Error - Empty Description")
        # A priority should be set.
        self.assertGreater(self.item.priority, 0, "A priority should be set")

    def tearDown(self):
        self.item = None


if __name__ == '__main__':
    unittest.main()
