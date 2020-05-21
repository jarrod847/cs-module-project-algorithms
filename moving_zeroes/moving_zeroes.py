'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    new_list = []
    for i in arr:
        if i == 0:
            new_list.append(i)
        else:
            new_list.insert(0, i)
    return new_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
