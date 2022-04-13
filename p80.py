def check_registration_rules(**kwargs):
    l1 = []
    for username, password in kwargs.items():
        check_invalid_username = username != 'quera' and username != 'codecup' 
        check_username =  len(username) >= 4 and check_invalid_username
        check_password = len(password) >= 6 and str.isdigit(password) == False
        if check_username and check_password:
            l1.append(username)
    return l1