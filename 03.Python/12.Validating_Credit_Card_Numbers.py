import re

def is_credit_card_numbers(card_number):
    start_with_456 = r'[456].+'
    digits_0_9 = r'\w+|[0-9]+'
    no_white_space_underscore = r'[^\s_]+'
    more_4th_consecutive_repeated_digits = r'(\d)\1{3,}'
    group_4_separated = r'(\d{4})-(\d{4})-(\d{4})-(\d{4})'
    is_group_4_seperated = re.findall(group_4_separated, card_number)
    if is_group_4_seperated:
        card_number = str(card_number).replace('-', '')
    is_start_with_456 =  bool(re.match(start_with_456, card_number))
    is_contains_16_digits = len(card_number) == 16
    is_no_white_space_under_score = bool(re.match(no_white_space_underscore, card_number))
    is_digits_0_9 = bool(re.match(digits_0_9, card_number))
    is_more_4th_consecutive_repeated_digits = bool(re.findall(more_4th_consecutive_repeated_digits, card_number))

    if (is_start_with_456 and is_contains_16_digits and is_digits_0_9 and is_no_white_space_under_score and not is_more_4th_consecutive_repeated_digits):
        return True
    return False

n = int(input())
for i in range(n):
    print('Valid' if is_credit_card_numbers(input()) else 'Invalid')