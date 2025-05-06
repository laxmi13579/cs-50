# Get user input
age = int(input("Enter your age: "))

# Determine age category
if age >= 0 and age <= 1:
    category = "Infant / Baby"
elif age >= 2 and age <= 3:
    category = "Toddler"
elif age >= 4 and age <= 5:
    category = "Preschooler"
elif age >= 6 and age <= 12:
    category = "Child / Grade-schooler"
elif age >= 13 and age <= 17:
    category = "Teen / Adolescent"
elif age >= 18 and age <= 24:
    category = "Young Adult"
elif age >= 25 and age <= 34:
    category = "Adult (Early)"
elif age >= 35 and age <= 44:
    category = "Adult (Mid)"
elif age >= 45 and age <= 54:
    category = "Middle-Aged Adult"
elif age >= 55 and age <= 64:
    category = "Older Adult / Pre-Senior"
elif age >= 65 and age <= 74:
    category = "Senior (Young-Old)"
elif age >= 75 and age <= 84:
    category = "Senior (Middle-Old)"
elif age >= 85:
    category = "Senior (Oldest-Old)"
else:
    category = "Invalid age"

# Output the result
print("Age category:", category)
