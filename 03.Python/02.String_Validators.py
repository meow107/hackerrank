# input 
# S = "qA2"

# output
# True
# True
# True
# True
# True

has_any_numberic_character = False
has_any_alphabetical_character = False
has_any_digit_character = False
has_any_lowercase_character = False
has_any_uppercase_character = False

for item in S:
    str_item = str(item)
    if str_item.isalnum() and has_any_numberic_character == False:
        has_any_numberic_character = True
    if str_item.isalpha() and has_any_alphabetical_character == False:
        has_any_alphabetical_character = True
    if str_item.isdigit() and has_any_digit_character == False :
        has_any_digit_character = True
    if str_item.islower() and has_any_lowercase_character == False:
        has_any_lowercase_character = True
    if str_item.isupper() and has_any_uppercase_character == False:
        has_any_uppercase_character = True
print(has_any_numberic_character)
print(has_any_alphabetical_character)
print(has_any_digit_character)
print(has_any_lowercase_character)
print(has_any_uppercase_character)
    

       
