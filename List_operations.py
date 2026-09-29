# Create a list of numbers
numbers = [10, 30, 20, 50, 40]

print("Original list:", numbers)

# Insertion
numbers.insert(2, 25)
print("After insertion:", numbers)

# Deletion
numbers.remove(30)
print("After deletion:", numbers)

# Sorting
numbers.sort()
print("After sorting:", numbers)

# Slicing
print("Sliced list:", numbers[1:4])

# Searching
search = int(input("Enter number to search: "))

if search in numbers:
    print(search, "is found in the list")
else:
    print(search, "is not found in the list")