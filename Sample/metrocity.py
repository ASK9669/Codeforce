##metropolitan city
##group members:
         
from cs1graphics import *
import time
canvas = Canvas(1200, 600)
canvas.setBackgroundColor("skyBlue")
green=Rectangle(1200,300,Point(600,450))
green.setFillColor("green")
canvas.add(green)
##road
road=Polygon(Point(0,550),Point(550,550),Point(500,300),Point(515,300),Point(900,550),Point(1200,550),Point(1200,600),Point(0,600),Point(0,550))
road.setFillColor("darkgrey")
canvas.add(road)

##railroad
rail=Path(Point(0,300),Point(1200,300))
rail.setBorderWidth(5)
canvas.add(rail)
##Sun
S=Circle(30,Point(50,50))
S.setFillColor("yellow")
S.setBorderColor("yellow")

canvas.add(S)
##train
t1=Polygon(Point(1100,300),Point(1100,290),Point(1150,270),Point(1400,270),Point(1400,300))
t1.setFillColor("yellow")
t1.setBorderWidth(3)

t5=t1.clone()
t5.moveTo(2300,300)
t5.flip=t2=Rectangle(300,30,Point(1550,285))
t2.setFillColor("yellow")
t2.setBorderWidth(3)

t3=t2.clone()
t3.moveTo(1850,285)

d1=Rectangle(280,10,Point(1550,280))
d1.setBorderWidth(6)
d2=d1.clone()
d2.moveTo(1250,280)
d3=d1.clone()
d3.moveTo(1850,280)
d4=d1.clone()
d4.moveTo(2150,280)

T=Layer()
T.add(t1)
T.add(t2)
T.add(t3)
T.add(t5)
T.add(d1)
T.add(d2)
T.add(d3)
T.add(d4)
T.setDepth(20)
canvas.add(T)

##building2
b2=Polygon(Point(700,380),Point(780,430),Point(780,280),Point(700,230))
b2.setFillColor("darkblue")
b2.setBorderWidth(4)
b2.setBorderColor("red")


r2=Polygon(Point(700,230),Point(780,230),Point(780,280))
r2.setFillColor("blue")
r2.setBorderWidth(2)
r2.setBorderColor("red")

B2=Layer()
B2.add(b2)
B2.add(r2)
B2.setDepth(-15)
canvas.add(B2)
##building3
b3=Polygon(Point(780,430),Point(860,480),Point(860,200),Point(780,150))
b3.setFillColor("black")
b3.setBorderWidth(4)
b3.setBorderColor("red")
b31=Polygon(Point(1000,400),Point(1000,200),Point(860,200),Point(860,400))
b31.setFillColor("pink")
b31.setBorderWidth(2)
b31.setBorderColor("red")

r3=Polygon(Point(1000,200),Point(920,150),Point(780,150),Point(860,200))
r3.setFillColor("pink")
r3.setBorderWidth(2)
r3.setBorderColor("red")

B3=Layer()
B3.add(b3)
B3.add(b31)
B3.add(r3)
B3.setDepth(-20)
canvas.add(B3)
##building4
b4=Polygon(Point(860,480),Point(940,530),Point(940,450),Point(860,400))
b4.setFillColor("grey")
b4.setBorderWidth(2)
b4.setBorderColor("black")

b41=Polygon(Point(940,530),Point(1200,530),Point(1100,450),Point(940,450))
b41.setFillColor("grey")
b41.setBorderWidth(2)
b41.setBorderColor("black")

r4=Polygon(Point(860,400),Point(1000,400),Point(1100,450),Point(940,450))
r4.setFillColor("black")
r4.setBorderWidth(2)
r4.setBorderColor("black")

parking=Polygon(Point(860,400), Point(1000,400), Point(940,450)) 
parking.setDepth(-15)
parking.setFillColor("yellow")



B4=Layer()
B4.add(b4)
B4.add(b41)
B4.add(r4)
B4.add(parking)
canvas.add(B4)

##banner
welcome=Text('WELCOME TO METRO-CITY')
welcome.move(400,500)
welcome.setDepth(-15)
canvas.add(welcome)

banner=Rectangle(250,30,Point(400,500))
banner.setFillColor("white")
stick=Rectangle(5,35,Point(400,525))
stick.setFillColor("black")
BANNER=Layer()
BANNER.add(banner)
BANNER.add(stick)
BANNER.setDepth(-10)
canvas.add(BANNER)
Banner=BANNER.clone()
Banner.moveTo(-20,100)
Banner.scale(0.5)
canvas.add(Banner)
welcome1=Text('MEGA SUPERMARKET',8,Point(180,350))
welcome1.setDepth(-15)
canvas.add(welcome1)

Banner1=BANNER.clone()
Banner1.moveTo(450,50)
Banner1.scale(0.6)
canvas.add(Banner1)
welcome2=Text('Jr.HOTEL',15,Point(655,350))
welcome2.setDepth(-15)
canvas.add(welcome2)

##windows

win=Polygon(Point(710,370), Point(710,330), Point(730,340), Point(730,380))
canvas.add(win)
win.setDepth(-25)
win.setFillColor("light blue")

win2=win.clone()
win2.moveTo(750,350)
canvas.add(win2)

win3=win.clone()
win3.moveTo(710,290)
canvas.add(win3)
##
win4=win.clone()
win4.moveTo(790,380)
canvas.add(win4)

win5=win.clone()
win5.moveTo(790,300)
canvas.add(win5)

win6=win.clone()
win6.moveTo(790,220)
canvas.add(win6)

win7=win.clone()
win7.moveTo(830,240)
canvas.add(win7)

win8=win.clone()
win8.moveTo(830,320)
canvas.add(win8)

win9=win.clone()
win9.moveTo(830,400)
canvas.add(win9)
##
win1=Polygon(Point(870,480), Point(920,510), Point(920,450), Point(870,420))
canvas.add(win1)
win1.setDepth(-25)
win1.setFillColor("lightblue")

winx=win1.clone()
winx.moveTo(900,250)
winx.setFillColor("black")
canvas.add(winx)
winx.rotate(30)

winx=win1.clone()
winx.moveTo(900,360)
winx.setFillColor("black")
canvas.add(winx)
winx.rotate(30)
winx.setDepth(-23)

winx=win1.clone()
winx.moveTo(900,320)
winx.setFillColor("lightblue")
canvas.add(winx)
winx.rotate(30)

x=Polygon(Point(850,420),Point(800,390),Point(760,390),Point(810,420))
x.setFillColor("darkgreen")
x.setDepth(-100)
canvas.add(x)
x1=Path(Point(810,420),Point(810,480))
x1.setBorderWidth(5)
x1.setBorderColor("darkgreen")
x1.setDepth(-40)
canvas.add(x1)
x2=x1.clone()
x2.moveTo(760,390)
canvas.add(x2)
##Hospital
h=Rectangle(300,150,Point(350,250))
h.setFillColor("white")
h.setBorderColor("white")
h1=Square(30,Point(250,200))
h1.setFillColor("black")
h2=h1.clone()
h2.moveTo(300,200)
h3=h1.clone()
h3.moveTo(350,200)
h4=h1.clone()
h4.moveTo(300,250)
h5=h1.clone()
h5.moveTo(350,250)
h6=h1.clone()
h6.moveTo(250,250)
h7=h1.clone()
h7.moveTo(250,300)
h8=h1.clone()
h8.moveTo(300,300)
h9=h1.clone()
h9.moveTo(350,300)
H=Layer()
H.add(h)
H.add(h1)
H.add(h2)
H.add(h3)
H.add(h4)
H.add(h5)
H.add(h6)
H.add(h7)
H.add(h8)
H.add(h9)
hh=Rectangle(100,30,Point(450,230))
hh.setFillColor("black")
hh.setBorderColor("black")
H.add(hh)
hd=Rectangle(50,70,Point(400,290))
hd.setFillColor("black")
hd.setBorderColor("black")
H.add(hd)
hs=hd.clone()
hs.moveTo(460,290)
H.add(hs)
H.setDepth(-30)
canvas.add(H)
hb=Rectangle(200,50,Point(350,150))
hb.setFillColor("pink")
hb.setBorderWidth(5)
H.add(hb)
hosp=Text("MC. GENERAL HOSPITAL",15,Point(350,150))
H.add(hosp)



##HELICOPTER

hel=Layer()
L=Polygon(Point(125,80),Point(50,90),Point(50,80),Point(40,80),Point(40,90),Point(20,90),Point(20,100),Point(125,120),Point(125,80))
L.setBorderColor("black")
L.setFillColor("red")
hel.add(L)

h11=Circle(40,Point(150,100))
h11.setFillColor("red")
h11.setBorderColor("red")
hel.add(h11)

h2=h11.clone()
h2.setFillColor("lightblue")
h2.moveTo(250,100)
hel.add(h2)

h23=Square(80,Point(200,100))
h23.setFillColor("red")
h23.setBorderColor("red")
hel.add(h23)

h4=Path(Point(160,130),Point(160,150),Point(140,150),Point(260,150),Point(240,130))
h4.setBorderWidth(5)
h4.setBorderColor("black")
hel.add(h4)

h5=Square(20,Point(200,50))
h5.setFillColor("black")
hel.add(h5)
hel.setDepth(-30)
canvas.add(hel)

##wing
w1=Path(Point(200,50),Point(125,50))
w1.setBorderColor("black")
w1.setBorderWidth(10)
w1.setDepth(-32)
canvas.add(w1)

w2=w1.clone()
w2.rotate(90)
w2.setDepth(-32)
canvas.add(w2)

w3=w1.clone()
w3.rotate(270)
w3.setDepth(-32)
canvas.add(w3)

w4=w1.clone()
w4.flip()
w4.setDepth(-32)
canvas.add(w4)

#######################garden /trees
tree=Polygon(Point(250,275),Point(210,375),Point(290,375))
tree.setFillColor("dark green")
bark=Rectangle(10,30,Point(250,390))
bark.setFillColor("darkgoldenrod")
Tree=Layer()
Tree.setDepth(-30)
Tree.add(tree)
Tree.add(bark)
canvas.add(Tree)

tree1=Tree.clone()
tree1.moveTo(-120,120)
canvas.add(tree1)

tree2=Tree.clone()
tree2.moveTo(100,150)
tree2.scale(0.8)
canvas.add(tree2)

tree3=Tree.clone()
tree3.moveTo(0,150)
tree3.scale(0.8)
canvas.add(tree3)

tree4=Tree.clone()
tree4.moveTo(900,100)
tree4.scale(0.8)
tree4.setDepth(20)
canvas.add(tree4)


tree5=Tree.clone()
tree5.moveTo(250,120)
tree5.scale(0.6)
canvas.add(tree5)

tree6=Tree.clone()
tree6.moveTo(50,100)
tree6.scale(0.6)
canvas.add(tree6)

tree7=Tree.clone()
tree7.moveTo(500,120)
tree7.scale(0.5)
canvas.add(tree7)

##traffic lights
r4=Rectangle(25,100,Point(900,500))
r4.setFillColor("brown")
r4.setDepth(-25)
canvas.add(r4)
r1=Circle(10,Point(900,450))
r1.setFillColor("grey")
r1.setDepth(-25)
canvas.add(r1)
r2=Circle(10,Point(900,470))
r2.setDepth(-25)
r2.setFillColor("grey")
canvas.add(r2)
r3=Circle(10,Point(900,490))
r3.setFillColor("grey")
r3.setDepth(-25)
canvas.add(r3)

##CAR
c1=Circle(30,Point(30,500))
c1.setFillColor("purple")
c2=Circle(30,Point(140,500))
c2.setFillColor("purple")
c3=Circle(50,Point(85,470))
c3.setFillColor("purple")
c5=Circle(40,Point(85,470))
c5.setFillColor("lightblue")
c4=Rectangle(110,60,Point(85,500))
c4.setFillColor("purple")

c6=Circle(15,Point(50,530))
c6.setFillColor("black")
c7=Circle(15,Point(120,530))
c7.setFillColor("black")


car=Layer()
car.add(c1)
car.add(c2)
car.add(c3)
car.add(c5)
car.add(c4)
car.add(c6)
car.add(c7)
car.setDepth(-50)
car.moveTo(0,50)
canvas.add(car)

##small people 
z=Circle(5, Point(10,270))
z.setDepth(-15)
z.setFillColor("yellow")
z1=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
z1.setDepth(-25)
z1.setFillColor("red")
z2=Rectangle(5,15,Point(7,300))
z2.setFillColor("white")
z2.setDepth(-20)
z3=z2.clone()
z3.moveTo(10,300)
Z=Layer()
Z.add(z)
Z.add(z1)
Z.add(z2)
Z.add(z3)
Z.moveTo(300,100)
canvas.add(Z)

a=Z.clone()
a.moveTo(420,200)
canvas.add(a)

c=Z.clone()
c.moveTo(420,100)
canvas.add(c)

v=Z.clone()
v.moveTo(970,140)
v.setDepth(-55)
canvas.add(v)

f=Z.clone()
f.moveTo(1150,50)
f.setDepth(-55)
canvas.add(f)


g=Circle(5, Point(10,270))
g.setDepth(-15)
g.setFillColor("brown")
g1=Polygon(Point(0,275),Point(20,275),Point(20,285),Point(15,285),Point(15,280),Point(15,295),Point(5,295),Point(5,280),Point(5,285),Point(0,285),Point(0,275))
g1.setDepth(-25)
g1.setFillColor("grey")
g2=Rectangle(5,15,Point(7,300))
g2.setFillColor("white")
g2.setDepth(-20)
g3=g2.clone()
g3.moveTo(10,300)
G=Layer()
G.add(g)
G.add(g1)
G.add(g2)
G.add(g3)
G.moveTo(100,50)
canvas.add(G)

l=G.clone()
l.moveTo(300,800)
l.setDepth(-55)
canvas.add(l)

u=G.clone()
u.moveTo(320,150)
canvas.add(u)

y=G.clone()
y.moveTo(770,140)
y.setDepth(-55)
canvas.add(y)

o=G.clone()
o.moveTo(1170,30)
o.setDepth(-55)
canvas.add(o)

##shade/house
sh=Polygon(Point(100,250),Point(50,400),Point(0,400),Point(50,250))
sh.setFillColor("purple")
sh.setDepth(-55)
canvas.add(sh)

sh1=Polygon(Point(0,400),Point(50,400),Point(50,540),Point(0,540))
sh1.setFillColor("white")
canvas.add(sh1)

sh2=Polygon(Point(100,250),Point(100,400),Point(50,400))
sh2.setFillColor("grey")
sh2.setDepth(-55)
canvas.add(sh2)

sh3=Polygon(Point(50,250),Point(50,150),Point(0,300),Point(0,400))
sh3.setFillColor("white")
sh3.setDepth(-55)
canvas.add(sh3)

sh4=Polygon(Point(50,150),Point(0,150),Point(0,300))
sh4.setFillColor("purple")
sh4.setDepth(-55)
canvas.add(sh4)

sh4=Polygon(Point(100,400),Point(50,400),Point(50,540))
sh4.setFillColor("black")
canvas.add(sh4)
##STOP........READY.....GOOOOOOOOO

for i in range(750):
    r1.setFillColor("red")
r1.setFillColor("grey")
for i in range(800):
    r2.setFillColor("yellow")
r2.setFillColor("grey")
for i in range(750):
    r3.setFillColor("green")
r3.setFillColor("grey")

####helicopter moves straight
for i in range(200):
     hel.move(4,0)
     w1.rotate(40)
     w1.move(4,0)
     w2.rotate(40)
     w2.move(4,0)
     w3.rotate(40)
     w3.move(4,0)
     w4.rotate(40)
     w4.move(4,0)
     f.move(0,0.4)
     o.move(0,0.4)
     a.move(0.4,0)
     l.move(0.4,0)
     G.move(0.2,0.4)
     Z.move(0,0.4)
     car.move(3,0)
##helicopter lands to pick up a person     
d=Rectangle(50,60,Point(1000,370))
d.setDepth(-40)
d.setFillColor("brown")
for i in range(200):
    f.move(0,-0.4)
    o.move(0,-0.4)
    c.move(-2,0)
    a.move(-4,0)
    l.move(4,0)
    G.move(-0.2,-0.4)
    Z.move(0,-0.4)
for i in range(135):
    hel.move(0,2)
    car.move(4.6,0)
    w1.rotate(12)
    w1.move(0,2)
    w2.rotate(12)
    w2.move(0,2)
    w3.rotate(12)
    w3.move(0,2)
    w4.rotate(12)
    w4.move(0,2)
    f.move(0,0.2)
    o.move(0,0.2)
    c.move(0.2,0)
    l.move(0.2,0)
    G.move(0.1,0.2)
    Z.move(0,0.2)
for i in range(10):
     v.move(1,-1)
canvas.add(d)

##train moves
for i in range(450):
    T.move(-6,0)
    f.move(0,0.15)
    o.move(0,0.2)
    G.move(0.6,0.4)
    a.move(0,1.7)
    c.move(0.5,0)
    Z.move(1,0)
    u.move(0.4,0.4)
##person gets on helicopter and man enters Jr.HOTEL  
canvas.remove(v)
canvas.remove(d)
canvas.remove(y)
##HELICOPTER TAKES THE PERSON AWAY
for i in range(450):
    T.move(6,0)
    hel.move(0,-2)
    w1.rotate(24)
    w1.move(0,-2)
    w2.rotate(24)
    w2.move(0,-2)
    w3.rotate(24)
    w3.move(0,-2)
    w4.rotate(24)
    w4.move(0,-2)
    f.move(0,-0.1)
    o.move(0,-0.2)
    G.move(-0.2,0.2)
    a.move(0,20)
    c.move(-0.5,0)
    Z.move(-0.6,0)
    u.move(0.2,-0.2)
canvas.remove(a)
##IT GETS DARK
canvas.setBackgroundColor("blue")
S.setFillColor("orange")
win.setFillColor("yellow")
win1.setFillColor("yellow")
win2.setFillColor("yellow")
win3.setFillColor("yellow")
win4.setFillColor("yellow")
win5.setFillColor("yellow")
win6.setFillColor("yellow")
win7.setFillColor("yellow")
win8.setFillColor("yellow")
win9.setFillColor("yellow")
h1.setFillColor("yellow")
h3.setFillColor("yellow")
h9.setFillColor("yellow")
h6.setFillColor("yellow")
h8.setFillColor("yellow")
hb.setFillColor("yellow")
##TRAIN MOVES AND PEOPLE RETURN HOME
for i in range(750):
    T.move(-4,0)
canvas.remove(f)
canvas.remove(o)
canvas.remove(Z)
for i in range(900):
    T.move(-3,0)
    hel.move(0,1)
    w1.rotate(12)
    w1.move(0,1)
    w2.rotate(12)
    w2.move(0,1)
    w3.rotate(12)
    w3.move(0,1)
    w4.rotate(12)
    w4.move(0,1)
canvas.add(d)
canvas.add(v)
for i in range(700):
     car.move(-3,0)
##midnight
canvas.setBackgroundColor("black")
canvas.remove(d)
for i in range(900):
    f.move(0,0.05)
    o.move(0,0.1)
    G.move(0.1,0.1)
    c.move(0.4,0)
    Z.move(0.3,0)
    u.move(-0.1,0.1)
    hel.move(0,-1)
    w1.rotate(12)
    w1.move(0,-1)
    w2.rotate(12)
    w2.move(0,-1)
    w3.rotate(12)
    w3.move(0,-1)
    w4.rotate(12)
    w4.move(0,-1)
    
##LATE PEOPLE GO HOME
canvas.remove(G)
canvas.remove(l)
canvas.remove(u)
canvas.remove(c)    
canvas.remove(v)
S.setFillColor("white")
##lights off
win.setFillColor("blue")
win1.setFillColor("blue")
win2.setFillColor("blue")
win3.setFillColor("blue")
win4.setFillColor("blue")
win5.setFillColor("blue")
win6.setFillColor("blue")
win7.setFillColor("blue")
win8.setFillColor("blue")
win9.setFillColor("yellow")
for i in range(150):
    S.move(1,0.5)
##SUNRISE
S.setFillColor("red")
for i in range(150):
    S.move(1,0.5)
canvas.setBackgroundColor("orange")
canvas.add(f)
canvas.add(o)
canvas.add(y)
canvas.add(a)
win.setFillColor("lightblue")
win1.setFillColor("lightblue")
win2.setFillColor("lightblue")
win3.setFillColor("lightblue")
win4.setFillColor("lightblue")
win5.setFillColor("lightblue")
win6.setFillColor("lightblue")
win7.setFillColor("lightblue")
win8.setFillColor("lightblue")
win9.setFillColor("lightblue")
for i in range(150):
    car.move(1,0)


##DAYTIME............GOOD MORNING
for i in range(300):
    S.move(-1,-0.5)
canvas.setBackgroundColor("lightblue")
S.setFillColor("yellow")
h1.setFillColor("lightblue")
h3.setFillColor("lightblue")
h9.setFillColor("lightblue")
h6.setFillColor("lightblue")
h8.setFillColor("lightblue")
hb.setFillColor("pink")
canvas.refresh()














































































































































































