# Problem statement in description

# HackerBlock problem: Leap Code : https://hack.codingblocks.com/app/dcb/1538

'''
Brute Force:
Run loop from 1 to n. Print 1 to n straightway.
For 10 till n, extract all digits one by one and check 
if the absolute difference between the two is one, print else reject.
'''

# Unable to think optimal solution

def isLeapCode(n):
    if n <= 9: return True
    
    prev = n % 10
    n //= 10

    while n != 0:
        current = n % 10
        if abs(current-prev)!=1:
            return False
        
        n //= 10
        prev = current

    return True

t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(n+1):
        if isLeapCode(i):
            print(i, end=" ")

    print()
    
'''
Input:
2
50
7720
Output:
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 101 121 123 210 212 232 234 321 323 343 345 432 434 454 456 543 545 565 567 654 656 676 678 765 767 787 789 876 878 898 987 989 1010 1012 1210 1212 1232 1234 2101 2121 2123 2321 2323 2343 2345 3210 3212 3232 3234 3432 3434 3454 3456 4321 4323 4343 4345 4543 4545 4565 4567 5432 5434 5454 5456 5654 5656 5676 5678 6543 6545 6565 6567 6765 6767 6787 6789 7654 7656 7676 7678 

'''
