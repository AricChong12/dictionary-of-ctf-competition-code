
from math import gcd
from Crypto.Util.number import long_to_bytes

# ==================================
# RSA VAULT A
# ==================================
nA = 1942668892225729070919461906823520455305416829490420089422957436437580309796491507761
  # Vault A modulus
eA = 65537
cA = 1574928985319013777436289945491687612751672976588545303342361399014858100334313795739
  # Vault A ciphertext

# ==================================
# RSA VAULT B
# ==================================
nB = 1942668892225729070919461906823519371241578281403951004079222153957205455266330293941
  # Vault B modulus

# ==================================
# STEP 1: Find shared prime
# ==================================
p = gcd(nA, nB)

if p == 1:
    print("[-] No shared prime found.")
    exit()

if p == nA:
    print("[-] Vault A modulus is fully shared.")
    exit()

print("[+] Shared prime found:", p)

# ==================================
# STEP 2: Factor Vault A
# ==================================
qA = nA // p

print("[+] Prime p:", p)
print("[+] Prime qA:", qA)

# ==================================
# STEP 3: Calculate Euler's totient
# ==================================
phiA = (p - 1) * (qA - 1)

# ==================================
# STEP 4: Recover private exponent
# ==================================
dA = pow(eA, -1, phiA)

print("[+] Private exponent recovered:", dA)

# ==================================
# STEP 5: Decrypt ciphertext
# ==================================
m = pow(cA, dA, nA)

plaintext = long_to_bytes(m)

print("[+] Decrypted message:")
print(plaintext)
print("[+] Hex:", plaintext.hex())
