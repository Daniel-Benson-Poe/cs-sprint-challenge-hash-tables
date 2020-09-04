from hashtable import HashTable

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
    hash = HashTable(length*2)
    for ticket in tickets:
        hash.put(ticket.source, ticket.destination)

    route = []
    next_dest = ""
    dest = hash.get("NONE")
    while dest != "NONE":
        route.append(dest)
        dest = hash.get(dest)
    route.append("NONE")
    return route

if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]
    print(reconstruct_trip(tickets, len(tickets)))