n, m = list(map(int, input().split()))

prices = list()
for _ in range(n):
    price = list(map(int, input().split()))
    prices.append(price)

regions = list()
for _ in range(m):
    region = list(map(int, input().split()))
    regions.append(region)

def calculate(regions, prices):
    result = 0
    for item in regions:
        number = prices[item[0]-1][item[1]-1]
        result += number



    return result

print(calculate(regions, prices))