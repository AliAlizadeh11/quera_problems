from datetime import datetime
def day_calculator(date_str):
    date_format = '%Y-%m-%d' 
    date = datetime.strptime(date_str, date_format)
    sajjad_bdate = datetime.strptime('1999-01-14', date_format)
    result = (date - sajjad_bdate).days 
    
    if result < 0:
        return 'Not yet born'
    else:
        return result
    
day_calculator('2005-01-06')
