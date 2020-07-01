# The "Food" class

class Comida():

    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.raio = 1
        self.captured = 0
        
    def display(self):
        noStroke()
        stroke(255)
        ellipse(self.x,self.y,self.raio*2,self.raio*2)
        
    def newFood(self):
        self.x = random(width)
        self.y = random(height)
        
        
