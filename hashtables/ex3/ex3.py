# We can save each individual value (number) in the list of lists as the key
# We can save a boolean value as the dictionary keys' values
# True indicates that value is found in all lists within the input
# False indicates that value is NOT found in all the lists given by the input
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    inter_dict = {}
    length = len(arrays)
    for arr in arrays:
        for i in range(len(arr)):
            if str(arr[i]) in inter_dict.keys():
                inter_dict[str(arr[i])] += 1
            else:
                inter_dict[str(arr[i])] = 1

    result = []
    for pair in inter_dict:
        if inter_dict[pair] == length:
            result.append(int(pair))

    return result


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays = [
    #         list(range(1000000, 2000000)) + [1,2,3],
    #         list(range(2000000, 3000000)) + [1,2,3],
    #         list(range(3000000, 4000000)) + [1,2,3],
    #         list(range(4000000, 5000000)) + [1,2,3],
    #         list(range(5000000, 6000000)) + [1,2,3],
    #         list(range(6000000, 7000000)) + [1,2,3],
    #         list(range(7000000, 8000000)) + [1,2,3],
    #         list(range(8000000, 9000000)) + [1,2,3],
    #         list(range(9000000, 10000000)) + [1,2,3],
    #         list(range(10000000, 11000000)) + [1,2,3]
    #     ]

    arrays = [
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ]
    print(intersection(arrays))
