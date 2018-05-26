from ItemClass import todoItem

items = [] # List to contain ToDo ItemClass instances

# Test Item
item1 = todoItem("Test", 3)
items.append(item1)

# Add another item
item2 = todoItem("Test 2", 2)
items.append(item2)

print "---------------------"
print "Items in list..."
item1.print_tem()
item2.print_tem()
