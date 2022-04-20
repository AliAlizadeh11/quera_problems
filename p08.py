from datetime import datetime

def day_calculator(date):
    """calculates the day of age"""
    
    date = datetime.strptime(input(), '%Y-%m-%d')
    sajjad_bdate = datetime.strptime("1999-01-14",'%Y-%m-%d')
    answer = (date - sajjad_bdate).days
    
    if answer < 0:
        print('Not yet born')
    else:
        return answer
day_calculator('2005-01-06')


