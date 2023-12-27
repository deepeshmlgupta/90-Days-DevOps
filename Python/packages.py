import os
import shutil

print(shutil.disk_usage("/"))
print(os.getcwd())

print("\n \n")

total, used, free = shutil.disk_usage("/")
print("\n \n")


print("This will be the result in BITS")

print("Total Disk Space: ", total)
print("Used Disk Space: ", used)
print("Free Disk Space: ", free)

# converting them in GB     (// will give us the approx value)  
# F = Formating String in this we can add multiple mutilple string
print("\n \n")

print("This will be the result in GB")

print(f"Total Disk Space: {total // (2**30)} GB")
print(f"Used Disk Space: {used // (2**30)} GB")
print(f"Free Disk Space: {free // (2**30)} GB")