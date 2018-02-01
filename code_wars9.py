# # def find_short(s):
# #     # your code here

# #     return l # l: shortest word length

# x = "bitcoin take over the world maybe who knows perhaps"
# my_list = list(x.split())
# x = [len(i) for i in my_list]
# final = sorted(x)
# print(final[0])
# # new = l.sort()
# print(my_list)
# print(x)
# print(final)


def find_short(s):
    my_list = list(s.split())
    x = [len(i) for i in my_list]
    final = sorted(x)
    l = final[0]

    return l  # l: shortest word length


def find_short(s):
    return min(len(x) for x in s.split())
