h = input()
def calculate(h):
    decimal_number = int(h, base=16)
    d = hex(decimal_number+1)
    d = str(d)
    print(d[2:].upper())

calculate(h)