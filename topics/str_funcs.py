name = "Endian"

print("\n")
# Print name(doesn't include end-line char)
print(len(name))

# Find index of given char
print(name.find("d"))

#To uppercase 1st letter(any additional words or spaces not capitalised)
print(name.capitalize())

#To uppercase
print(name.upper())

#To lowercase
print(name.lower())

# Is digit?
print(name.isdigit())

# Is aplhabet?(if space present, then no)
print(name.isalpha())

# To count number of given chars in a string
print(name.count("n"))

# Replace chars in string
print(name.replace("n","o"))

# Display a string multiple times
print(name * 3)

print("\n")