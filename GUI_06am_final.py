# mode-demo.py

from tkinter import *
import random

####################################
# other functions
####################################

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

import random
from tkinter import *
import urllib.request
import re
import string
 
class rainState(object):
 
    def __init__(self, name, x,y,width,height,rainpercent,cap,color):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.cap = cap
        self.rainpercent = rainpercent
        self.drawpercent = 0
        self.color = color
 
    def reanimate(self,data):
        self.drawpercent = 0
 
    def draw(self, canvas,data):
        if data.climate:
            canvas.create_rectangle(self.x-self.width/2, self.y-self.height/2,
                           self.x+self.width/2, self.y+self.height/2,
                           outline="grey",fill=self.color)
        else:
            canvas.create_rectangle(self.x-self.width/2, self.y-self.height/2,
                                self.x+self.width/2, self.y+self.height/2,
                                outline="grey",fill="white")
        canvas.create_rectangle(self.x-self.width/2,self.y+self.height/2-self.height*self.drawpercent/100,
                           self.x+self.width/2, self.y+self.height/2,
                           outline="grey",fill="lightblue")
        canvas.create_text(self.x, self.y, text=self.cap+ "\n"+str(self.rainpercent),font="Helvetica "+
                                    str(min(13,int(min(self.width,self.height)//3))))
 
    def onTimerFired(self, data):
        if self.drawpercent < self.rainpercent :
            self.drawpercent += 5
 
 
def getData():
    
    states = [("Washington",10),("Montana",20),("Oregon",30),("Idaho",10),
            ("Wyoming",10),("Nevada",20),("Utah",80),("California",60),("Colorado",30),
            ("Arizona",70),("New Mexico",90),("Texas",40),("Oklahoma",30),("Kansas",10),
            ("Nebraska",20),("South Dakota",10),("North Dakota",20),("Minnesota",20),
            ("Iowa",30),("Missouri",10),("Arkansas",30),("Mississippi",10),("Wisconsin",20),
            ("Illinois",20),("Tennessee", 60),("Alabama",20),("Georgia",20),("Kentucky",40),
            ("Ohio",10),("West Virginia",40),("Virginia",20),("North Carolina", 20),("Indiana",60),
            ("South Carolina", 30),("Florida",80),("Pennsylvania",40),("Maryland",40),
            ("New York", 40), ("Connecticut",40),("Massachusetts",50),("New Hampshire",30),
            ("Maine", 30),("Rhode Island",30),("New Jersey",20),("Delaware",30),("Vermont",50),
            ("Louisiana",60),("Michigan",30),("Hawaii",10),("Alaska",10)]
    
    #states = statePrecip()
    print(len(states))
    return states
 
 
def statePrecip():
    symbolslist = ['Illinois','Indiana','Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
                   'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 
                   'Idaho','Iowa','Kansas', 'Kentucky', 'Louisiana', 
                   'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
                   'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 
                   'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                   'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 
                   'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 
                   'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    i = 0
    precip = []
    cancaString = ''
    while i < len(symbolslist):
        url = 'http://www.usclimatedata.com/climate/'+symbolslist[i].lower()+'/united-states/'
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        stateClimate = '"Climate ' + symbolslist[i]+ '"'
        regex = b'<td>Average annual precipitation - rainfall:</td><td>(.+?) inch</td>'
        pattern = re.compile(regex)
        state = re.findall(pattern,htmltext)
        for num in state[0].decode("utf-8"):
            cancaString += num
        precip.append(float(cancaString))
        cancaString = ''
        i+= 1
    return list(zip(symbolslist,precip))

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.climate = False
    data.mode = "splashScreen"
    data.score = 0
    data.wrong = False
    data.question = ["Which state has a combination of more than two kinds\n of climates?","Which state does not have warm-summer mediterranean\n continental climate?","Which state has hot dessert climate?","What is the dominent climate in Alaska?"]
    data.choice=[["Maine","Georgia","Texas","Florida"],["Montana","North Dakota","Washington","Utah"],["Arizona","New Mexico","Colorado","Oklahoma"],["ice-cap","tundra","oceanic","subarctic"]]
    data.ansidx = [2,1,2,3]
    data.ans =["Texas","North Dakota","Arizona","subarctic"]
    data.i = 0
    data.show = False    
    data.states = []
    data.initdata = getData()
    data.swidth = 3/4* data.width
    data.wMargin = data.swidth * 1/8+data.width*1/4
    data.hMargin = data.height * 1/7
    widthRate = 12
    heightRate = 12
    inputL= [("Washington",data.wMargin+0*data.swidth/widthRate,data.hMargin+0*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"WA","green"),
             ("Montana",data.wMargin+1.5*data.swidth/widthRate,data.hMargin+0*data.height/heightRate,2*data.swidth/widthRate,data.height/heightRate,20,"MT","orange"),
             ("Oregon",data.wMargin+0*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,30,"OR","green"),
             ("Idaho",data.wMargin+1*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"ID","purple"),
             ("Utah",data.wMargin+1.5*data.swidth/widthRate,data.hMargin+2.5*data.height/heightRate,data.swidth/widthRate,2*data.height/heightRate,80,"UT","orange"),
             ("Wyoming",data.wMargin+2*data.swidth/widthRate,data.hMargin+1.25*data.height/heightRate,data.swidth/widthRate,1.5*data.height/heightRate,10,"WY","orange"),
             ("Nevada",data.wMargin+.5*data.swidth/widthRate,data.hMargin+2.5*data.height/heightRate,data.swidth/widthRate,2*data.height/heightRate,20,"NV","orange"),
             ("California",data.wMargin-.25*data.swidth/widthRate,data.hMargin+3*data.height/heightRate,data.swidth/(2*widthRate),data.height/(heightRate/3),60,"CA","yellow"),
             ("Arizona",data.wMargin+1.5*data.swidth/widthRate,data.hMargin+4.25*data.height/heightRate,data.swidth/widthRate,1.5*data.height/heightRate,70,"AZ","red"),
             ("New Mexico",data.wMargin+2.5*data.swidth/widthRate,data.hMargin+4.25*data.height/heightRate,data.swidth/widthRate,1.5*data.height/heightRate,90,"NM","orange"),
             ("Texas",data.wMargin+3.5*data.swidth/widthRate,data.hMargin+4.75*data.height/heightRate,data.swidth/widthRate,2*data.height/heightRate,40,"TX","lightGreen"),
             ("Louisiana",data.wMargin+4.5*data.swidth/widthRate,data.hMargin+5*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,60,"LA","lightGreen"),
             ("Oklahoma",data.wMargin+3.5*data.swidth/widthRate,data.hMargin+3.75*data.height/heightRate,data.swidth/widthRate,data.height/(2*heightRate),30,"OK","lightGreen"),
             ("Kansas",data.wMargin+3.5*data.swidth/widthRate,data.hMargin+3*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"KS","lightGreen"),
             ("Nebraska",data.wMargin+3*data.swidth/widthRate,data.hMargin+2*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,20,"NE","cyan"),
             ("Colorado",data.wMargin+2.5*data.swidth/widthRate,data.hMargin+2.75*data.height/heightRate,data.swidth/widthRate,1.5*data.height/heightRate,40,"CO","orange"),
             ("South Dakota",data.wMargin+3*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"SD","cyan"),
             ("North Dakota",data.wMargin+3*data.swidth/widthRate,data.hMargin+0*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,20,"ND","blue"),
             ("Minnesota",data.wMargin+4*data.swidth/widthRate,data.hMargin+0.5*data.height/heightRate,data.swidth/widthRate,2*data.height/heightRate,20,"MN","blue"),
             ("Iowa",data.wMargin+4*data.swidth/widthRate,data.hMargin+2*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,30,"IA","cyan"),
             ("Missouri",data.wMargin+4.5*data.swidth/widthRate,data.hMargin+3*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"MO","lightGreen"),
             ("Arkansas",data.wMargin+4.5*data.swidth/widthRate,data.hMargin+4*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,30,"AR","lightGreen"),
             ("Wisconsin",data.wMargin+5*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,data.swidth/widthRate,2*data.height/heightRate,20,"WI","blue"),
             ("Illinois",data.wMargin+5.25*data.swidth/widthRate,data.hMargin+3*data.height/heightRate,data.swidth/(2*widthRate),2*data.height/heightRate,20,"IL","cyan"),
             ("Indiana", data.wMargin+5.75*data.swidth/widthRate,data.hMargin+2.25*data.height/heightRate,data.swidth/(2*widthRate),2*data.height/heightRate,60,"IN","cyan"),
             ("Kentucky",data.wMargin+6*data.swidth/widthRate,data.hMargin+3.5*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,40,"KY","lightGreen"),
             ("Tennessee", data.wMargin+6*data.swidth/widthRate,data.hMargin+4*data.height/heightRate,data.swidth/widthRate,data.height/(2*heightRate),60,"TN","lightGreen"),
             ("Alabama",data.wMargin+5.75*data.swidth/widthRate,data.hMargin+5*data.height/heightRate,data.swidth/(2*widthRate),1.5*data.height/heightRate,20,"AL","lightGreen"),
             ("Mississippi",data.wMargin+5.25*data.swidth/widthRate,data.hMargin+4.75*data.height/heightRate,data.swidth/(2*widthRate),1.5*data.height/heightRate,10,"MS","lightGreen"),
             ("Michigan",data.wMargin+6*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"MI","blue"),
             ("Ohio",data.wMargin+6.5*data.swidth/widthRate,data.hMargin+2*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,10,"OH","cyan"),
             ("West Virginia",data.wMargin+6.5*data.swidth/widthRate,data.hMargin+2.75*data.height/heightRate,data.swidth/widthRate,data.height/(2*heightRate),40,"WV","lightGreen"),
             ("Virginia",data.wMargin+7*data.swidth/widthRate,data.hMargin+3.25*data.height/heightRate,data.swidth/widthRate,0.5*data.height/heightRate,20,"VA","lightGreen"),
             ("North Carolina", data.wMargin+7*data.swidth/widthRate,data.hMargin+3.75*data.height/heightRate,data.swidth/widthRate,data.height/(2*heightRate),20,"NC","lightGreen"),
             ("South Carolina", data.wMargin+7*data.swidth/widthRate,data.hMargin+4.25*data.height/heightRate,data.swidth/widthRate,data.height/(2*heightRate),30,"SC","lightGreen"),
             ("Georgia",data.wMargin+6.25*data.swidth/widthRate,data.hMargin+5*data.height/heightRate,.5*data.swidth/widthRate,1.5*data.height/heightRate,20,"GA","lightGreen"),
             ("Florida",data.wMargin+6.5*data.swidth/widthRate,data.hMargin+6.75*data.height/heightRate,.5*data.swidth/widthRate,2*data.height/heightRate,80,"FL","lightGreen"),
             ("New York", data.wMargin+7.75*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,1.5*data.swidth/widthRate,data.height/heightRate,40,"NY","blue"),
             ("Pennsylvania",data.wMargin+7.5*data.swidth/widthRate,data.hMargin+2*data.height/heightRate,data.swidth/widthRate,data.height/heightRate,40,"PA","blue"),
             ("Maryland",data.wMargin+7.25*data.width/widthRate,data.hMargin+2.75*data.height/heightRate,.5*data.width/widthRate,1*data.height/(2*heightRate),40,"MD","lightGreen"),
             ("Delaware",data.wMargin+7.75*data.swidth/widthRate,data.hMargin+2.75*data.height/heightRate,.5*data.swidth/widthRate,1*data.height/(2*heightRate),30,"DL","lightGreen"),
             ("New Jersey",data.wMargin+8.25*data.swidth/widthRate,data.hMargin+2*data.height/heightRate,.5*data.swidth/widthRate,data.height/heightRate,20,"NJ","lightGreen"),
             ("Vermont",data.wMargin+8.625*data.swidth/widthRate,data.hMargin+1*data.height/heightRate,.25*data.swidth/widthRate,data.height/heightRate,50,"VT","blue"),
             ("New Hampshire",data.wMargin+8.875*data.swidth/widthRate,data.hMargin+data.height/heightRate,data.swidth/(4*widthRate),data.height/heightRate, 30,"NH","blue"),
             ("Massachusetts",data.wMargin+8.75*data.swidth/widthRate,data.hMargin+1.75*data.height/heightRate,.5*data.swidth/widthRate,data.height/(2*heightRate),50,"MT","blue"),
             ("Maine", data.wMargin+9.5*data.swidth/widthRate,data.hMargin+data.height/heightRate,data.swidth/widthRate,data.height/heightRate,30,"ME","blue"),
             ("Connecticut",data.wMargin+8.625*data.swidth/widthRate,data.hMargin+2.25*data.height/heightRate,data.swidth/(4*widthRate),data.height/(2*heightRate),40,"CT","blue"),
             ("Rhode Island",data.wMargin+8.875*data.swidth/widthRate,data.hMargin+2.25*data.height/heightRate,data.swidth/(4*widthRate),data.height/(2*heightRate),30,"RI","blue"),
             ("Alaska",data.wMargin+0*data.swidth/widthRate,data.hMargin+6*data.height/heightRate,data.swidth/(4*widthRate),data.height/(2*heightRate),30,"AK","gray"),
             ("Hawaii",data.wMargin+0*data.swidth/widthRate,data.hMargin+7*data.height/heightRate,data.swidth/(4*widthRate),data.height/(2*heightRate),30,"HI","magenta")
             ]
    data.nameList = []
    data.xList = []
    data.yList = []
    data. widthList = []
    data. heightList = []
    data. rainList =[]
    data.capList =[]
    data.colorList = []
    for (name,x,y,width,height,rain,cap,color) in inputL:
        data.nameList.append(name)
        data.xList.append(x)
        data.yList.append(y)
        data.widthList.append(width)
        data.heightList.append(height)
        data.rainList.append(rain)
        data.capList.append(cap)
        data.colorList.append(color)
    for i in range(len(data.initdata)):
        stateName = data.initdata[i][0]
        idx = data.nameList.index(stateName)
        data.rainList[idx]=data.initdata[i][1]
    for i in range(len(data.nameList)):
        data.states.append(rainState(data.nameList[i],data.xList[i],data.yList[i],
            data.widthList[i],data.heightList[i],data.rainList[i],data.capList[i],data.colorList[i]))
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "graph"):   graphMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)
    elif(data.mode == "intro"):       introMousePressed(event, data)
    elif(data.mode == "quiz"):       quizMousePressed(event, data)
    elif(data.mode == "team"):       teamMousePressed(event, data)
    elif(data.mode == "ques"):       quesMousePressed(event, data)

def keyPressed(event, data,canvas):
    if(data.mode == "ques"):       quesKeyPressed(event, data,canvas)


def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "graph"):   graphTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif (data.mode == "intro"):      introTimeFired(data)
    elif(data.mode == "quiz"):       quizTimeFired(data)
    elif(data.mode == "team"):       teamTimeFired(data)
    elif(data.mode == "ques"):       quesTimeFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "graph"):   graphRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif (data.mode == "intro"):      introRedrawAll(canvas, data)
    elif(data.mode == "quiz"):       quizRedrawAll(canvas, data)
    elif(data.mode == "team"):       teamRedrawAll(canvas, data)
    elif(data.mode == "ques"):       quesRedrawAll(canvas, data)
    

####################################
# menu, background
####################################
menuColor = rgbString(93, 93, 213)
buttonColor = rgbString(42, 42, 162)

def drawMenu(canvas, data):
    canvas.create_rectangle(0,0,250, 600, fill=menuColor)
    canvas.create_text(125, 75, text="Whether\nWeather", fill=rgbString(0, 0, 102), font="Arial 30 bold")
    xStart = 20
    xEnd = 230
    cx = 125
    menuName = ["About", "Rainfall Graph", "Quiz", "Team", "Help"]
    for i in range(5):
        cy = 100+(i+1)*80
        canvas.create_rectangle(xStart, cy-30, xEnd, cy+30, fill=buttonColor)
        canvas.create_text(125, cy, text=menuName[i],fill="white", font="Arial 20 bold")

def background(canvas, data):
    canvas.create_rectangle(0,0,1000,600, fill= rgbString(204, 230,255 ))
    
def menuMousePressed(event, data):
    cx = [20, 230]
    ay = [180-30, 180+30]
    ag = [260-30, 260+30]
    aq = [340-30, 340+30]
    at = [420-30, 420+30]
    ah = [500-30, 500+30]
    inX = event.x>cx[0] and event.x<cx[1]
    inYA = event.y>ay[0] and event.y<ay[1]
    inYG = event.y>ag[0] and event.y<ag[1]
    inYQ = event.y>aq[0] and event.y<aq[1]
    inYT = event.y>at[0] and event.y<at[1]
    inYH = event.y>ah[0] and event.y<ah[1]
    if inX and inYA: data.mode="intro"
    elif inX and inYG: 
        data.mode="graph"
        replay(data)
    elif inX and inYQ: data.mode="quiz"
    elif inX and inYT: data.mode="team"
    elif inX and inYH: data.mode="help"
    
    

    
####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    enterPos = [750,500, 950,550]
    inX = event.x > enterPos[0] and event.x<enterPos[2]
    inY = event.y > enterPos[1] and event.y<enterPos[3]
    if inX and inY:
        data.mode = "intro"


def splashScreenKeyPressed(event, data):
    data.mode = "playGame"

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    (cx,cy) = (1000/2, 400/2)
    background(canvas, data)
    canvas.create_text(700, 200,
                       text="Welcome to\n    Whether\n    Weather!", font="Arial 70 bold")
    enterPos = [750,500, 950,550]
    canvas.create_rectangle(enterPos, fill = rgbString(0, 119, 230),outline=rgbString(0, 119, 230) )
    canvas.create_text((enterPos[0]+enterPos[2])/2, (enterPos[1]+enterPos[3])/2,
                       text="Click to enter!", font="Arial 20", fill ="white")
    drawCloud(canvas,data)
    
def drawCloud(canvas,cloud):
    (cx,cy)=(250, 250)
    r = 25
    canvas.create_oval(cx-80-r,cy,cx-80+r,cy+50, fill="white", outline="white")
    canvas.create_oval(cx+80-r,cy,cx+80+r,cy+50, fill="white", outline="white")
    canvas.create_oval(cx-50-r,cy-40,cx-50+r,cy+10, fill="white", outline="white")
    canvas.create_oval(cx+50-r,cy-40,cx+50+r,cy+10, fill="white", outline="white")
    canvas.create_oval(cx-1.5*r,cy-70,cx+1.5*r,cy, fill="white", outline="white")
    canvas.create_rectangle(cx-50, cy-40, cx+50, cy+10,fill="white", outline="white")
    canvas.create_rectangle(cx-80, cy, cx+80, cy+50,fill="white", outline="white")
    canvas.create_arc(200,400,220,420,start=180,extent=180,fill="white",outline="white")
    canvas.create_polygon(200,410,220,410,210,390,fill="white",outline="white")
    canvas.create_arc(250,350,270,370,start=180,extent=180,fill="white",outline="white")
    canvas.create_polygon(250,360,270,360,260,340,fill="white",outline="white")
    canvas.create_arc(290,450,310,470,start=180,extent=180,fill="white",outline="white")
    canvas.create_polygon(290,460,310,460,300,440,fill="white",outline="white")
 
####################################
# intro mode
####################################

def introMousePressed(event, data):
    menuMousePressed(event, data)

def introKeyPressed(event, data):
    pass

def introTimeFired(data):
    pass


def introRedrawAll(canvas, data):
    background(canvas, data)
    canvas.create_text(625, 80, text = "Introduction", font="Arial 30 bold")
    canvas.create_text(625, 130, text = "What is Whether Weather ?",font="Arial 26 bold")
    canvas.create_text(625,320,font="Arial 20", text='''
          Whether Weather is a program that displays \nthe weather data from each state of the United States. \nThere are also some small quizzes to test your\nunderstanding  of your howetown!!!
    
    ''')
    canvas.create_text(625,480,font="Arial 20",text='''
                notice the meaning of the colors! \n green: warm-summer mediterranean;   yellow: hot-summer mediterranean \n purple: warm-summer mediterranean continental;   orange: cold semi-arid \n red: hot dessert;   blue: warm-summer humid continental \n cyan: hot-summer humid continental;   light green: humid subtropical
    ''')
    drawMenu(canvas, data)

####################################
# help mode
####################################



def helpMousePressed(event, data):
    menuMousePressed(event, data)

def helpKeyPressed(event, data):
    data.mode = "playGame"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    background(canvas, data)
    canvas.create_text(625, 80,
                       text="Do you need help ?", font="Arial 30 bold")
    canvas.create_text(625, 200,
                       text="Click on About to see the introduction to Whether Weather.", font="Helvetica 20")
    canvas.create_text(625, 280,
                       text="Click on Rainfall Graph to see the amount of rainfall in each state per year.", font="Helvetica 20")
    canvas.create_text(625, 360,
                       text="Click on Quiz to see the questions related to weather and climate.", font="Helvetica 20")
    canvas.create_text(625, 440,
                       text="Click on Team to see the information about members who create the program.", font="Helvetica 20")
    drawMenu(canvas, data)
####################################
# Graph mode
####################################

def graphMousePressed(event, data):
    if (data.width*8/9<=event.x<=data.width*8/9+data.width/18 and
        data.height*8/9<=event.y<=data.height*8/9+data.height/18):
        data.climate = not data.climate
        print(data.climate)
    menuMousePressed(event, data)


def replay(data):
    for state in data.states:
        state.reanimate(data)
 
 
def graphRedrawAll(canvas, data):
    for state in data.states:
        state.draw(canvas,data)
    canvas.create_rectangle(data.width*8/9,data.height*8/9,data.width*8/9+data.width/18
                        ,data.height*8/9+data.height/18,fill="lightblue")
    canvas.create_text(data.width*8/9+data.width/36
                   ,data.height*8/9+data.height/36,text="climate",fill="white")
    drawMenu(canvas,data)
 
def graphKeyPressed(event, data):
    if event.keysym == "r":
        replay(data)
 
def graphTimerFired(data):
    for state in data.states:
        state.onTimerFired(data)
 


####################################
# quiz mode
####################################

def quizMousePressed(event, data):
    menuMousePressed(event, data)
    nextMousePressed(event, data)
    
def nextMousePressed(event, data):
    inX = event.x >850 and event.x<950
    inY = event.y >500 and event.y<570
    if inX and inY:
        data.mode="ques"


def getRandomList(lst):
    while len(lst)<4:
        randomIndex=random.randint(0,16)
        if randomIndex not in lst:
            lst.append(randomIndex)
    random.shuffle(lst)
    return lst
    
def state(data):
    stateIndex=random.randint(0,16)
    data.st=data.state[stateIndex]


def quizKeyPressed(event, data):
    pass

def quizTimeFired(data):
    pass
    
    
def quizRedrawAll(canvas, data):
    background(canvas, data)
    canvas.create_text(625, 80,
                       text="Quiz", font="Arial 30 bold")
    canvas.create_text(625, 130, text = "Come check your understanding!",font="Arial 26 bold")
    canvas.create_text(625, 250, text = "Press next to start!",font="Arial 20 bold")
    drawMenu(canvas, data)
    drawNext(canvas)


def drawNext(canvas):
    canvas.create_rectangle(850,500 ,950,570, fill=rgbString(93, 93, 213))
    canvas.create_text(900,535,text="next", font="Arial 26 bold", fill="white") 
 
####################################
# question mode
####################################   

def quesMousePressed(event, data):
    menuMousePressed(event, data)
    AnsMousePressed(event,data)
    

    
def AnsMousePressed(event,data):
    inX = event.x >850 and event.x<950
    inY = event.y >500 and event.y<570
    if not data.wrong:
        width = 750/4
        q = 90
        s = 25
        pos = [[250+width,300],[250+width*3,300],[250+width,400],[250+width*3,400]]
        if clicked(event,data):
            if (pos[data.ansidx[data.i]][0]-q<= event.x <= pos[data.ansidx[data.i]][0]+q and
                pos[data.ansidx[data.i]][1]-s<= event.y <= pos[data.ansidx[data.i]][1]+s):
                    data.score+=1
                    data.i=(data.i+1)%3
            else:
                data.wrong = True
                print(data.wrong)
    elif inX and inY:
        data.i=(data.i+1)%3
        data.wrong = False
    data.show = False

def clicked(event,data):
    flag = False
    width = 750/4
    pos = [[250+width,300],[250+width*3,300],[250+width,400],[250+width*3,400]]
    q = 90
    s = 25
    for i in range(4):
        if pos[i][0]+q >=event.x >=pos[i][0]-q or pos[i][1]+s>=event.y>= pos[i][1]-s:
            flag = True
    return flag

def question1(canvas,data):
    canvas.create_text(625,150,text=data.question[data.i], font="Arial 20")


def choiceBox(canvas, data):
    width = 750/4
    q = 90
    s = 25
    pos = [[250+width,300],[250+width*3,300],[250+width,400],[250+width*3,400]]
    for i in range(4):
        canvas.create_rectangle(pos[i][0]-q,pos[i][1]-s,pos[i][0]+q,pos[i][1]+s, fill=rgbString(113, 113, 218))
        canvas.create_text(pos[i],text=data.choice[data.i][i], font="Arial 20")

def drawTime(canvas,data):
    canvas.create_text(900,25,
                       text="Time = " + str(data.score), font="Arial 20")

def quesTimeFired(data):
    data.score += 1
    
def quesKeyPressed(event, data,canvas):
    data.show = True
    
def quesRedrawAll(canvas, data):
    background(canvas, data)
    drawMenu(canvas, data)
    if data.wrong:
        print("here")
        canvas.create_text(625,500,text="Sorry, the right answer is "+ data.ans[data.i],font="Arial 20")
    else:
        canvas.create_text(625,500,text="choose an answer", font="Arial 20")
    drawNext(canvas)
    question1(canvas, data)
    choiceBox(canvas, data)
    drawTime(canvas,data)



    


####################################
# team mode
####################################

def teamMousePressed(event, data):
    menuMousePressed(event, data)

def teamKeyPressed(event, data):
    pass

def teamTimeFired(data):
    pass


def teamRedrawAll(canvas, data):
    background(canvas, data)
    canvas.create_text(625, 80,
                       text="Our Team", font="Arial 30 bold")
    canvas.create_text(625, 130, text = "Who made Whether Weather ?",font="Arial 26 bold")
    canvas.create_text(625,350,font="Arial 20", text='''
          This program is made by four CMU freshmen  \n   during 2017 TartanHacks! We are: \n\n \tWenxin Ding >> Quiz \n \tCrystal Lin >> GUI \n \tJiatian Sun >> Rainfall Graphics \n \tBlair Wang >> Rainfall Data
    
    ''')
    drawMenu(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data,canvas)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


run(1000, 600)
