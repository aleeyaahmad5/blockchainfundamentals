# Which number is not prime -
from sympy import isprime 

nums = [313, 317, 379, 887, 983, 992, 997]

for n in nums:
    print(n, isprime(n))

# GCD calculations -

import math

print(math.gcd(8, 12))   # 4
print(math.gcd(9, 21))   # 3
print(math.gcd(9, 11))   # 1

# Modular arithmetic -

print(51 % 5)     # 1
print(389 % 77)   # 1

# Coprime checks -

import math

# Example of any coprime pair 
print(math.gcd(8, 15))   # 1 → coprime

# Check if 6 and 30 are coprime
print(math.gcd(6, 30))   # 6 → NOT coprime

# Modular exponent & modular inverse -

print(pow(10, 19, 33))

print(pow(5, 11, 77))

print(pow(7, -1, 33))

print(pow(23, -1, 551))
