
# required method
def format_number(n, d, symbol):
    # if n is 0, return "0"
    if n == 0:
        return '0'
    # create an empty string to store the result
    result = ""
    # check if n is negative
    negative = n < 0
    # if yes, make n positive
    if negative:
        n = -n
    # initialize a counter to 0
    counter = 0
    # loop as long as n > 0
    while n > 0:
        # extract last digit of n
        last_digit = n % 10
        # remove last digit from n
        n = n // 10
        # prepend last digit to result (add at the beginning)
        result = str(last_digit) + result
        # increment counter
        counter += 1
        # for every d digits, prepend the symbol, only if there are more digits left to process
        if counter % d == 0 and n > 0:
            result = symbol + result
    # if n was negative, prepend a minus sign to result
    if negative:
        result = '-' + result
    # return result
    return result


# code for testing
if __name__ == '__main__':
    # use the given test cases
    print(format_number(77500000, 3, ','))
    print(format_number(77500000, 4, ','))
    print(format_number(42, 3, ','))
    print(format_number(42, 2, ','))
    print(format_number(42, 1, ','))
    print(format_number(-1234567, 3, '.'))
    print(format_number(-3840, 3, ' '))