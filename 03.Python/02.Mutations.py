# input
# string = abracadabra
# position = 5 
# character = 'k'

# output
# abrackdabra

def mutate_string(string, position, character):
    return (string[:position] + character + string[position + 1:])