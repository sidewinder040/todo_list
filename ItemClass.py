class todoItem(object):
    """docstring for to-do_item."""
    def __init__(self, description, priority=0):

        # Check parameters...
        if len(description) == 0:
            print("Error: Description string empty")
            return
        
        self.description = description
        print("Adding item: '%s'" % description)
        self.priority = priority
        print("with a priority of %d" % priority)

    """Print To Do List Item"""
    def print_tem(self):
        print("\nTo Do Item: ")
        print("Description: %s" % self.description)
        print("Priority: %d" % self.priority)

    
