def remove_vowel(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for i in range(len(str)):
        if str[i] not in vowels:
            result = result + str[i]
    print("\nAfter removing Vowels: ", result)

str = "India gate"
print("\nOriginal string : ",str)
remove_vowel(str) 