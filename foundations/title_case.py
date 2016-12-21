"""Foundations Problems from CodeWars.

A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'


"""

# My solution:
def title_case(title, minor_words=None):
    """Capitalizes words in title string.  Exception made for words in minor_words, except for the first word."""

    if not title:
        return ''
    
    if minor_words:
        minor_words = minor_words.lower().split(' ')
        minor_len = len(minor_words)
    
    title = title.lower().split(' ')
    output = ''
    for i, word in enumerate(title):
        if word == title[0]:
            title[0] = title[0][0].upper() + title[0][1:]
            output += title[0] + ' '
        elif minor_words and word in minor_words:
            output += word + ' '
        else:
            title[i] = title[i][0].upper() + title[i][1:]
            output += title[i] + ' '
        
    output = output.strip()

    return output

            
# MY ALTERNATE REFACTORED SOLUTION
def title_case(title, minor_words=None):
    """Capitalizes words in title string.  Exception made for words in minor_words, except for the first word."""

    if not title:
        return ''
    
    if minor_words:
        minor_words = minor_words.lower().split(' ')
        minor_len = len(minor_words)
    
    title = title.lower().split(' ')
    output = ''
    for i, word in enumerate(title):
        if i == 0:
            output += title[0][0].upper() + title[0][1:] + ' '
        elif minor_words and word in minor_words:
            output += word + ' '
        else:            
            output += title[i][0].upper() + title[i][1:] + ' '
    
    output = output.strip()

    return output


# Alternative answer




