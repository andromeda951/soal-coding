matrik = [
    [7,3,8],
    [1,2,8],
    [6,7,8],
    [1,2,3]
]

print(matrik)
print(matrik[0])
print(matrik[3])
print(matrik[0][0])
print(matrik[3][1])
print()

for i in range(len(matrik)):
    col = len(matrik[0])
    for j in range(col):
        if j == col-1:
            print(matrik[i][j])
        else:
            print(matrik[i][j], end="_")
        


# Inisialisasi matrik dengan nol dan print
print()
matrik = []
for i in range(3):
    line = []
    for j in range(4):
        line.append(0)
    matrik.append(line)
    
print(matrik)
print()       


# Isi nilai matrik dari input user dan print
matrik = []
for i in range(3):
    line = []
    for j in range(4):
        x = int(input())
        line.append(x)
    matrik.append(line)
    
print(matrik)


# penjumlahan matrik
