from ItemClass import todoItem

items = []  # List to contain ToDo ItemClass instances

# Test Item
item1 = todoItem("Test", 3)
items.append(item1)

# Add another item
item2 = todoItem("Test 2", 2)
items.append(item2)

print("---------------------")
print("Items in list...")
# item1.print_item()
# item2.print_item()
for i in items:
    i.print_item()
