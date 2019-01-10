def capitalize(string):
    splited_string = string.split(" ")
    for index in range(len(splited_string)):
        splited_string[index] = (str(splited_string[index])).capitalize()
    return " ".join(splited_string)

# input 
# s = "hello world"

# output 
# Hello World

# s = "hello world"
# print (capitalize(s))

