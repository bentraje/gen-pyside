from manager.todo import Item, Items

items = Items()

items.add(Item('apple', 2))
items.add(Item('orange', 2))
items.add(Item('bannana', 2))
items.add(Item('pieapple', 2))
items.add(Item('milk', 2))

print("Here is your list: ")
for item in items:
    print(item)