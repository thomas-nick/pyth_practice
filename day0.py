nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)
# print(my_list[::-1])

# my_list = [n for n in nums]
# print(my_list)

# # my_list = []
# # # for n in nums:
# # #     my_list.append(n * n - 1)
# # # print(my_list)
# # # print(my_list[::-1])

# # # my_list = [n * n for n in nums]
# # # print(my_list)

# # # # my_list = map(lambda n: n * n, nums)
# # # # print(my_list)

# # my_list = []
# # for n in nums:
# #     if n % 2 == 0:
# #         my_list.append(n)
# # print(my_list)
# # print(sum(my_list))
# # print(max(my_list))

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# # my_list = []
# # for letter in 'abcd':
# #     for num in range(4):
# #         my_list.append((letter, num))
# # print(my_list)

# # my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# names = ['Bruce', 'Clark', 'Lee', 'John']
# heros = ['Spiderman', 'Batman', 'Superman', 'Joker']
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Clark'}
# print(my_dict)

# nums = [1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 5, 7, 6, 3, 2, 1, 2, 3, 45, 7, 89, 2]
# # my_set = set()
# # my_set2 = set()
# # for n in nums:
# #     if n <= 10:
# #         my_set.add(n)
# #     else:
# #         my_set2.add(n)

# # print(my_set)
# # print(my_set2)

# my_set = {n for n in nums}
# print(my_set)
# print(nums)


# def gen_func(nums):
#     for n in nums:
#         yield n * n

# my_gen = (n * (n - 1) for n in nums)
# # my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)
