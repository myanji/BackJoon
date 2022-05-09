A = []
for i in range(5):
    a = int(input())
    if a <40:
        a = 40
    A.append(a)

B = A[0]+A[1]+A[2]+A[3]+A[4]
print(B//5)
