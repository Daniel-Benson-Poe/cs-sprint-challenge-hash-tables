def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    i = 0
    for weight in weights:
        if weight in hash.keys():
            hash[weight].append(i)
        else:
            hash[weight] = [i]
        i += 1

    for weight in hash:
        if limit - weight in hash.keys() and limit - weight == weight:
            index_list = []
            index_list.append(max(hash[weight][0], hash[limit-weight][1]))
            index_list.append(min(hash[weight][0], hash[limit - weight][1]))
            return index_list
        elif limit - weight in hash.keys() and limit - weight != weight:
            index_list = []
            index_list.append(max(hash[weight][0], hash[limit-weight][0]))
            index_list.append(min(hash[weight][0], hash[limit - weight][0]))
            return index_list
        
    return None

# Example:
# ```
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
# ```

if __name__ == "__main__":
    weights_2 = [4, 4]
    print(get_indices_of_item_weights(weights_2, 2, 8))