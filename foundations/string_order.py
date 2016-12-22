"""Fundamental Problems from CodeWars.
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""

# My solution:
def order(sentence):
    """Sort string, where each word will contain it's correct position (number, 1 thru 9)."""

    if not sentence:
        return ''

    sentence = sentence.split(' ')
    num_word = {}

    for word in sentence:
        for ltr in word:
            try:
                ltr = int(ltr)
                num_word[ltr] = word
                break
            except ValueError:
                pass

    sent_len = len(sentence)
    output = ''
    for i in range(1, sent_len + 1):
        output += str(num_word[i]) + ' '

    return output.strip()


# Alternative answer
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


# Alternative answer
def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)


# Alternative answer
def order(sentence):
    def sort_key(s):
        return next(c for c in s if c.isdigit())
    return ' '.join(sorted(sentence.split(), key=sort_key))
