def read_grade(prompt: str) -> int:
    while True:
        raw = input(prompt)
        if not raw.lstrip("-").isdigit():
            print("Error: digits only")
            continue
        grade = int(raw)
        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue
        return grade


def to_letter(grade: float) -> str:
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    if grade >= 50:
        return "E"
    return "F"

def average(grades: list) -> float:
    return sum(grades) / len(grades)

def count_above(grades: list, limit: float) -> int:
    return sum(1 for g in grades if g > limit)

def print_report(name: str, group: str, grades: list) -> None:
    avg = average(grades)
    letter = to_letter(avg)
    above = count_above(grades, avg)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", " ".join(str(g) for g in grades))
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above}")

def main():
    name = "Anna Havula"
    group = "IT-32"
    n = 4

    print(f"{name}, {group}")

    grades = []
    for i in range(1, n + 1):
        grades.append(read_grade(f"Grade {i} (0-100): "))

    print_report(name, group, grades)

main()