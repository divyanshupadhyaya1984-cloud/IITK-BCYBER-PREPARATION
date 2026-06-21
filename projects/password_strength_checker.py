#PASSWORD_STRENGTH_CHECKER

import zxcvbn
import re
"""
Some criteria for a strong password are :-
1.Password should be at least 8 characters long.
2.Add at least one lowercase letter (a-z).
3.Add at least one uppercase letter (A-Z).
4.Add at least one number (0-9).
5.Add at least one special character (e.g., @, #, $, %).
"""

def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    remarks = []
    
    # 1. Check Length
    if len(password) >= 8: 
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")
        
    # 2. Check for Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter (a-z).")
        
    # 3. Check for Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter (A-Z).")
        
    # 4. Check for Digits
    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add at least one number (0-9).")
        
    # 5. Check for Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character (e.g., @, #, $, %).")
    
    # Evaluate Strength based on score
    strength_levels = {
        5: "Very Strong 🔥",
        4: "Strong 💪",
        3: "Medium ⚠️",
        2: "Weak ❌",
        1: "Very Weak 🚨",
        0: "Very Weak 🚨"
    }
    
    return {
        "strength": strength_levels[score],
        "score": score,
        "suggestions": remarks
    }

# Example usage:
if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    result = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")
    if result['suggestions']:
        print("Suggestions to improve:")
        for suggestion in result['suggestions']:
            print(f"- {suggestion}")

from zxcvbn import zxcvbn

def advanced_password_check(password):
    # zxcvbn handles dictionary attacks, common patterns, and leaks automatically
    results = zxcvbn(password)
    
    score = results['score'] # Scale from 0 (very guessable) to 4 (very secure)
    feedback = results['feedback']
    
    strength_labels = {
        0: "Too Weak (Instant Crack) ❌",
        1: "Weak ⚠️",
        2: "Fair 🧐",
        3: "Good 👍",
        4: "Excellent 🔥"
    }
    
    print(f"Strength Rating: {strength_labels[score]}")
    print(f"Estimated cracks needed: {results['crack_times_display']['online_no_throttling_10_per_second']}")
    
    # Provide tips if they exist
    if feedback['warning']:
        print(f"Warning: {feedback['warning']}")
    if feedback['suggestions']:
        print("Suggestions:")
        for hint in feedback['suggestions']:
            print(f"- {hint}")

advanced_password_check(user_password)    
