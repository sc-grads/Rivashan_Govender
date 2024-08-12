# Ask the user if they would like to play
while True:
    user_input = input("Would you like to play? (Y/n) ")
    if user_input == 'n':
        break

    # If they want to play, ask for a number and compare it
    user_number = int(input("Enter a number: "))
    if user_number == 5:
        print("Correct number!")
    else:
        print("Wrong number, try again.")

# For loop example with friends list
friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

# For loop with range
for i in range(4):
    print(f"{i} is my friend.")

# For loop to calculate average grade
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# Using sum function to calculate average grade
total = sum(grades)
amount = len(grades)
print(total / amount)
