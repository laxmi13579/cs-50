name = input("Enter your name? ")

# remove white space right and left from the string 
print(f"Hello! {name.strip()}")

# Capitalize user's name like first alphabet to capital
print(f"Hello! {name.title()}")

#  direction first strip and then title 
print(f"Hello! {name.strip().title()}")

name = input("Enter your name? ").strip().title()
print(f"Hello! {name}")

# split name with white space
first, last = name.split(" ")
print(f"Hello! {first}")
