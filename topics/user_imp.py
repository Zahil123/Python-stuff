# If a even a float is supplied to a variable type casted as int, it will throw an error instead of using the int part 
# Accept I/P
print("\n")
name = input("Enter your name: ")       # Whenever we accept user I/P, it is always as string data type

#age = input("What's  your age:")       Will produce error when ++ed

age = int(input("What's  your age:"))     #Fixed
age += 1

height = float(input("How tall are you: "))

print("\nHello " + name)

print("You are " + str(age) + "years old")

print("You are " + str(height) + "cm tall")
print("\n")