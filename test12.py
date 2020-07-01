class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,m):
        x = self.x + m.x
        y = self.y + m.y
        return Point(x,y)

    def __sub__(self,m):
        x = self.x - m.x
        y = self.y - m.y
        return Point(x,y)

    def __mul__(self,m):
        x = self.x * m.x
        y = self.y * m.y
        return Point(x,y)

    def __truediv__(self,m):
        x = self.x / m.x
        y = self.y / m.y
        return Point(x,y)

    def __floordiv__(self,m):
        x = self.x // m.x
        y = self.y // m.y
        return Point(x,y)

    def __pow__(self,m):
        x = self.x ** m.x
        y = self.y ** m.y
        return Point(x,y)

    def __lt__(self,m):
        self_mag = (self.x**2) + (self.y**2)
        m_mag = (m.x**2) + (m.y**2)
        return self_mag < m_mag

p1 = Point(2,4)
p2 = Point(5,9)
print("cong: ",p1+p2)
print("Tru: ",p1-p2)
print("Nhan: ",p1*p2)
print("Chia: ",p1/p2)
print("Luy Thua: ",p1**p2)
print("Chia lay phan nguyen: ",p2//p1)
