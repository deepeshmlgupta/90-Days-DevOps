#taking string type input 
name = input("Enter your name: ")
print("Hello, " + name)
print(type(name))


#taking int type input

number = int(input("Enter your number: "))
print("The number is ", number)
print(type(number))

#taking inputs in form of list sets

List = list()
Set = set()
l = int(input("Enter the size of List "))
s = int(input("Enter the size of Set "))

print("Enter the elements of list ")
for i in range(0, l): 
    List.append(int(input()))

print("Enter the elements of Set ")
for i in range(0, s):
    Set.add(int(input()))

print(List)
print(Set)