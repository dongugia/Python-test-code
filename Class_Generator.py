def N7(n):
    i = 0
    while i<n:
        j=i
        i+=1
        if j%7==0:
            yield j

def N5(n):
    i = 0
    while i<n:
        j=i
        i+=1
        if j%5==0:
            yield j

n = int(input("nhap gia tri n: "))
A = []
for m in N7(n):
    for l in N5(n):
        if m == l:
            A.append(m)
print(A)