score = int(input("Enter score (0-100): "))
missed = int(input("Enter number of missed classes: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        letter = "A"
    elif score >= 82:
        letter = "B"
    elif score >= 74:
        letter = "C"
    elif score >= 64:
        letter = "D"
    elif score >= 60:
        letter = "E"
    else:
        letter = "F"

    total_classes = 16
    missed_percent = missed / total_classes * 100

    not_admitted = missed_percent > 30

    if not_admitted:
        print(f"Warning: missed {missed} of {total_classes} classes ({missed_percent:.1f}%) — not admitted to exam")

    passed = (letter != "F") and not not_admitted

    status = "passed" if passed else "failed"
    print(f"Score: {score}, Grade: {letter}, Status: {status}")