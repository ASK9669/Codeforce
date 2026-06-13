#CSE Grapgics projct
#Mahlet Girma
#Tigist Mekonnen
#Yhoanes
#Naol
#Kibur
from cs1graphics import*
import time
can = Canvas(1000, 600)
can.setBackgroundColor("deepskyblue")

# layer section
boat=Layer()
tree1=Layer()
moon=Layer()
resort=Layer()

# drawing section
moon1 = Circle(25, Point(100, 50))
moon1.setFillColor("white")
moon1.setBorderWidth(0)
moon.add(moon1)

moon2 = Circle(25, Point(115, 40))
moon2.setFillColor("deepskyblue")
moon2.setBorderWidth(0)
moon.add(moon2)

grass=Rectangle(1500, 300)
grass.setFillColor("green")
grass.setDepth(60)
grass.moveTo(500, 600)
can.add(grass)

mountain = Polygon(Point(0,300), Point(0, 150), Point(80,100), Point(100, 100), Point(100, 150), Point(300, 300), Point( 100,300), Point(400, 150), Point(500, 250), Point(550, 150), Point(600, 150), Point(620, 150), Point(650, 200), Point(700, 50), Point(800, 250), Point(1000, 150),Point(1000, 300))
mountain.setFillColor("chocolate4")
mountain.setBorderWidth(0)
mountain.setDepth(60)
can.add(mountain)

mountainref = Polygon(Point(0,150), Point(0, 75), Point(80,50), Point(100, 50), Point(100, 75), Point(300, 150), Point( 100,150), Point(400, 75), Point(500, 125), Point(550, 75), Point(600, 75), Point(620, 75), Point(650, 100), Point(700, 25), Point(800, 125), Point(1000, 75),Point(1000, 150))
mountainref.flip(90)
mountainref.setBorderWidth(0)
mountainref.move(0, 150)
mountainref.setFillColor("darkgrey")
mountainref.setDepth(54)
can.add(mountainref)

lake=Rectangle(1500, 150, Point(500,375))
lake.setFillColor("skyblue")
lake.setDepth(55)
can.add(lake)

base = Polygon(Point(150, 150), Point(200, 200), Point(300, 200), Point(350, 150))
base.setFillColor("yellow")
base.setDepth(0)
boat.add(base)

flagpole= Path(Point(300, 175), Point(300, 75))
flagpole.setBorderWidth(5)
flagpole.setBorderColor("red")
boat.add(flagpole)

flag = Polygon(Point(300, 150), Point(300, 80), Point(200,80))
flag.setFillColor("blue")
flag.setDepth(51)
boat.add(flag)

baseref = Polygon(Point(150, 75), Point(200, 100), Point(300, 100), Point(350, 75))
baseref.setFillColor("darkgrey")
baseref.setBorderWidth(0)
baseref.flip(90)
baseref.move(0, 150)
boat.add(baseref)

flagpoleref = Path(Point(300, 175), Point(300, 75))
flagpoleref.setBorderColor("darkgrey")
flagpoleref.setBorderWidth(5)
flagpoleref.move(0, -25)
flagpoleref.flip(90)
boat.add(flagpoleref)
boat.scale(0.5)

resortroof=Polygon(Point(525,3),Point(500,33),Point(660,33),Point(680,13),Point(810,13),Point(790,33),Point(950,33),Point(975,3))
resortroof.setFillColor("chocolate")
resortroof.setDepth(10)
resort.add(resortroof)

resortfrontwall1=Rectangle(160,80,Point(580,73))
resortfrontwall1.setFillColor("cyan")
resortfrontwall1.setDepth(10)
resort.add(resortfrontwall1)

resortfrontwall2=Rectangle(135,80,Point(740,53))
resortfrontwall2.setFillColor("cyan")
resortfrontwall2.setDepth(11)
resort.add(resortfrontwall2)

resortfrontwall3=Rectangle(160,80,Point(870,73))
resortfrontwall3.setFillColor("cyan")
resortfrontwall3.setDepth(10)
resort.add(resortfrontwall3)

resortside1=Polygon(Point(660,33),Point(680,13),Point(680,93),Point(660,113))
resortside1.setFillColor("brown")
resortside1.setDepth(10)
resort.add(resortside1)

resortside2=Polygon(Point(950,33),Point(975,3),Point(975,83),Point(950,113))
resortside2.setFillColor("brown")
resortside2.setDepth(10)
resort.add(resortside2)

resortwindow1=Rectangle(25,30,Point(520,55))
resortwindow1.setFillColor("white")
resortwindow1.setDepth(10)
resort.add(resortwindow1)

resortwindow2=Rectangle(25,30,Point(550,55))
resortwindow2.setFillColor("white")
resortwindow2.setDepth(10)
resort.add(resortwindow2)

resortwindow3=Rectangle(25,30,Point(580,55))
resortwindow3.setFillColor("white")
resortwindow3.setDepth(10)

resortwindow4=Rectangle(25,30,Point(610,55))
resortwindow4.setFillColor("white")
resortwindow4.setDepth(10)
resort.add(resortwindow4)

resortwindow5=Rectangle(25,30,Point(640,55))
resortwindow5.setFillColor("white")
resortwindow5.setDepth(10)
resort.add(resortwindow5)

resortwindow6=Rectangle(25,30,Point(520,95))
resortwindow6.setFillColor("white")
resortwindow6.setDepth(10)
resort.add(resortwindow6)

resortwindow7=Rectangle(25,30,Point(550,95))
resortwindow7.setFillColor("white")
resortwindow7.setDepth(10)
resort.add(resortwindow7)

resortwindow8=Rectangle(25,30,Point(580,95))
resortwindow8.setFillColor("white")
resortwindow8.setDepth(10)

resortwindow9=Rectangle(25,30,Point(610,95))
resortwindow9.setFillColor("white")
resortwindow9.setDepth(10)
resort.add(resortwindow9)

resortwindow10=Rectangle(25,30,Point(640,95))
resortwindow10.setFillColor("white")
resortwindow10.setDepth(10)
resort.add(resortwindow10)

resortwindow11=Rectangle(25,30,Point(810,55))
resortwindow11.setFillColor("white")
resortwindow11.setDepth(9)
resort.add(resortwindow11)

resortwindow12=Rectangle(25,30,Point(840,55))
resortwindow12.setFillColor("white")
resortwindow12.setDepth(9)
resort.add(resortwindow12)

resortwindow13=Rectangle(25,30,Point(870,55))
resortwindow13.setFillColor("white")
resortwindow13.setDepth(9)

resortwindow14=Rectangle(25,30,Point(900,55))
resortwindow14.setFillColor("white")
resortwindow14.setDepth(9)
resort.add(resortwindow14)

resortwindow15=Rectangle(25,30,Point(930,55))
resortwindow15.setFillColor("white")
resortwindow15.setDepth(9)
resort.add(resortwindow15)

resortwindow16=Rectangle(25,30,Point(810,95))
resortwindow16.setFillColor("white")
resortwindow16.setDepth(9)
resort.add(resortwindow16)

resortwindow17=Rectangle(25,30,Point(840,95))
resortwindow17.setFillColor("white")
resortwindow17.setDepth(9)
resort.add(resortwindow17)

resortwindow18=Rectangle(25,30,Point(870,95))
resortwindow18.setFillColor("white")
resortwindow18.setDepth(9)

resortwindow19=Rectangle(25,30,Point(900,95))
resortwindow19.setFillColor("white")
resortwindow19.setDepth(9)
resort.add(resortwindow19)

resortwindow20=Rectangle(25,30,Point(930,95))
resortwindow20.setFillColor("white")
resortwindow20.setDepth(9)
resort.add(resortwindow20)

board=Rectangle(380,30,Point(740,-5))
board.setFillColor("darkgoldenrod")
board.setDepth(10)
resort.add(board)
resortfrontdoor1=Polygon(Point(740,32),Point(770,32),Point(780,40),Point(780,90),Point(740,90))
resortfrontdoor1.setFillColor("white")
resortfrontdoor1.setDepth(10)
resort.add(resortfrontdoor1)

resortfrontdoor2=Polygon(Point(700,40),Point(710,32),Point(740,32),Point(740,90),Point(700,90))
resortfrontdoor2.setFillColor("white")
resortfrontdoor2.setDepth(10)
resort.add(resortfrontdoor2)

resort1= resort.clone()
resort1.move(0, -80)
resort1.setDepth(10)
resort.add(resort1)

road = Polygon(Point(680, 95), Point(790, 95), Point(750, 300), Point(600, 300))
road.setFillColor("red")
road.move(25, 350)
can.add(road)
#birds
bird1=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird1.setBorderWidth(10)
bird1.setBorderColor("black")
bird1.setDepth(10)
bird1.moveTo(900, 50)
can.add(bird1)

bird2=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird2.setBorderWidth(10)
bird2.setBorderColor("black")
bird2.setDepth(10)
bird2.moveTo(950, 100)
can.add(bird2)

bird3=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird3.setBorderWidth(10)
bird3.setBorderColor("black")
bird3.setDepth(10)
bird3.moveTo(800, 50)
can.add(bird3)

bird4=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird4.setBorderWidth(10)
bird4.setBorderColor("black")
bird4.setDepth(10)
bird4.moveTo(850, 100)
can.add(bird4)

bird5=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird5.setBorderWidth(10)
bird5.setBorderColor("black")
bird5.setDepth(10)
bird5.moveTo(820, 90)
can.add(bird5)

bird6=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird6.setBorderWidth(10)
bird6.setBorderColor("black")
bird6.setDepth(10)
bird6.moveTo(800, 95)
can.add(bird6)

leaf1=Polygon(Point(50, 80), Point(30, 140), Point(70, 140))
leaf1.setFillColor("green")
leaf1.setBorderColor("black")
leaf1.moveTo(700, 300)
leaf1.setDepth(10)
tree1.add(leaf1)
#tree
stem1=Rectangle(8,25, Point(700, 360))
stem1.setFillColor("darkred")
stem1.setDepth(11)
tree1.add(stem1)

tree2 = tree1.clone()
tree2.move(100, 200)
tree2.setDepth(9)

tree3 = tree1.clone()
tree3.move(-40, 150)
tree3.setDepth(9)

tree4 = tree2.clone()
tree4.move(-160,0)
tree4.setDepth(0)

woodroad = road.clone()
woodroad.setFillColor("brown")
woodroad.move(-500, -30)
woodroad.scale(0.2)

pool= Polygon(Point(50, 150), Point(100, 100), Point(300, 100), Point(250, 150))
pool.setFillColor("lightblue")
pool.setBorderWidth(0.1)
pool.setDepth(0)
pool.move(0, 400)
pool.scale(1.5)

poolbar1 = Spline(Point(120, 150), Point(120, 100), Point(75, 100), Point(75, 200))
poolbar1.setBorderColor("black")
poolbar1.setBorderWidth(5)
poolbar1.setDepth(-10)
poolbar1.move(280, 350)
poolbar1.scale(0.4)

poolbar2=poolbar1.clone()
poolbar2.move(-15,15)

boat1 = boat.clone()
boat1.move(100, 320)

# layer modification section
resort.setDepth(10)
boat.move(-100, 290)
tree1.setDepth(9)
tree1.move(120, 150)
resort.move(20,375)

#add section
can.add(moon)
can.add(boat)
can.add(boat1)
can.add(resort)
can.add(woodroad)
can.add(tree1)
can.add(tree2)
can.add(tree3)
can.add(tree4)
can.add(pool)
can.add(poolbar1)
can.add(poolbar2)

# animation section
for i in range (95):
    bird1.flip (90)
    bird2.flip(90)
    bird3.flip(90)
    bird4.flip(90)
    bird5.flip(90)
    bird6.flip(90)
    
    bird1.move(-20,0)
    bird2.move(-10,0)
    bird3.move(-20,0)
    bird4.move(-10,0)
    bird5.move(-10,0)
    bird6.move(-20,0)
    boat.move(7, 0)
    
    bird1.scale(0.95)
    bird2.scale(0.95)
    bird3.scale(0.95)
    bird4.scale(0.95)
    bird5.scale(0.95)
    bird6.scale(0.95)
    time.sleep (0.1)

while sign:
    sign.setFontColor("yellow")
    time.sleep(0.5)
    sign.setFontColor("blue")
    time.sleep(0.5)
    sign.setFontColor("red")
    time.sleep(0.5)
    sign.setFontColor("azure4")
    time.sleep(0.5)
    sign.setFontColor("green")
    time.sleep(0.5)
    sign.setFontColor("brown")
    time.sleep(0.5)
    sign.setFontColor("purple")
    time.sleep(0.5)
    sign.setFontColor("orange")
    time.sleep(0.5)
