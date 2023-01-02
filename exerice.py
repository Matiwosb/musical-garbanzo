from functools import reduce

def square(num):
    return num * num
my_list = [1,2,3,4,5,6]

# map takes a function and applies
# to each element on the list
res = list(map(square, my_list))

print(res)
#
# res = list(map(lambda x: x * x, my_list))
# print(res)

# res = list(map(lambda x: x**2 if x % 2 == 0 else x**3, my_list))
# print(res)

# def square_or_odd(_list):
#     my_list = []
#     for i in _list:
#         if i % 2 == 0:
#             my_list.append(i**2)
#         else:
#             my_list.append(i**3)
#     return my_list
#
# def square_or_odd2(_list):
#     for i in _list:
#         if i % 2 == 0:
#             my_list.append(i**2)
#         else:
#             my_list.append(i**3)
#res = square_or_odd(my_list)
#print(res)

# res = list(map(square_or_odd2, my_list))
# print(res)
# res = list(filter(lambda x: x%2 == 0, my_list))
# print(res)
#
# res = reduce(filter(lambda x: x%2 == 0, my_list))
# print(res)

# dogs = ["Todd", "Tom", "Bob"]
# big_dogs = []
# for dog in dogs:
#     big_dogs.append("Big {}".format(dog))
#
# print(big_dogs)
# print()
#
# big_dogs = ["Big {}".format(dog) for dog in dogs]
# print(big_dogs)
#
#
# # my_list = [2, 4, 6, 8, 10]
# # res = [2:4, 4:16, 6:36, 8:64, 10:100]
#
# res = {i : i**2 for i in my_list}
#
# '''
# res = {4:[1,2,3,4,5], 16:[1,2,3,4,5], 36:[1,2,3,4,5], 64:[1,2,3,4,5], 100:[1,2,3,4,5]}
# '''
#
# res = {i**2:[i/2 for i in my_list] for i in my_list}