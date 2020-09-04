#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first we create a hash table
    hash_table = {}

    # then we define the length of the route
    route = [None] * length

    for ticket in tickets:
        # then we push the ticket info into hash table we've created
        hash_table[ticket.source] = ticket.destination

    # then we turn hash table into  a lists of keys and values
    source = list(hash_table.keys())
    destination = list(hash_table.values())

    # then we set the route to start at NONE and set the 2nd position to 1st position
    route[0] = hash_table["NONE"]
    route[1] = hash_table[route[0]]

    # then we iterate over the route find the location of i and subtract 1
    if length > 2:
        for i in range(2, length):
            route[i] = hash_table[route[i - 1]]

    return route
