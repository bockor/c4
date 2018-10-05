#!/usr/bin/python3
# syntax.py by Jane
# task: Produce a simple Python3 script.

import random


#the calculations


#calculate gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

#calculate private key (d)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def calc_all (p,q):
    #calculating the modulus
    n = p * q
    print("modulus n= p x q =", n)
    # calculating phi
    phi = (p-1) * (q-1)
    print("phi = (p-1) x (q-1) =", phi, "\n")

    # Selection public key
    e = int(input("Choose Public key e: "))
    # check the GCD
    import math

    print(math.gcd(e, phi))
    print("[*] ", e, "and ", phi, "have no common factors except 1\n")


    #compute the private key
    d = modinv(e, phi)
    print("Computed Private key d:", d)
    print("[*] ", e, "* ", d, "mod ", phi, "= 1\n")

    #test message m
    m = int(input("Select message m: "))

    #encrypt message
    c = m ** e % n
    print("Encrypted message c = m ** e % n = ", c)

    #decrypt message
    mm = c ** d % n
    print("decrypted message mm = c ** d % n = ", mm, "\n")

    print("is m == mm ? ... OK WORKING EXAMPLE")


if __name__ == "__main__":
    print("simple RSA encryption example")
    print("----------------------------- \n")

#asking for the primes
p = int(input("Select prime p: "))
q = int(input("Select prime p: "))
print("\n")

#use functions
calc_all(p,q)





