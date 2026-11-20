import string
import getpass


# Function to check password strength
def check_password(password):

    score = 0
    suggestions = []

    # 1. Check password length
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # 2. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # 3. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # 4. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include numbers (0-9).")

    # 5. Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters (!, @, #, $).")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 3:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return score, strength, suggestions


# Main program
def main():

    print("\n========================================")
    print("       PASSWORD STRENGTH CHECKER")
    print("========================================")

    password = getpass.getpass("\nEnter your test password: ")

    score, strength, suggestions = check_password(password)

    print("\n----------- PASSWORD REPORT -----------")

    print("Password Length :", len(password))
    print("Security Score  :", str(score) + "/5")
    print("Password Strength:", strength)

    print("\n----------- FEEDBACK ------------------")

    if strength == "STRONG":
        print("Excellent! Your password passed all checks.")
    else:
        print("Suggestions to improve your password:")

        for item in suggestions:
            print("*", item)

    print("\n========================================")
    print("       THANK YOU!")
    print("========================================")


# Execute the program
if __name__ == "__main__":
    main()
