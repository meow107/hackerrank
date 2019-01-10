#Grading Students 
def solve(grades):
    result = []
    for item in grades:
        print (solve_for_one_number(item))
    
def round_unit(number):
    if number >= 0 and number < 3:
        return number
    elif number >= 3 and number <= 5:
        return 5
    elif number > 5 and number < 8:
        return number
    else:
        return 10

def solve_for_one_number(aNumber):
    if aNumber >= 38 and aNumber < 100 :
        tenDigit = int(aNumber / 10)
        unitNumber = aNumber % 10
        return (aNumber - unitNumber) + round_unit(unitNumber)
    else:
        return aNumber
            
        

grades = [73,65,38,33]
solve(grades)


