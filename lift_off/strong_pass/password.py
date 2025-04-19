import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")
    
    # Provide feedback
    for message in feedback:
        print(message)

def generate_strong_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Create a strong password
    characters = (
        string.ascii_lowercase + 
        string.ascii_uppercase + 
        string.digits + 
        "!@#$%^&*"
    )
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Meter!")
    
    # Get user input
    password = input("Enter your password: ")
    check_password_strength(password)

    # Ask if the user wants a strong password suggestion
    if input("Would you like a strong password suggestion? (yes/no): ").strip().lower() == 'yes':
        suggested_password = generate_strong_password()
        if suggested_password:
            print(f"Suggested Strong Password: {suggested_password}")