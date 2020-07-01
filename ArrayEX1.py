
input_srt= input("Nhap X,Y: ")
dimensions= [int(x) for x in input_srt.split(",")]    # Kich Thuoc
rowNum= dimensions[0]
colNum= dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]   # Danh Sach Hien Thi
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = col*row
print(multilist)


  