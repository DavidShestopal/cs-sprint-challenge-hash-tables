def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #  first we create an empty list
    result = []
    # then we create an empty hash table
    numbers = {}

    for num in a:
        # then we add the numbers to the hash table
        numbers[num] = 1
    for num in a:
        # if numbers * -1 is in the hash table and a positive number exsists, add number into to the result array
        if (num*-1) in numbers and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
