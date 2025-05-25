# Check if two strings are anagrams

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
   
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
