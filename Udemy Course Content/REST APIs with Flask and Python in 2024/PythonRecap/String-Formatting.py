name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)  # Output: Hello, Bob

name = "Rolf"
with_name = greeting.format(name)
print(with_name)  # Output: Hello, Rolf

# Longer template
longer_phrase = "Hello, {}. Today is {}."
formatted_string = longer_phrase.format("Rolf", "Monday")
print(formatted_string)  # Output: Hello, Rolf. Today is Monday.