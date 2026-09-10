name = "Anna"
surname = "Havula"

print(f"{name} {surname}")

full_name = name + surname
vowels = 0
consonants = 0

for ch in full_name:
    if ch.lower() in "aeiouy":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {vowels + consonants}")