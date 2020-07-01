list1 = [x for x in input("nhap chuoi cua ban vao day: ").split(' ')]
m_max = 0
for i in range(1,len(list1)):      
    if  len(list1[m_max]) <= len(list1[i]):
        m_max = i
print(list1[m_max])

