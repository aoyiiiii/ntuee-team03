#GlowScript 2.9 VPython
from vpython import*
import numpy as np

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
theta = pi/32

wallB = box (pos=vector(2, -side+0.5, 0), size=vector(s3+70, thk, thk*2),  color = color.blue)
inclinebox = box(pos=vector(0,0,0),size = vector(s3+65,thk, thk*2), color = color.yellow)
inclinebox.rotate(angle = theta, axis = vector(0,0,1))

ball = sphere (color = color.green, radius = 0.5, make_trail=True, retain=200)
ball.mass = 1.0
ball.p = vector (-0.15, 0, 0)
ball.pos = vector(30,2,0)


side = side - thk*0.5 - ball.radius
wallnor=vec(sin(theta),-cos(theta),0)
flrnor=vec(0,1,0)
dt = 0.3
n=0
while True :
    rate(200)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    if n < 315:
        if tan(theta)*ball.pos.x <= ball.pos.y:
            ball.p = (-2*(dot(wallnor,ball.p)*wallnor)+ball.p)
            n += 1
            print(f'collision : {n}')
        if ball.pos.y <= -side:
            ball.p = (-2*(dot(flrnor,ball.p)*flrnor)+ball.p)
            n += 1
            print(f'collision : {n}')
        if ball.pos.x > 30:
            break
            
