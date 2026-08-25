even_number=[]
odd_number=[]
for i in range(1,51):
    if i%2==0:
        even_number.append(i)
    else:
        odd_number.append(i)
    print("number is even",even_number)
    print("number is odd",odd_number)