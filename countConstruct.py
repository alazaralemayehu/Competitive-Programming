def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return 1
    total_count = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            num_ways = countConstruct(suffix, wordBank, memo)
            total_count += num_ways

    memo[target] = total_count
    return memo[target]


print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("skateboard", ["bo", "rd", "ska", "sk", "boar"]))
print(countConstruct("alazar", ["a", "l", "az", "ar", "azar", "abcd"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
