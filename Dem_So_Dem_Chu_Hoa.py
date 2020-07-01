
s = input("Nhap cau cua ban: ")
d={"UPPER CASE":0,"LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
     pass
print("CHU HOA: ",d["UPPER CASE"])
print("CHU THUONG: ",d["LOWER CASE"])