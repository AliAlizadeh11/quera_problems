import re
def validate_email(email):
    if re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        return True
    else:
        return False
def validate_phone(number):
    if re.match(r'^09[0-9]{9}$', number):
        return True
    elif re.match(r'^\+989[0-9]{9}$', number):
        return True
    elif re.match(r'^00980[0-9]{9}$', number):
        return True
    else:
        return False
