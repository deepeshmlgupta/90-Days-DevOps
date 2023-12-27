#
#
# The main diff between array and list is that 
# Array is the data structure which can only hold same or similar type of data   while
# List is the data structure that can hold differnet type of data or datatype
#
#
list_items = []

list_items.append("Deepesh")
list_items.append("21")
print(list_items)



list_of_cloud = ["aws", "azure", "gcp"]
list_of_evn = ["dev, test", "prod"]

print(list_of_cloud[2])

#
# for loops
#

#list iteration
for i in range(2):
    i = "Google Cloud"
    # print("Google Cloud")
    print(i)

for cloud in list_of_cloud:
    print(cloud)


#
# 
# Dictionary
# Anything which is described in a pair of key and value is known as dictionary
# 
# 

dict_of_cloud = {
    "aws": "Amazon Web Services",
    "azure": "Microsoft Azure",
    "gcp": "Google Cloud Platform"
}

# Use the update method to add a new key-value pair
dict_of_cloud.update({
    "oracle": "Oracle Cloud"
})

print(dict_of_cloud["gcp"])
# Correct the case of "Oracle" in the get method
print(dict_of_cloud.get("oracle", "not found"))
