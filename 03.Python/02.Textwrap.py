import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width) 

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4

# string = "This is a very very very very very long string."
# w = 8

print(textwrap.fill(string, w))