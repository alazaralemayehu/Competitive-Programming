def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            new_remainder = remainder_result.copy()
            new_remainder.append(num)
            memo[target_sum] = new_remainder
            print(memo)
            return memo[target_sum]

    memo[target_sum] = None
    return None


# print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
# print(how_sum(7, [2, 4]))
# print(how_sum(6, [2, 3, 5]))
# print(how_sum(300, [7, 14]))
