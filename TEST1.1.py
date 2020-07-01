list1 = [x for x in input("nhap chuoi cua ban vao day: ")]
list3 = []
list4 = []
for i in list1:
    
    if i.isalpha() and list1[len(list1)-1]!=i :
        list3.append(i)
    elif list1[len(list1)-1].isalpha() == True:
        m = len(list3)
        list4.append(m)
    elif i.isalpha() == False:       
        m=len(list3)
        list3 = []
        list4.append(m)
print(list4)