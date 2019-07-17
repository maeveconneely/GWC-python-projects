# Syntax to create a new dictionary
#       { key: value }

d = {"mom": "Jen", "dad": "Mike", "sister": "orla"}

# i gets the reference, so use indexing in for loops
for i in d:
    print(d[i])

# i is now the keys
for i in d.keys():
    print(i)

# i in now the values
for i in d.values():
    print(i)


# prints a list of all of the definitions in the dictionary as tuples
print()
print(list(d.items())) # add list() so it looks prettier and becomes list item

print()
# adding new elements
d["sister2"] = "aoife"

print("aoife" in d) # False
print("sister2" in d) # True

print()
# if you're looking for a value that you are not sure exists, use .get()
print(d.get("sister")) # orla
print(d.get("brother")) # None Class: NoneType

# change the element
print()
d["sister2"] = "feena"

# delete an element in the list
del d["sister2"]
print(d)
print()

# get the item back
sister = d.pop("sister") # uses key like .pop() in list uses indexes
print(sister)
print(d)


# clears the dictionary
d.clear()
print()
print(d)

# Notes:
    # changing "" to '' doesn't matter, because python parses them the same way
    # keys can be ints, floats, tuples, strings, or anything that is immutatable
