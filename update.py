class Toyota:

    def dungxe(self):
        print("Toyota dung xe de nap dien")

    def nomay(self):
        print("Toyota no may bang hop so tu dong")

class Porsche:

    def dungxe(self):
        print("Porsche dung xe de bom xang")

    def nomay(self):
        print("Porsche no may bang hop so co")

def kiemtra_dungxe(car):
    car.dungxe()
    car.nomay()

toyota = Toyota()
porsche = Porsche()

kiemtra_dungxe(toyota)
kiemtra_dungxe(porsche)
