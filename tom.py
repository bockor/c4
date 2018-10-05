#!/usr/bin/python3

##Author: Desmet Tom - desmet_t@hotmail.com - 02/10/2018

import random

#----------Function to find greatest common divisor----------#
def gcd(e, phi):
    while phi != 0:
        e, phi = phi, e % phi
    return e

#----------Function Mod Inverser-----------------------------#
def modinv(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None

#----------BEGINNING-----------------------------------------#
print("Simple RSA Encryption example:")
print("------------------------------------""\n")
p = int(input("Select prime p: "))
q = int(input("Select prime q: "))
n = p*q
print("")
print("Modulus: n = p*q = {} * {} = {}".format(p, q, n))
phi = (p-1)*(q-1)
print("phi = (p-1)*(q-1) = ({}-1)*({}-1) = {}".format(p, q, phi))
print("")
#/////////////////////////////////////////////////////////////////////////////////////////#
e = random.randrange(1,phi)
g = gcd(e, phi)
while g != 1:
    e = random.randrange(1, phi)
    g = gcd(e, phi)
print("Choose Public Key e: {}".format(e))
print("[*]{} and {} have no common factors except 1".format(e, phi))
print("")
#/////////////////////////////////////////////////////////////////////////////////////////#
d = modinv(e, phi)
print("Computed Private Key d: " + str(d))
print("[*]{}*{} mod {} = 1".format(e, d, phi))
print("")
#/////////////////////////////////////////////////////////////////////////////////////////#
m = int(input("Select Message m: "))
#/////////////////////////////////////////////////////////////////////////////////////////#
c = m ** e % n
print("Encrypted message c = m ** e % n = {}".format(c))
mm = c ** d % n
print("Decrypted message mm = c ** d % n = {}".format(mm))
