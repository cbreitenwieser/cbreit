import turtle as t

def quadrado ():
    t.speed(10000)
    x = 0
    angle = 50
    while x<= 36:
        t.circle(100)
        t.left(angle)
        x+=1
        
def outro ():
    x = 0
    angle = 50
    while x<=36:
        t.circle(150)
        t.left(angle)
        angle = angle + 1
        x+=1
        
def outro1 ():
    x = 0
    angle = 50
    while x<=36:
        t.circle(175)
        t.left(angle)
        x+=1

quadrado()
outro()
outro1()
