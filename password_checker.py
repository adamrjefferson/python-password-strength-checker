
# Python Password Strength Checker
# Version 4: Reusable functions and safer input handling
# Educational project - use fictional passwords only.

from getpass import getpass

COMMON_PASSWORDS = {
    "password",
    "password123",
    "password123!",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "welcome123",
    "iloveyou",
    "abc123"
}

PREDICTABLE_PATTERNS = [
    "123456",
    "qwerty",
    "abcdef",
    "password"
]


def analyze_password(password):
    """Analyze a fictional password using basic rules."""

    length_ok = len(password) >= 12
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    is_common = password.lower() in COMMON_PASSWORDS

    all_repeated = (
        len(password) > 0
        and len(set(password)) == 1
    )

    has_pattern = any(
        pattern in password.lower()
        for pattern in PREDICTABLE_PATTERNS
    )

    score = sum([
        length_ok,
        has_uppercase,
        has_lowercase,
        has_number,
        has_symbol
    ])

    feedback = []

    if not length_ok:
        feedback.append("Use at least 12 characters.")

    if not has_uppercase:
        feedback.append("No uppercase letters detected.")

    if not has_lowercase:
        feedback.append("No lowercase letters detected.")

    if not has_number:
        feedback.append("No numbers detected.")

    if not has_symbol:
        feedback.append("No symbols detected.")

    if is_common:
        feedback.append("Found in the common-password list.")

    if all_repeated:
        feedback.append("Repeated single character detected.")

    if has_pattern:
        feedback.append("Predictable pattern detected.")

    if is_common or all_repeated or has_pattern:
        result = "WEAK - Predictable password detected."
    elif not length_ok:
        result = "NEEDS IMPROVEMENT - Too short."
    elif score == 5:
        result = "Meets all five basic checks."
    else:
        result = "Review the recommendations."

    return {
        "length": len(password),
        "score": score,
        "result": result,
        "feedback": feedback
    }


def main():
    """Run the interactive password checker."""

    print("=== Python Password Strength Checker ===")
    print("For educational use with fictional passwords only.")
    print("Type 'quit' to exit.")

    while True:
        password = getpass("\nEnter a sample password: ")

        if password.lower() == "quit":
            print("Goodbye!")
            break

        analysis = analyze_password(password)

        print("\n--- Password Analysis ---")
        print("Length:", analysis["length"])
        print("Basic checks:", analysis["score"], "/ 5")
        print("Result:", analysis["result"])

        if analysis["feedback"]:
            print("\nRecommendations:")
            for message in analysis["feedback"]:
                print("-", message)
        else:
            print("No issues found by the basic checks.")


if __name__ == "__main__":
    main()
