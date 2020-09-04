def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first we create an empty list
    result = []
    # then we create an empty hash table
    hash_table = {}

    # subarray is single list containing the integers within list
    for subarray in arrays:
        for num in subarray:
            if num not in hash_table:  # if the num is not in the hash table - add it
                hash_table[num] = 1  # num = key, with 0 value

            else:
                # append num to the intersection list
                result.append(num)
    # creates new list, removing any potential duplicates from the list
    result = list(dict.fromkeys(result))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
