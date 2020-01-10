from vpython import *

v1, v2, m1 = 0, -5, 1
k = int(input(''))
m2 = 100**k



scene = canvas(width=400, height=400, center=vec(0.4,0.2,0), align = 'left', background=vec(0.5,0.5,0))
wall = box(pos=vec(-5, 0, 0), length=1, height=100, width=100)

box_1 = box(pos=vector(10,-45,0), width = 10, height = 10, length = 10, color=color.red)
box_2 = box(pos=vector(30,-40,0), width = 20, height = 20, length = 20, color=color.blue)
box_1.m = m1
box_2.m = m2
box_1.v = v1
box_2.v = v2

count = 0
dt = 0.0001
while True:
    rate(1000)
    box_1.pos.x += box_1.v*dt
    box_2.pos.x += box_2.v*dt
    if (count%2)==0:
        if abs(box_1.pos.x-box_2.pos.x)<=15:
            box_1.v, box_2.v = box_1.v*(box_1.m-box_2.m)/(box_1.m+box_2.m)+2*(box_2.v)*(box_2.m)/(box_1.m+box_2.m), 2*box_1.v*(box_1.m)/(box_1.m+box_2.m)+(box_2.v)*(box_2.m-box_1.m)/(box_1.m+box_2.m)
            count += 1
            print(count)
    else:
        if abs(wall.pos.x-box_1.pos.x)<=5.5:
            box_1.v = -box_1.v
            count+=1
            print(count)
