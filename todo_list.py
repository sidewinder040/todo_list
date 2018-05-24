from ItemClass import todo_item

items = [] # List to contain ToDo ItemClass instances

# Test Item
item1 = todo_item("Test", 3)
items.append(item1)

# Add another item
item2 = todo_item("Test 2", 2)
items.append(item2)

print "---------------------"
print "Items in list..."
item1.Print_Item()
item2.Print_Item()
