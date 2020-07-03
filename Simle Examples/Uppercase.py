# Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with the first letter capitalized.
# Eg., print(capitalize('word')) should print the word Word.
# Then, given a line of lowercase ASCII words (text separated by a single space),
# print it with the first letter of each word capitalized using the your own function capitalize().

# In Python there is a function ord(character), which returns character code in the ASCII chart, and the function chr(code),
# which returns the character itself from the ASCII code. For example, ord('a') == 97, chr(97) == 'a'.

def capitilizer(a):
    for i in range(len(a)):
        if i==0 or a[i-1]==" ":
            a[i]=chr(ord(a[i])-32)
    return "".join(a)
a=[i for i in input()]
print(capitilizer(a))

