def canConstruct(target, wordBank, memo=None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ska", "sk", "boar"]))
print(canConstruct("alazar", ["a", "l", "az", "ar", "abcd"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
