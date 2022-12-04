def minNumberOfCoinsForChangebestSum(target_sum, numbers, memo=None):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    if memo is None:
        memo = {}

    # if target_sum in memo:
    #     return memo[target_sum]

    shortest_combination = None

    for num in numbers:
        print(target_sum)
        remainder = target_sum - num
        remainder_combination = bestSum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination.copy()
            combination.append(num)
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    # memo[target_sum] = shortest_combination
    return shortest_combination


def bestSumMemo(target_sum, numbers, memo=None):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = bestSum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination.copy()
            combination.append(num)
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


# print(bestSum(3, [2, 3, 1]))
# print(bestSum(8, [2, 3, 5]))
# print(bestSum(8, [1, 4, 5]))
# print(bestSum(100, [1, 2, 5, 25]))


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.

    list_of_coins = minNumberOfCoinForChangeHelper(n, denoms, None)
    print(list_of_coins)
    return len(list_of_coins) if list_of_coins is not None else None


def minNumberOfCoinForChangeHelper(n, denoms, memo=None):
    if n == 0:
        return []
    if n < 0:
        return None
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    shortest_combination = None

    for num in denoms:
        remainder = n - num
        remainder_combination = minNumberOfCoinForChangeHelper(remainder, denoms, memo)
        if remainder_combination is not None:
            combination = remainder_combination.copy()
            combination.append(num)
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    memo[n] = shortest_combination

    return shortest_combination


print(minNumberOfCoinsForChange(7, [1, 5, 10]))
print(minNumberOfCoinsForChange(100, [1, 2, 5, 25]))
