class HCN(object):
    def __init__(self,l,w):
        self.dai = l
        self.rong = w
    def area(self):
        return self.dai*self.rong

m = float(input("nhap chieu dai: "))
n = float(input("nhap chieu rong: "))
S_HCN = HCN(m,n)
print(S_HCN.area())

