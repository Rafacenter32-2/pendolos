import turtle
from time import sleep
import json

try:
    configraw = open("config.json").read()
except:
    open("config.json","w").write(
"""
{
"rotation":[4,0,3.5],
"size":0.9,
"speed":0.01,
"axecolor":"white",
"trail":"gray",
"background":"black"
}
"""
    )
    configraw ="""
{
"rotation":[4,0,3.5],
"size":0.9,
"speed":0.01,
"axecolor":"white",
"trail":"gray",
"background":"black"
}
        """
config = json.loads(configraw)
turtle.delay(0.1)
turtle.tracer(0)
turtle.bgcolor("black")

space = False
buffer = False
stop = False

screen = turtle.Screen()
pause = False
def onspace():
    global space
    global buffer
    if (not buffer):
        space = not space
        buffer = True
def onenter():
    global stop
    stop = True
def onspacerelease():
    global buffer
    buffer = False
screen.onkeypress(onspace, "space")
screen.onkeyrelease(onspacerelease, "space")
screen.listen()
screen.onkeypress(onenter, "Return")

puffy = turtle.Turtle()
puffball = turtle.Turtle()

axes = [90] + [0] * (len(config["rotation"]) -1)
axestemplate = [90] + [0] * (len(config["rotation"]) -1)
trail = []
puffy.speed(0)
puffy.hideturtle()
puffball.speed(0)
puffball.hideturtle()
puffball.penup()
puffy.color(config["axecolor"])
puffball.color(config["trail"])
puffy.pen(pensize=7)
puffball.pen(pensize=7)
time = 0

while not stop:
    if (space and not pause):
        if time > 5:
            for i in range(len(axes)):
                if axes[i] % 360 != axestemplate[i] % 360:
                    all_match = False
                    break
            if all_match == True:
                pause = True
        puffy.clear()
        puffy.goto(0,0)
        puffy.setheading(0)
        puffy.pendown()
        for x in axes:
            puffy.dot(10,"blue")
            puffy.left(x)
            puffy.forward(50 * config["size"])
        puffy.dot(10,"blue")
        puffy.penup()
        puffball.goto(puffy.pos())
        puffball.pendown()
        """
        axes[0] += (axemoves[0]*10)-5
        axes[1] += (axemoves[1]*10)-5
        axes[2] += (axemoves[2]*10)-5
        axes[3] += (axemoves[3]*10)-5
        #"""
        time += 1
        for i in range(len(config["rotation"])):
            axes[i] += config["rotation"][i]
        all_match = True
                
    elif not space:
        puffy.goto(0,0)
        puffy.write("precione espaço para continuar e enter para parar \n (ou vai dar erro)",font=("Arial",16,"normal"),align="center")
    turtle.update()
    sleep(config["speed"])
turtle.bye()