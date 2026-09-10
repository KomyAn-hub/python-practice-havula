day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if month < 1 or month > 12:
    print(f"Date is invalid: month {month} does not exist")
elif year <= 0:
    print(f"Date is invalid: year {year} must be positive")
else:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:  # month == 2
        max_day = 29 if is_leap else 28

    if day < 1 or day > max_day:
        print(f"Date is invalid: month {month} has only {max_day} days")
    else:
        print("Date is valid")