data = []
data_to_print = []

count = int(sys.stdin.readline())
even = 0

while (count != 0):
    count -= 1
    data.append(int(sys.stdin.readline()))
    if (even == 0):
        data.sort()
        mid = data[int(len(data)/2)]
        even = 1
        data_to_print.append(mid)
    else:        
        even = 0
        data_to_print.append(mid)

for data in data_to_print:
    print(data)