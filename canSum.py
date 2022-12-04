def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):
            return True
    return False


def can_sum(target_sum, numbers, memo=None):
    if memo == None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        memo[remainder] = can_sum(remainder, numbers, memo)
        if memo[remainder]:
            return True
    return False


# print(can_sum(7, [2, 3]))
# print(can_sum(7, [5, 3, 4, 7]))
# print(can_sum(7, [2, 4]))
# print(can_sum(7, [2, 3, 5]))
print(can_sum(300, [7, 14]))
