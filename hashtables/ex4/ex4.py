def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    negatives = []
    positives = []
    for val in a:
        if val < 0:
            negatives.append(abs(val))
        if val > 0:
            positives.append(val)

    result = []

    for val in positives:
        if val in negatives:
            result.append(val)
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
