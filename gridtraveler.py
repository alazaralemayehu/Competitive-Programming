def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def grid_traveler_memo(m, n, memo=None):

    if memo == None:
        memo = {}
    key = str(m) + ":" + str(n)

    if key in memo:
        return memo[key]

    key2 = str(n) + ":" + str(m)
    if key2 in memo:
        return memo[key2]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
    return memo[key]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))

import datetime

start = datetime.datetime.now()
print(grid_traveler_memo(280, 580))
end = datetime.datetime.now()
print(end - start)
