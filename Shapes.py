import pgzrun
import random
WIDTH=700
HEIGHT=450
def draw():
    screen.fill("Black")
    """
    rectangle = Rect((0,0),(300,250))
    rectangle.center=250,175
    screen.draw.rect(rectangle,"black")
    #screen.draw.filled_rect(rectangle,"black")
    rectangle = Rect((0,0),(200,150))
    rectangle.center=250,175
    screen.draw.rect(rectangle,"black")
    #screen.draw.filled_rect(rectangle,"black")"""
    W=600
    H=400
    r=random.randint(0,255)
    g=0
    b=255
    for i in range(20):
        rectangle = Rect((0,0),(W,H))
        rectangle.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rectangle,(r,g,b))
        W-=20
        H-=20
        b-=10
        g+=10
def update():
    pass
pgzrun.go()