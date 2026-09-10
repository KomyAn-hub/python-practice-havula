name = "Anna"
surname = "Havula"
group = "IT-32"
y = 2009

def print_card():
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {y}")


def print_card_args(name, surname, y, group=group):
    print(f"{name} {surname}, {group}, {y}")


def main():
    print(f"{name} {surname}, {group}")

    for i in (1, 2, 3):
        print(f"--- no parameters, call {i} ---")
        print_card()

    print("--- positional arguments ---")
    print_card_args("Anna", "Havula", 2009, "IT-32")

    print("--- keyword arguments ---")
    print_card_args(surname="Havula", group="IT-32", y=2009, name="Anna")

    print("--- mixed: first two positional, rest by name ---")
    print_card_args("Anna", "Havula", group="IT-32", y=2009)

    print("--- default group (group not passed) ---")
    print_card_args("Anna", "Havula", 2009)

    print("--- calling print_card_args('Anna') ---")
    try:
        print_card_args("Anna")
    except TypeError as e:
        print(f"Error: {e}")

    print("print_card_args(name='Anna', 'Havula') -> SyntaxError "
          "(positional argument follows keyword argument), "
          )

if __name__ == "__main__":
    main()