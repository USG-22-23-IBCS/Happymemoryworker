import turtle

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
            
    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
    def square (self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def polygon (self, size = 100):
        for i in range(6):
            self.t.left(120)
            self.t.right(180)
            self.t.forward(size)
            
    def icecream(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
        for i in range(240):
            self.t.right(1)
            self.t.forward(1)

    def star (self, size = 100):
        for i in range(5):
            self.t.right(36)
            self.t.left(252)
            self.t.forward(size)
            
    def circle(self, size = 100):
        for i in range(360):
            self.t.left(1)
            self.t.forward(1)
            
    def icecream(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
        for i in range(240):
            self.t.right(1)
            self.t.forward(1)

    def dodecagon(self, size = 100):
        for i in range (12):
            self.t.left(30)
            self.t.forward(size)
         
            
def main():
    canvas = turtle.Screen()
    canvas.bgcolor("#419f6a")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(100)
    art = Artist(t)
    art.move(20, 300)
    
    art.triangle()

    art.move(150, 200)
    
    art.square()
    art.move(-100, 150)
    
    art.polygon(50)
    art.move(100, 10)

    art.star()
    art.move(30, -200)
    
    art.circle()
    art.move(-200, -300)
    art.t.circle(110)
    art.t.circle(120)
    art.t.circle(130)
    art.t.circle(140)
    art.circle(150)
    art.move(-10, -200)

    art.icecream()
    art.move(300, -5)
    
    art.dodecagon(50)
   


    

    


if __name__ == "__main__":
    main()

    
