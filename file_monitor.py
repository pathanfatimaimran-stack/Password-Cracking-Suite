import hashlib

# Simple wordlist (dictionary attack)
wordlist = ["123456", "admin", "password", "qwerty", "fatima123"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

target_password = input("Enter password to test: ")
target_hash = hash_password(target_password)

print("Generated Hash:", target_hash)
print("Starting dictionary attack...")

found = False

for word in wordlist:
    if hash_password(word) == target_hash:
        print("⚠️ Weak Password Cracked:", word)
        found = True
        break

if not found:
    print("✅ Strong password (not found in dictionary)")
