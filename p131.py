x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

sum_result =  x1 + x2 + x3 + x4
Average_result = sum_result / 4
product_result = x1 * x2 * x3 * x4
max_result = max(x1, x2, x3, x4)
min_result = min(x1, x2, x3, x4)

txt = 'Sum : {:.6f} \nAverage : {:.6f} \nProduct : {:.6f} \nMAX : {:.6f} \nMIN : {:.6f} \n' 
print(txt.format(sum_result, Average_result, product_result, max_result, min_result))