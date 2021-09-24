def chop(list):
    del list[len(list) - 1]
    del list[0]
    return None


def middle(list):
    list = list[1: len(list) - 1]
    return list


letters = ["a", "b", "c"]
alpha = ["a", "b", "c", "d", "e", "f"]

chop(letters)
print(letters)
print(middle(alpha))
