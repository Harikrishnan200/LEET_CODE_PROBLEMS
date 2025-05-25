# check whether a string is a substring of another string


def is_substring(str1, str2):
    return str2 in str1

str1 = "hello world"
str2 = "world"

if is_substring(str1, str2):
    print(f'"{str2}" is present in "{str1}".')
else:
    print(f'"{str2}" is NOT present in "{str1}".')




# Without using  in operator


def is_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)


    for i in range(len1 - len2 + 1):
        if str1[i:i+len2] == str2:
            return True
    return False


str1 = "hello world"
str2 = "world"

if is_substring(str1, str2):
    print(f'"{str2}" is present in "{str1}".')
else:
    print(f'"{str2}" is NOT present in "{str1}".')
