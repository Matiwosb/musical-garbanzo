from random import randint


def luhn_last_digit(n):
    num = n[-1::-2]
    b = 0
    for a in num:
        i = int(a) * 2
        if i > 9:
            i = i - 9
            b = b + i
            num_2 = n[-2::-2]
            for c in num_2:
                j = int(c)
                b = b + j
                x = 0
                while (b + x) % 10 != 0:
                    x += 1
                    return x
                    # print(luhn_last_digit(''))
def generate_card_number(card_type):
    card_num = ''
    if card_type == 'v':
        card_num += '4'
        card_len = [13, 16, 19]
        n = randint(0, 2)
        p = card_len[n]
        for i in range(0, p):
            card_num = str(card_num) + randint(0, 9)
    elif card_type == 'm':
            a = randint(51, 55)
            b = randint(222100, 272099)
            i = [a, b]
            n = randint(0, 1)
            s = str(i[n])
            card_num += s
            for e in range(15 - len(s)):
                card_num += str(randint(0, 9))
    else:
            return None

        # using previous function to make it valid credit number
    card_num += str(luhn_last_digit(card_num))


    return card_num
while True:
    # prompting user to enter card type
    card_type = input('Enter v for a Visa number, m for MasterCard, anything else to exit: ')
    # if not a valid card type then exiting program
    if card_type != 'v' and card_type != 'm':
        break
    card_num = generate_card_number(card_type)
    print(card_num)

print("Bye, don't have *too* much fun...")

