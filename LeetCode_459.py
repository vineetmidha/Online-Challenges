def repeatedSubstringPattern(s):
    if len(s) <= 1: return False

    for length in range(1, len(s)//2+1):
        if len(s) % length == 0:
            substring = s[:length]
            if substring * (len(s) // length) == s:
                return True

    return False
        
