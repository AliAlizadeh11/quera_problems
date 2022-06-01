def solve(path):
    f = open(path, "r")
    lines = []
    while True:
        line = f.readline()
        line.strip()
        if line == '':
            break # end of file
        lines.append(line)
    lines.reverse()
    for line in lines:
        print(line, end = '')

path = input()
solve(path)