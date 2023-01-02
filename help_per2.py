# importing randint function
from random import randint


# function to add appropriate last digit
# to make it a valid credit card number
def luhn_last_digit(n):
    n2 = ""
    s = 0

    if (len(n) % 2 == 0):
        checkI = 1
    else:
        checkI = 0

    # traversing the string credit card character by character
    for i in range(0, len(n)):
        # if current index position is to be doubled
        # then doubling it and subtracting 9
        # if doubled number exceeds 9
        if i % 2 == checkI:
            temp = int(n[i]) * 2
            if temp > 9:
                n2 += str(temp - 9)
            else:
                n2 += str(temp)
        # otherwise simply appending it
        else:
            n2 += n[i]
    # getting sum of all digit
    for i in range(len(n2)):
        s += int(n2[i])

    # last number to be added such that
    # total value ends with 0
    last = (10 - s % 10) % 10

    return last


# function to randomly generate a valid card number
def generate_card_number(card_type):
    card_number = ""
    if card_type == "v":
        card_number += '4'

        # list of possible length to be added
        possibleLength = [11, 14, 17]

        ni = randint(0, 2)
        n = possibleLength[ni]

        # filling upto second last with random numbers
        for i in range(0, n):
            card_number += str(randint(0, 9))
    elif card_type == 'm':
        first = randint(51, 55)
        second = randint(222100, 272099)

        # list of possible starter number to be used
        possibleStarter = [first, second]
        ni = randint(0, 1)
        starter = str(possibleStarter[ni])
        card_number += starter

        for i in range(15 - len(starter)):
            card_number += str(randint(0, 9))
    else:
        return None

    # using previous function to make it valid credit number
    card_number += str(luhn_last_digit(card_num))ber))

    return card_number


# infinite loop
while True:
    # prompting user to enter card type
    card_type = input('Enter v for a Visa number, m for MasterCard, anything else to exit: ')
    # if not a valid card type then exiting program
    if card_type != 'v' and card_type != 'm':
        break
    card_number = generate_card_number(card_type)
    print(card_number)

print("Bye, don't have *too* much fun...")
print(luhn_last_digit('042'))
