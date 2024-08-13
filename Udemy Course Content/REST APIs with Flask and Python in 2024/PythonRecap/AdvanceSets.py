friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = friends.difference(abroad)
print(local)  # Output: {'Rolf'}

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
print(friends)  # Output: {'Bob', 'Anne', 'Rolf'}

# Difference in reverse
abroad_diff = abroad.difference(friends)
print(abroad_diff)  # Output: set()

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
print(friends)  # Output: {'Bob', 'Anne', 'Rolf'}

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)  # Output: {'Bob', 'Jen'}


