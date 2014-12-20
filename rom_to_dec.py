def convert_to_decimal(roman):
    '''Write a function that converts a Roman numeral number to a decimal number.
    Function takes a string as input and returns an integer. Assum roman numeral is
    passed in in standard format for roman numbers.

    >>> convert_to_decimal('XLVIII')
    48

    >>> convert_to_decimal('LXXXVI')
    86

    >>> convert_to_decimal('IX')
    9

    >>> convert_to_decimal('MMCDXXXIV')
    2434
    '''
    
    convertor = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimals = []

    #translate using dictionary
    for i in range(len(roman)):
        decimals.append(convertor[roman[i]])
    
    #check order for everything except the last digit
    decimals_ordered = []
    counter = 0
    while counter < (len(decimals) -1) :
        if decimals[counter] < decimals[counter + 1]:
            decimals_ordered.append(decimals[counter + 1] - decimals[counter])
            counter += 1
        else:
            decimals_ordered.append(decimals[counter])
        counter += 1

    #check if the last digit needs to be added
    if decimals[-2] >= decimals[-1]:
        decimals_ordered.append(decimals[-1])

    #sum everything
    sum = 0
    for num in decimals_ordered:
        sum += num
    return sum
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()






