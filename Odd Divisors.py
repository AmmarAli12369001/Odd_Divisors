"""
Odd Divisors
You are given an interval of integers [A,B].
For each number in this interval compute its greatest odd divisor. Output the sum of these divisors.

Standard input
The first line contains an integer T representing the number of test cases that will follow.
Each test case consists of one line containing two integer values A and B.

Standard output
The output should contain the answer for each test case on a different line.
Each answer consists of a single integer value.
"""

num = int(input())


def sqr(n):
    return n * n


def myFunc(n):
    if n == 0:
        return 0
    # if number is odd
    if n % 2 == 1:
        return sqr(int((n + 1) / 2)) + myFunc(int(n / 2))
    else:
        return sqr(int(n / 2)) + myFunc(int(n / 2))


for x in range(num):
    digits = input().split()
    result = myFunc(int(digits[1])) - myFunc(int(digits[0]) - 1)
    print(f'{int(result)}')
