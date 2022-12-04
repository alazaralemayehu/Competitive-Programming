def arrayOfProducts(array):
    # Write your code here.
    output = []

    dict_right = {}
    dict_left = {}
    left_product = 1
    right_product = 1

    for i in range(len(array)):
        dict_left[i] = left_product
        left_product *= array[i]
    for i in range(len(array) - 1, -1, -1):
        dict_right[i] = right_product
        right_product *= array[i]

    for i in range(len(array)):
        output.append(dict_left[i] * dict_right[i])

    return output
