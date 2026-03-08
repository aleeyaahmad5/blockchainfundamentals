from sympy import isprime
import math

# A. Prime check
nums = [313, 317, 379, 887, 983, 992, 997]
print("Prime check:")
for n in nums:
    print(n, isprime(n))

# B–D. GCD
print("\nGCDs:")
print("GCD(8,12) =", math.gcd(8,12))
print("GCD(9,21) =", math.gcd(9,21))
print("GCD(9,11) =", math.gcd(9,11))

# E–F. Mod
print("\nMod results:")
print("51 mod 5 =", 51 % 5)
print("389 mod 77 =", 389 % 77)

# G–H. Coprime
print("\nCoprime examples:")
print("GCD(8,15) =", math.gcd(8,15))   # coprime example
print("Are 6 and 30 coprime? GCD =", math.gcd(6,30))

# Modular exponent + inverse
print("\nModular exponent & inverse:")
print("10^19 mod 33 =", pow(10, 19, 33))
print("5^11 mod 77 =", pow(5, 11, 77))
print("7^-1 mod 33 =", pow(7, -1, 33))
print("23^-1 mod 551 =", pow(23, -1, 551))