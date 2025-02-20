import re

def checkPasswordStrength(password):
    passwordIssues = []

    if len(password) < 8:
        passwordIssues.append("-Try making your password longer!")
    if not re.search(r'[A-Z]', password):
        passwordIssues.append("-Try including some capital letters!")
    if not re.search(r'[a-z]', password):
        passwordIssues.append("-Try including some lowercase letters!")
    if not re.search(r'[0-9]', password):
        passwordIssues.append("-Try including numbers!")
    if not re.search(r'[\W_]', password):
        passwordIssues.append("-Try including symbols!")

    if len(passwordIssues) > 3:
        return "Weak Password :(\n" + "\n".join(passwordIssues)

    if len(passwordIssues) <= 3 & len(passwordIssues) > 1:
        return "Ok Password :/\n" + "\n".join(passwordIssues)

    if len(passwordIssues) == 1:
        return "Good Password :|\n" + "\n".join(passwordIssues)

    if len(passwordIssues) == 0 and len(password) > 12 and len(password) <= 20:
        return "SUPER PASSWORD!!!"

    if len(passwordIssues) == 0 and len(password) > 20:
        return "INSANE PASSWORD!!!!!!!!!"

    return "Strong Password! :)"

password = input("Enter your password: ")
print(checkPasswordStrength(password))