class todo_item(object):
    """docstring for to-do_item."""
    def __init__(self, description, priority=0):
        #super(to-do_item, self).__init__()
        # Check parameters...
        if len(description) == 0:
            print "Error: Description string empty"
            return
        
        self.description = description
        print "Adding item: '%s'" % description
        self.priority = priority
        print "with a priority of %d" % priority

    """Print To Do List Item"""
    def Print_Item(self):
        print "\nTo Do Item: "
        print "Description: %s" % self.description
        print "Priority: %d" % self.priority

    
