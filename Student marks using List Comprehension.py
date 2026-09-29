# Accept student marks
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

print("All marks:", marks)

# List comprehension for marks greater than 50
greater_than_50 = [m for m in marks if m > 50]

print("Marks greater than 50:", greater_than_50)