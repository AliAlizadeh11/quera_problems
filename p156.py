sent = 'quera is the best platform.‍‍'
n = input()
n = int(n)
if n > 0 and n < 28:
    charachter = sent[n-1]
    ascii_val = ord(charachter)
    print(ascii_val)