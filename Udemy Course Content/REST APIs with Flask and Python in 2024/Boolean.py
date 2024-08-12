friends = ["Bob", "Rolf", "Anne"]
abroad = ["Bob", "Rolf", "Anne"]
print(friends == abroad)  # Output: True
print(friends is abroad)  # Output: False

abroad = friends
print(friends is abroad)  # Output: True


# Equal to
print(5 == 5)  # Output: True

# Not equal to
print(10 != 10)  # Output: False

# Greater than
print(5 > 3)  # Output: True

# Less than
print(5 < 3)  # Output: False

# Greater than or equal to
print(5 >= 5)  # Output: True

# Less than or equal to
print(5 <= 4)  # Output: False




# Creating two separate lists with the same elements
friends = ["Bob", "Rolf", "Anne"]
abroad = ["Bob", "Rolf", "Anne"]

# Comparing elements inside the lists
print(friends == abroad)  # Output: True

# Comparing memory location of the lists
print(friends is abroad)  # Output: False

# Pointing abroad to the same list as friends
abroad = friends

# Now both point to the same list
print(friends is abroad)  # Output: True