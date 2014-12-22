def unique_characters(string):
    '''Determine if the string contains all unique characters.

    Python implementation of problem 1-1 in Cracking the Coding Interview.

    Args:
        string: a string
    Returns:
        Boolean

    >>> unique_characters('12basjj')
    False

    >>> unique_characters('a')
    True

    >>> unique_characters('\|012 fF')
    True

    >>> unique_characters('kitten')
    False

    '''
    my_dict = {}
    for letter in string:
        if my_dict.get(letter):
            return False
        my_dict[letter] = 1
    return True

def unique_characters2(string):
    '''Determine if the string contains all unique characters.

    Python implementation of problem 1-1 in Cracking the Coding Interview with no
    dictionaries

    Args:
        string: a string
    Returns:
        Boolean

    >>> unique_characters2('12basjj')
    False

    >>> unique_characters2('a')
    True

    >>> unique_characters2('\|012 fF')
    True

    >>> unique_characters2('kitten')
    False

    '''
    letters = []
    for letter in string:
        if letter in letters:
            return False
        else:
            letters.append(letter)
    return True

def reverse_string(string):
    '''Reverse a string.

    Args:
        string: a string
    Returns:
        the string reversed

    >>> reverse_string('abcde')
    'edcba'

    >>> reverse_string('a')
    'a'

    >>> reverse_string('abba')
    'abba'

    >>> reverse_string('abc ')
    ' cba'

    '''

    new_string = ''
    for i in range(len(string)):
        new_string = new_string + string[len(string) - i - 1]
    return new_string

def is_permutation(string1, string2):
    '''Determine if one string is a permutation of another.  Assume equal lengths

    Args:
        string1: a string
        string2: a string of equal length as string 1

    Returns:
        Boolean

    >>> is_permutation('abcde', 'cabed')
    True

    >>> is_permutation('abc', 'def')
    False

    >>> is_permutation('aaabbbccc', 'abcabccab')
    True

    '''

    dictionary1 = {}
    dictionary2 = {}

    for letter in string1:
        dictionary1[letter] = dictionary1.setdefault(letter, 0) + 1

    for letter in string2:
        dictionary2[letter] = dictionary2.setdefault(letter, 0) + 1

    return dictionary1 == dictionary2

def replace_spaces_20(string):
    '''Replace all spaces in a string with "%20". Trim spaces for front and end

    Args:
        string: a string
    Returns:
        a string

    >>> replace_spaces_20('I love Python    ')
    'I%20love%20Python'

    >>> replace_spaces_20('hohoho')
    'hohoho'

    '''
    new_string = ''
    string = string.rstrip()
    for i in range(len(string)):
        if string[i] == " ":
            new_string = new_string + '%20'
        else:
            new_string = new_string + string[i]
    return new_string

def compress_string(string):
    '''Compress a string to give a character and the number of times a character
    is repeated.

    Args:
        string: input string of only upper and lower case a-z
    Returns:
        string with the character followed by the number of times that it occurs.
        If the compressed string length is not less than the original string length,
        tha original string is returned.

    >>> compress_string('aabccccaaa')
    'a2b1c4a3'

    >>> compress_string('aabbcc')
    'aabbcc'

    >>> compress_string('aabcccccca')
    'a2b1c6a1'

    '''
    new_string = ''
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            new_string += string[i]
            new_string += str(count)
            count = 1 
        if i + 2 == len(string):
            new_string += string[-1]
            new_string += str(count)
         
    if len(new_string) < len(string):
        return new_string
    else:
        return string

if __name__ == '__main__':
    import doctest
    doctest.testmod()

