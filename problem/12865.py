n, k = map(int, input().split())

weight_value = [[0,0]]
data = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    weight_value.append(list(map(int, input().split())))

for i in range(n+1):
    for j in range(k+1):
        weight = weight_value[i][0]
        value = weight_value[i][1]
        
        if(j < weight):
            data[i][j] = data[i-1][j]
        else:
            data[i][j] = max(value + data[i-1][j-weight], data[i-1][j])

print(data[i][j])