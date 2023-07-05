import os


def return_2_max_val_of_dict(dictionary: dict):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    list1 = list(sorted_dict)
    list2 = [v for k, v in enumerate(sorted_dict) if k < 2]
    print(list(sorted_dict.keys())[:2])
    # print(list2)
    print(enumerate(sorted_dict))

# def func1(dictionary: dict):
#     for item in dictionary.values():
#         print(item)


dict1 = {
    "a": 123,
    "b": 32,
    "c": 99,
    "d": 1,
}
# print(dict1.__getitem__("b"))

# key_value = 99

# for item in dict1.items():
#     if item[1] == key_value:
#         print(item[0])

# return_2_max_val_of_dict(dict1)
# func1(dict1)


# creating a new dictionary
# my_dict = {"Java": 100, "Python": 112, "C": 11}
#
# print(list(my_dict.keys())[list(my_dict.values()).index(112)])
#
# tuple1 = {"a", "b", "c"}
#
# string1 = "".join(tuple1)
# print(string1)

# one-liner
# print(list(my_dict.keys())[list(my_dict.values()).index(100)])

print(__file__)
abs_path = os.path.abspath(__file__)
base_dir = os.path.dirname(abs_path)
print(abs_path)
print(base_dir)

