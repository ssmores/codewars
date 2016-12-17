"""Foundations Problems from CodeWars.

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
"aa11" -> 2 # 'a' and '1'
"""

# My solution:
def duplicate_count(text):
    """Counts distincts letters and digits. Returns how many items appear more than once."""

    unique_char = {}
    output = set()
    for item in text:
        if item.lower() in unique_char:
            unique_char[item.lower()] += 1
            output.add(item.lower())
        else:
            unique_char[item.lower()] = 1

    return len(output)


# Alternative answer
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


#Alternative answer
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)


# Alternative answer
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)


