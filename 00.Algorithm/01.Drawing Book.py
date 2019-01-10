import sys

#Drawing Book

def solve(n, p):
    # Complete this function
    end_page = n
    is_odd_p = p % 2 != 0
    is_even_p = p % 2 == 0

    is_odd_n = n % 2 != 0
    is_even_n = n % 2 == 0
    
    # two ways
    if (p - 1) < (n - p):
        if is_odd_p:
            return (int)(p / 2)
        else:
            return (int)((p +  1) / 2)
    else:
        if (is_even_n and is_even_p) or (is_odd_n and is_odd_p):
            return int((n - p) / 2)
        elif is_even_n and is_odd_p:
            odd_p_page = p - 1
            return int((n - odd_p_page) / 2)
        elif is_odd_n and is_even_p:
            even_p_page = p + 1
            return int((n - even_p_page) / 2)
   
n = 5
p = 4

result = solve(n, p)
print(result)

