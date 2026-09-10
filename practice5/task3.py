name = "Anna"
surname = "Havula"
group = "IT-32"
c = 6

def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."

def count_letters(text: str, letter: str = "a") -> int:
    text_lower = text.lower()
    letter_lower = letter.lower()
    count = 0
    for ch in text_lower:
        if ch == letter_lower:
            count += 1
    return count

def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    text_lower = text.lower()
    count = 0
    for ch in text_lower:
        if ch in vowels:
            count += 1
    return count

def reverse_text(text: str) -> str:
    result = ""
    for ch in text:
        result = ch + result
    return result

def main():
    print(f"{name} {surname}, {group}")

    print(f"Initials: {get_initials(name, surname)}")

    length = len(surname)
    vowels = count_vowels(surname)
    consonants = length - vowels
    print(f"Letters in surname: {length}")
    print(f"Vowels: {vowels}, consonants: {consonants}")

    for v in "aeiou":
        print(f"{v}: {count_letters(surname, letter=v)}")

    print(f"Default letter 'a': {count_letters(surname)}")

    print(f"Reversed surname: {reverse_text(surname)}")

    print(f"Docstring: {count_letters.__doc__}")
    print(f"Annotations: {count_letters.__annotations__}")

if __name__ == "__main__":
    main()