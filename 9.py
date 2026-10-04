#count vowels, consonants, digits and special characters in the string
def count(text):
    vowels = 0
    consonants = 0
    digits = 0
    special_char = 0
    
    vowel_set="aeiouAEIOU"
    
    for char in text:
        if char.isalpha():
            if char in vowel_set:
                vowels+=1
            else:
                consonants+=1
        elif char.isdigit():
            digits+=1
        else:
            special_char+=1

print(f"Vowels:{vowels}")
print(f"Consonants:{consonants}")
print(f"Digits:{digits}")
print(f"Special Characters:{special_char}")
