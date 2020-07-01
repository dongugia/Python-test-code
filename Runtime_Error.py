import math
n = int(input("Nhap so n > 0 : "))
sum = 0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(round(sum,3))