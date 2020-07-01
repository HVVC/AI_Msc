from Vehicle import Vehicle
from Comida import Comida

    
def setup():
    global v, c, d, cont
    size(640, 360)
    vel = PVector(0,-2)
    v = Vehicle(width / 2, height / 2)
    x = random(width)
    y = random(height)
    c = Comida(x, y)
    cont = 0
    # d = Comida(x, y)           
    
    
def display(num):
    textSize(32)
    text(str(num), 10, 30)
    fill(0, 102, 153)
    
def draw():
    background(50)    
    eixo1 = PVector(c.x,c.y)
    v.update()
    v.display()
    
    c.display()
    v.arrive(eixo1)
    
    #verifica se ocorreu a colisão e caso tenha ocorrido gera uma nova comida e atualiza o contador
    if(round(c.x,0) == round(v.position[0],0) and round(c.x,0) == round(v.position[0],0)):
        c.newFood()   
        c.captured = c.captured + 1
        # print(c.captured)    se tu  remover este comentário vai ficar printando no console
    
    display(c.captured) #imprime na tela a quantidade de comida capiturada
    
    

    

    

   
    
    
