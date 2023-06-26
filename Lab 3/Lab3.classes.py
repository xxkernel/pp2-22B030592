from math import*
"""class Upper:
    def __init__(self):
        self.text = " "
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())
    
write = Upper()
write.getString()
write.printString()"""




"""class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length*self.length
    
area_square = Square(10)
print(area_square.area())"""




"""class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length*self.width

area_of_rectangle = Rectangle(10,10)
print(area_of_rectangle.area())"""





"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self,x,y):
        self.x = self.x+x
        self.y = self.y+y
    
    def dist(self,sum):
        dx = sum.x - self.x
        dy = sum.y - self.y
        return sqrt(dx**2 + dy**2)

coord_1 = Point(1,2)
coord_2 = Point(1,1)
print(coord_1.show())
print(coord_2.show())
coord_1.move(10,2)
print(coord_1.show())
print(coord_1.dist(coord_2))"""




"""class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_add):
        self.balance +=dep_add
        print("Deposit Accepted!")
    def withdraw(self,add):
        if self.balance >= add:
            self.balance -=add
            print("Withdrawal accepted!")
        else:
            print("Withdrawal cancelled!")
    
person_1 = Account("Temerlan", 0)
person_1.deposit(50)
person_1.withdraw(500)"""




def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter(arr):
    new = []
    for i in arr:
        if isPrime(i):
            new.append(i) 
    return new

arr = [1,2,3,4,5]
print(filter(arr))