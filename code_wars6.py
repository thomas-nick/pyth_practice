def get_middle(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


print(get_middle("buttchek"))
print(get_middle("buttcheek"))
print(get_middle("test"))
print(get_middle("testing"))
