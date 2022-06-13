n , x, k = input().split()
n = int(n)
x = int(x) - 1
k = int(k)
channels = list()
for i in range(n):
    input_channels = input()
    channels.append(input_channels)

first_channel = channels[x]
result_channel = first_channel
for i in range(k):
    if result_channel == channels[-1]:
        result_channel = channels[0]
    else:
        result_channel = channels[channels.index(result_channel) + 1]

print(result_channel)