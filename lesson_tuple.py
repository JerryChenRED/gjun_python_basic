list_height = [168, 179, 178, 182, 187]
list_name = ["Jerry", "Tom", "Thomas", "james", "kd"]
list_tuple = [
    (list_height[0], list_name[0]),
    (list_height[1], list_name[1]),
    (list_height[2], list_name[2]),
    (list_height[3], list_name[3]),
    (list_height[4], list_name[4]),
]
list_tuple_2 = [
    (list_name[0], list_height[0]),
    (list_name[1], list_height[1]),
    (list_name[2], list_height[2]),
    (list_name[3], list_height[3]),
    (list_name[4], list_height[4]),
]

print(list_tuple)
print("Tuple (height, name): ", sorted(list_tuple))
print("Tuple (height, name): ", sorted(list_tuple_2, key = lambda x:x[1]))