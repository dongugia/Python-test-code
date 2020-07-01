class Car:

    def __init__(self,hangxe ,tenxe, mauxe):
        self.hangxe = hangxe
        self.tenxe = tenxe
        self.mauxe = mauxe
        
    def chayxe(self):
        print("{} dang chay tren duong".format(self.tenxe))

    def dungxe(self,mucdich):
        print("{} dang dung xe de {}".format(self.tenxe,mucdich))

class toyota(Car):

    def __init__(self, hangxe, tenxe, mauxe, nguyenlieu):        # tao object __init__ moi
        super().__init__(hangxe, tenxe, mauxe)                   # Goi thuoc tinh tu init cua lop Car va ke thua tu Car
        self.nguyenlieu = nguyenlieu
       
    def dungxe(self,mucdich):
        print("{} dang dung xe de {}".format(self.tenxe,mucdich))
        print("{} chay bang {}".format(self.tenxe,self.nguyenlieu))
    def nomay(self):
        print("{} mau {} dang no may".format(self.tenxe,self.mauxe))

toyota1 = toyota("Toyota","Toyota hilux","Do","Dien")
toyota2 = toyota("Toyota","Toyota yaris","Vang","Deisel")
toyota3 = toyota("Toyota","Toyota Vios","Xanh","Gas")

toyota1.dungxe("nap dien")
toyota2.chayxe()
toyota3.nomay()