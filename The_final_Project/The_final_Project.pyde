Win = 0
add_library('sound')
Avaria = 0
Shlopa = 0
Catlife = 1
T = 1
textX=950
Cat = 0
Bufw=100
Bufh=100
speed = 0
timer = 1000
Heart1 = 0
Heart2 = 0
Heart3 = 0
XHeart1 = 0
XHeart2 = 0
XHeart3 = 0
Heartx1 = 900
Hearty1 = 0
Heartx2 = 800
Hearty2 = 0
Heartx3 = 700
Hearty3 = 0
XHeartx1 = 900
XHearty1 = 0
Catw = 100
Cath = 100
XHeartx2 = 800
XHearty2 = 0
XHeartx3 = 700
XHearty3 = 0
Bufx = 100
Catx = 0
Caty = 250
Bufy = 600
Konus1 = 0
Konus2 = 0
Konus3 = 0
Konusw = 100
Konush = 100
Carw = 150
Carh = 300
Carx = 175
Enemyx = 825
Konusx1 = 100
Konusy1 = 100
Buf = 0
Konusx2 = 300
Konusy2 = 400
Konusx3 = 250
Konusy3 = 600
Enemyy = 700
Cary= 700
Enemy = 0
Car = 0
road = 0
life = 3
CarKrug = 0
EnemyKrug = 0
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False
def setup():
    size(1000,1000)
    global road, Car, Win, Enemy, Konus1, Konus2, Konus3, Buf, Heart1, Heart2, Heart3, XHeart1, XHeart2, XHeart3, Cat, Avaria, Shlopa
    frameRate(100)
    Win = SoundFile(this,"Win.mp3")
    Shlopa = SoundFile(this,"Shlopa.mp3")
    Avaria  = SoundFile(this,"Avaria.mp3")
    road = loadImage("road.jpg")
    Car = loadImage("Car.png")
    Enemy = loadImage("Enemy.png")
    Konus1 = loadImage("Konus.png")
    Konus2 = loadImage("Konus.png")
    Konus3 = loadImage("Konus.png")
    Buf = loadImage("Buf.png")
    Heart1 = loadImage("Heart.png")
    Heart2 = loadImage("Heart.png")
    Heart3 = loadImage("Heart.png")
    XHeart1 = loadImage("Heart-HP.png")
    XHeart2 = loadImage("Heart-HP.png")
    XHeart3 = loadImage("Heart-HP.png")
    Cat = loadImage("Cat.png")
def draw():
    global life, Win, Avaria, Catlife, timer, textX, road, Car, Enemy, Cary, Enemyy, Carx, Enemyx, Konus, Konusx1, Konusy1, Konusx2, Konusy2, Konusx3, Konusy3, Konusw, Konush, Buf, Bufx, Bufy, Bufw, Bufh, Heart1, Heart2, Heart3, XHeart1, XHeart2, XHeart3, XHeartx1, XHearty1, XHeartx2, XHearty2, XHeartx3, XHearty3, Carw, Carh, Cat, Catx, Caty, T, Catw, Cath, CarKrug, EnemyKrug                       
    image(road,0,0,1000,1000)
    image(Konus1,Konusx1,Konusy1,Konusw,Konush)
    image(Konus2,Konusx2,Konusy2,Konusw,Konush)
    image(Konus3,Konusx3,Konusy3,Konusw,Konush)
    image(XHeart1,XHeartx1,XHearty1,100,100)
    image(XHeart2,XHeartx2,XHearty2,100,100)
    image(XHeart3,XHeartx3,XHearty3,100,100)
    image(Buf,Bufx,Bufy,Bufw,Bufh)
    image(Car,Carx,Cary,Carw,Carh)
    if life == 3:
        image(Heart1,Heartx1,Hearty1,100,100)
        image(Heart2,Heartx2,Hearty2,100,100)
        image(Heart3,Heartx3,Hearty3,100,100)
    if life == 2:
        image(XHeart1,XHeartx1,XHearty1,100,100)
        image(Heart2,Heartx2,Hearty2,100,100)
        image(Heart3,Heartx3,Hearty3,100,100)
    if life == 1:
        image(XHeart1,XHeartx1,XHearty1,100,100)
        image(XHeart2,XHeartx2,XHearty2,100,100)
        image(Heart3,Heartx3,Hearty3,100,100)
    if Catlife==1:
        image(Cat,Catx,Caty,Catw,Cath)
        if collideRectRect(Carx,Cary,Carw,Carh,Catx,Caty,Catw,Cath):
            life = life - 1
            Catlife = 0
            Shlopa.play()
    if Cary<0:
        Catlife = 1
    push()
    translate(Enemyx,Enemyy)
    rotate(radians(90))
    image(Enemy,0,0,300,200)
    pop()
    if keyPressed==True:
        if key=="w":
            # if Catlife==1:
            #     image(Cat,Catx,Caty,Catw,Cath)
            #     if collideRectRect(Carx,Cary,Carw,Carh,Catx,Caty,Catw,Cath):
            #         Catlife=0
            #         if life==3:
            #             XHeartx1 = 900
            #             XHearty1 = 0
            #             life = 2
            #         Catx = -100
            #         Caty = -100
            #         if life==2:
            #             XHeartx2 = 800
            #             XHearty2 = 0
            #             life = 1
            #         if life==1:
            #             XHeartx3 = 700
            #             XHearty3 = 0
            #             life = 0
            if collideRectRect(Carx,Cary,Carw,Carh,Bufx,Bufy,Bufw,Bufh):
                Cary = Cary - 5
                timer = timer - 1
            elif collideRectRect(Carx,Cary,Carw,Carh,Konusx1,Konusy1,Konusw,Konush):
                Cary = Cary - 2
                timer = timer - 1
            elif collideRectRect(Carx,Cary,Carw,Carh,Konusx2,Konusy2,Konusw,Konush):
                Cary = Cary - 2
                timer = timer - 1
            elif collideRectRect(Carx,Cary,Carw,Carh,Konusx3,Konusy3,Konusw,Konush):
                Cary = Cary - 2
                timer = timer - 1
            else:
                Cary = Cary - 4
            if timer == 0:
                Cary = Cary - 100
        if key=="a":
            Carx = Carx - 3
        if key=="d":
            Carx = Carx + 3
    if Carx<=0:
        Carx=Carx+3  
    if Carx>=350:
        Carx=Carx - 3
    Enemyy = Enemyy - 2
    Catx = Catx + T
    if Catx > 350:
        T = - T
    if Cary<0:
        T = 1
        Catlife=1
        Cary=700
        Konusx1 = random(0,150)
        Konusy1 = random(0,200)
        Konusx2 = random(200,350)
        Konusy2 = random(200,400)
        Konusx3 = random(400,450)
        Konusy3 = random(400,600)
        Bufx = random(0,250)
        Bufy = random(0,500)
        Catx = 0
        Caty = random(0,500)
        Catx = Catx - T
        CarKrug = CarKrug + 1
    if Enemyy<0:
        Enemyy=700
        EnemyKrug = EnemyKrug + 1
    if life == 0:
        clear()
        fill(255,0,0)
        textSize(50)
        text("Game Over",350,450)
        Avaria.play()
        noLoop()
    if CarKrug == 10:
        clear()
        fill(255,255,0)
        textSize(50)
        text("You Won",350,450)
        Win.play
        noLoop()
    if EnemyKrug == 10:
        clear()
        textX=900
        fill(255,0,0)
        textSize(50)
        text("Game Over",350,450)
        noLoop()
    textSize(75)
    fill(0,0,255)
    text(CarKrug,0,990)
    textSize(75)
    fill(0,0,255)
    text(EnemyKrug,textX,990)
        
        
    
        
        
    
        
    
    
    
    
    
    
