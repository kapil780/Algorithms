# Given a string, count the number of consonants.
# Note a consonant is a letter that is not a vowel
# i.e. a letter that is not a,e,i,o,u.
input_str_1 = "abc_de"
input_str_2 = "LuCiDProGrAMiNG"
vowels = "aeiou"

def iterative_const_count(str_val):
    count = 0
    for i in str_val:
        if i.lower() not in vowels and i.isalpha():
            count += 1
    return count
def recursive_const_count(str_val):
    if str_val == "":
        return 0
    elif str_val[0].lower() not in vowels and str_val[0].isalpha():
        return 1 + recursive_const_count(str_val[1:])
    else:
        return recursive_const_count(str_val[1:]) 
print(iterative_const_count(input_str_1))
print(recursive_const_count(input_str_1))
