my_list = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
print(my_list[3])     # access "3"
print(my_list[5])     # access "Hi-Kod"
print(my_list[-1])    # access 4.7
print(my_list[2:6])   # access 9, "3", 8.4, "Hi-Kod"
print(my_list[4:])    # access 8.4, "Hi-Kod", "False", 4.7

new_list = []   # initialize an empty list

for value in my_list:                # traverse my_list
    if isinstance(value, str):       # if a value is string
        new_list.append(value)       # then add it to the new_list

fruit_names = [
    "Apple", "Banana", "Orange", "Grapes", "Strawberry", 
    "Watermelon", "Pineapple", "Mango", "Peach", "Pear", 
    "Cherry", "Kiwi", "Plum", "Lemon", "Avocado", 
    "Raspberry", "Blueberry", "Apricot", "Pomegranate", "Coconut"
]
for count, value in enumerate(fruit_names):
    print("Element in index {:2d} is {}".format(count,value))