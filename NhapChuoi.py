
items= [x for x in input("Nhap mot chuoi: ").split(',')]
items.sort()  #Sap xep chuoi theo thu tu bang chu cai Anpha
print(','.join(items))