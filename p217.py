def fruits(tuple_of_fruits):
    result = dict()
    for i in range(len(tuple_of_fruits)):
        check1 = tuple_of_fruits[i]['shape'] == 'sphere'
        check2 = tuple_of_fruits[i]['mass'] >= 300 and tuple_of_fruits[i]['mass'] <= 600
        check3 = tuple_of_fruits[i]['volume'] >= 100 and tuple_of_fruits[i]['volume'] <= 500
        
        if check1 and check2 and check3:
            if tuple_of_fruits[i]['name'] not in result.keys():
                result[tuple_of_fruits[i]['name']] = 1
            else:
                result[tuple_of_fruits[i]['name']] += 1
    
    return result
