def print_tickets(number_of_tickets, *name):
    i = 0
    while i < number_of_tickets:
        print(name[i])
        i += 1


names = ('John', 'Alice')
print_tickets(2, names)
