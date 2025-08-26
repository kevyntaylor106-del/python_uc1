matriz = [
    [1, 2, 3],
    [10, 15, 22],
    [18, 20, 11]
]

print("elemento(0,0,):" ,matriz[0][0])
print("elemento (2,1):" , matriz[2][1])

for linha in matriz:
    for elemento in linha:
        print(elemento, end='')
    print()
    

