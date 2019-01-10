# input
# Sorting1234

# output
# ginortS1324


# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Great comment from forum:

# 1. if isdigit, give higher priority. so alphas come before digits now
# Ex- Sorting1234 => Sorting1234
# 2. if isevendigit, give higher priority. so, among the digits, now even have higher priority. While the 1st part in key is maintained
# Ex- Sorting1234 => Sorting1324
# 3. next priority goes to upper case keeping both previous keys maintained. so uppercase can't go after the numbers as that key has higher priority.
# Ex - Sorting1234 => ortingS1324
# 4. next priority is given to lowercase characters, but that isn't required as it's the only ones left in alphanumeric characters. We will get the same output either way
# Ex - Sorting1234 => ortingS1324
# 5. now sort according to the characters, but keeping all the previous keys in mind, all the characters will be sorted in place, keeping their order as defined in previous keys
# Ex - Sorting1234 => ginortS1324

s = input()
s = sorted(s, key = lambda x: (
                                str(x).isdigit(),
                                str(x).isdigit() and int(str(x)) % 2 == 0,
                                str(x).isalpha(),
                                str(x).isupper(),
                                x
                                )
            ,reverse = False
          )



print(*s, sep = '')
