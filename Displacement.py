https://www.hackerrank.com/contests/all-india-contest-by-mission-helix-a-11th-july/challenges/easy-2-cc/problem

def get_answer(t, x):
    return t * 60 * x // 2

tests = int(input())

for _ in range(tests):
    t, x = map(int, input().split())
    
    print(get_answer(t, x))
    
'''
Explanation: 

Total time in seconds T = t x 60

If speed is uniform all time, then time spend going east, T/2
[Maximum displacement]

Displacement = X * T/2 = X * t * 30
'''
