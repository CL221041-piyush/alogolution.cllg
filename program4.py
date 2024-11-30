def isPalindrome(s: str) -> bool:
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    
    return filtered == filtered[::-1]

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome(s1))  
print(isPalindrome(s2))  
