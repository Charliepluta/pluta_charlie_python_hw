import re

def is_valid_password(password):
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        return True
    return False

def check_passwords(passwords):
    valid_passwords = [p for p in passwords.split(",") if is_valid_password(p)]
    return ",".join(valid_passwords)

input_passwords = "ABd1234@1,a F1#,2w3E*,2We3345"
print(check_passwords(input_passwords))