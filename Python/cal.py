a = float(input("Enter the number: "))
b = float(input("Enter the number: "))
choice = input("Enter the operation +, -, /, * : ")

if(choice == "+"):
    sum = a + b
    print("Addition: ", sum)
    #sum = int(a) + int(b)
if(choice == "*"):
    product = a*b
    print("Multiplication", product)
if(choice == "-"):
    sub = a-b
    print("Subtraction", sub)
if(choice == "/"):
    divide = a/b
    print("Division", divide)
else:
    print("invalid operation applied")
