def is_anagram(s1,s2):
    for x in s1:
        if x not in s2:
            return False
        
    return True

print(is_anagram('Hello','elolH'))
print(is_anagram('Hello','elolh'))