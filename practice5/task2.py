name = "Anna"
surname = "Havula"
group = "IT-32"
y = 2009

def print_age(year, current_year=2026):
    print(f"Age: {current_year - year}")

def get_age(year, current_year=2026):

    if year > current_year or year < 0:
        return -1
    return current_year - year

def main():
    print(f"{name} {surname}, {group}")

    print_age(y)

    result = print_age(y)
    print(f"print_age returned: {result}")

    age = get_age(y)
    print(f"Age from get_age: {age}")

    print(f"Age in months: {age * 12}")
    print(f"Age in weeks: {age * 52}")

    print(f"Age in 2030: {get_age(y, current_year=2030)}")

    try:
        print(print_age(y) * 12)
    except TypeError as e:
        print(f"Error: {e}")

    print(f"Invalid year 3000 gives: {get_age(3000)}")

if __name__ == "__main__":
    main()