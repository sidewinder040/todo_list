class todo_item(object):
    """docstring for to-do_item."""
    def __init__(self, description):
        #super(to-do_item, self).__init__()
        self.description = description
        print "Adding item: '%s'" % description

    """Print To Do List Item"""
    def Print_Item(self):
        print self.description

# item1 = todo_item("Test")
# print item1.Print_Item()
# item1.description = "Test - Changed"
# print item1.Print_Item()
