try:
    x = int(input("Nhap 1 so nam trong khoang tu 1 den 10: "))
    if x<1 or x>10:
        raise Exception
    print('Ban vua nhap 1 so hop le!')
except:
    print ('So ban vua nhap nam ngoai khoang 1-10!')