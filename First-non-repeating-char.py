from collections import OrderedDict

def first_non_repeating_char(s):
    freq = OrderedDict()


    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char, count in freq.items():
        if count == 1:
            return char

    return None  


s = "swiss"
result = first_non_repeating_char(s)
if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("No non-repeating character found.")


# Uses OrderedDict to maintain insertion order.
# You can use a normal dictionary (dict) to count character frequencies, but if you're using Python before version 3.7, the order is not guaranteed.



def first_non_repeating_char(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return None

    # Using OrderedDict is safe for maintaining insertion order in all supported Python versions.
    # In modern Python (3.7+), regular dict also preserves insertion order.