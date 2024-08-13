# Defining a list
l = ["Bob", "Rolf", "Anne"]

# Accessing elements
print(l[0])  # Output: Bob

# Modifying elements
l[0] = "Smith"
print(l)  # Output: ['Smith', 'Rolf', 'Anne']

# Adding elements
l.append("John")
print(l)  # Output: ['Smith', 'Rolf', 'Anne', 'John']

# Removing elements
l.remove("Rolf")
print(l)  # Output: ['Smith', 'Anne', 'John']

///////////////////////////////////////////////

# Defining a tuple
t = ("Bob", "Rolf", "Anne")

# Accessing elements
print(t[0])  # Output: Bob

# Trying to modify elements (will raise an error)
# t[0] = "Smith"  # Error: 'tuple' object does not support item assignment

///////////////////////////////////////////////

# Defining a set
s = {"Bob", "Rolf", "Anne"}

# Adding elements
s.add("Smith")
print(s)  # Output: {'Anne', 'Bob', 'Smith', 'Rolf'}

# Removing elements
s.remove("Rolf")
print(s)  # Output: {'Anne', 'Bob', 'Smith'}

# Adding a duplicate element (will not be added)
s.add("Smith")
print(s)  # Output: {'Anne', 'Bob', 'Smith'}


