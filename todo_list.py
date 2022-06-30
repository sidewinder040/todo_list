from ItemClass import todo_item

todo_list = [] # List to hold items

todo_list.append(todo_item("Test", 3))
todo_list.append(todo_item("Another Item", 2))

for item in todo_list:
    item.Print_Item()
