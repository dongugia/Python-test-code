
value=[]
items = [x for x in input("Nhap Cac So Nhi Phan: ").split(',')]
for p in items:
    intp = int(p,3)
    if not intp%5:
     value.append(p)
print(','.join(value))