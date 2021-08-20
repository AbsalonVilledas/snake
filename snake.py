import turtle
import time 
import random


posponer = 0.1


#Configuracion de la ventana
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(600, 600)
wn.tracer()


#cabeza de serpiente


cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('white')



#comida


comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')


#Funciones


def arriba():
    cabeza.direction = 'up'


def abajo():
    cabeza.direction = 'down'


def izquierda():
    cabeza.direction = 'left'


def derecha():
    cabeza.direction = 'right'





def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)


    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)


    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)


    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#teclado


wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')




while True:
    wn.update()
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)


    mov()
    time.sleep(posponer)
