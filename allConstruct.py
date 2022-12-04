def allConstruct(target, wordBank):
    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = allConstruct(suffix, wordBank)
            target_ways = suffix_ways.copy()
            [way.append(word) for way in suffix_ways]
            result.append(suffix_ways.copy())

    return result


# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(allConstruct("skateboard", ["bo", "rd", "ska", "sk", "boar"]))
print(allConstruct("alazar", ["a", "l", "az", "ar", "azar", "abcd"]))
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee"]))
