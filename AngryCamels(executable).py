#Momin Javed and Antares Rahman
#Final project: AngryCamels(executable).py
#Due: December 18, 2013

from math import *
from graphics import *
from buttonClass import *
from random import *

class Projectile:
    """A Projectile constructor which takes in the angle in radians,
    initial velocity in m/s, the x-coordinate of the object and its height
    (y-coordinate)."""
    def __init__(self, angle, velocity, x, height):
        self.xpos = x #x-position of the object to be thrown
        self.ypos = height #y-position of the object to be thrown

        ##dividing velocity vector into x and y components##
        self.xvel = velocity * cos(angle)
        self.yvel = velocity * sin(angle)
        
        self.moveY = 0 #initial shift of position of object in y direction
        self.moveX = 0 #initial shift of position of object in x direction
        
    def update(self, time):
        """A method which updates all the input values untill upto the
        time entered."""

        ##using equations of Physics to update values##
        self.moveX = time * self.xvel
        self.xpos = self.xpos + self.moveX
        yvel1 = self.yvel - 9.8 * time #yvel1 is a temporary variable used to briefly store the
                                       #updated value of self.yvel
        self.moveY = time * (self.yvel + yvel1) / 2.0
        self.ypos = self.ypos + self.moveY
        self.yvel = yvel1
        
    def getYpos(self):
        """Returns the current y-coordinate of the object in Projectile."""
        return self.ypos
    
    def getXpos(self):
        """Returns the current x-coordinate of the object in Projectile."""
        return self.xpos
    
    def getMoveY(self):
        """Returns the latest shift the Project went through in the y direction."""
        return self.moveY
    
    def getMoveX(self):
        """Returns the latest shift the Project went through in the x direction."""
        return self.moveX
    

################################## HELPER FUNCTIONS ###########################################


def title(gwin):
    #Sets up the title screen and required buttons (PLAY & How to Play?).
    #Also includes additional features - a random projectile upon a stray
    #click with the appearance of a dialogue bubble with "Wait..." on it.
    
    titlebg = Image(Point(450,325), "Images/Backgrounds/titlebg.gif")
    titlebg.draw(gwin)
    introB = Button(gwin, Point(842,618),120,60,"How to Play?", "gold")
    start = Button(gwin, Point(450,65), 200, 100, "", "green3")
    labelStart = Text(Point(450,65),"P L A Y !")
    labelStart.setStyle("bold")
    labelStart.setSize(30)
    labelStart.setFill("white")
    labelStart.draw(gwin)
    positions = [Point(455,497), Point(575,497), Point(690, 497)] #speech bubble positions
    x0, time = -20, 0.001 #input variables for the Projectile class
    vel = 108.5
    
    pt = gwin.getMouse()
    while not start.clicked(pt): #while PLAY button is not clicked
        
        if introB.clicked(pt): #if How to Play? button is clicked
            introB.undraw() #undraw the How to Play? button
            intro(gwin) #intro function is called and executed(described below)
            introB.draw(gwin) #draw the How to Play? button
            pt = gwin.getMouse()
            
        else: #if a stray click, shoot in a random Projectile with a "Wait..." bubble    
            speech_pos = positions[randrange(3)]
            speech = Image(speech_pos, "Images/speech_bubble.gif")
            speech.draw(gwin)
            prompt = Text(speech_pos, "Wait...")
            prompt.setFill("white")
            prompt.setStyle("bold")
            prompt.setSize(14)
            prompt.draw(gwin)
            h0 = randrange(150,350) #input variable of height for Random projectile
                                    #is set randomly within this range
            camel = Image(Point(x0,h0), "Images/camel.gif")
            camel.draw(gwin)
            angle = (pi/2)*random() #angle selected randomly from 0 till pi/2
            cball = Projectile(angle, vel, x0, h0) #Projectile class is called
            while not (cball.getYpos() <= 148): #while not hit the ground
                cball.update(time) #keep updating values
                x,y = cball.getMoveX(), cball.getMoveY()
                camel.move(x,y) #move projectile according to updated values
            speech.undraw()
            prompt.undraw()
            pt = gwin.getMouse()
            camel.undraw()
            
    #if PLAY button is clicked, the screen in cleared for setting up the Main Menu       
    titlebg.undraw()
    introB.undraw()
    start.undraw()
    labelStart.undraw()
    return pt

def file_read(filename):
    #File reader - reads the file named 'filename'.txt
    file = open(filename + ".txt", "r") #opens file named 'filename'.txt
    readFile = file.read() #reads the whole file as a string
    return readFile #returns one string containing the whole text

def intro(gwin):
    #Called when "How To Play?" is clicked. Draws a huge rectangle and displays
    #the rules on it, which are read from a text file.
    
    intro_canvas = Rectangle(Point(150,0), Point(750,650))
    intro_canvas.setFill(color_rgb(51, 85, 153))
    intro_canvas.setOutline(color_rgb(51, 85, 153))
    intro_canvas.draw(gwin)
    story = file_read("Intro") #the file_read function is called
    storyDisp = Text(Point(450,325), story) #the text is displayed
    storyDisp.setFill("white")
    storyDisp.setStyle("bold")
    storyDisp.draw(gwin)
    
    gwin.getMouse() #everything undrawn after a click
    intro_canvas.undraw()
    storyDisp.undraw()

def menuFunc(gwin):
    #Sets up the screen for the Main Menu where user can decide the
    #difficulty level he/she chooses to play. Levels are explained using
    #images displayed on top of the "easy" and "hard" buttons.
    
    menubg = Image(Point(450,325), "Images/Backgrounds/mainmenubg.gif")
    menubg.draw(gwin)
    easy = Button(gwin, Point(250,395), 360,405, "", "")
    easyImg = Image(Point(247,395), "Images/easy.gif")
    easyFilm = Image(Point(250,395), "Images/FilmStrip.gif")
    easyImg.draw(gwin)
    easyFilm.draw(gwin)
    hard = Button(gwin, Point(650,395), 360,405, "", "")
    hardImg = Image(Point(645,395), "Images/hard.gif")
    hardFilm = Image(Point(650,395), "Images/FilmStrip.gif")
    hardImg.draw(gwin)
    hardFilm.draw(gwin)
    exitB = Button(gwin, Point(872,630), 60,40,"Exit", "red3")

    pt = gwin.getMouse()
    while not (easy.clicked(pt) or hard.clicked(pt) or exitB.clicked(pt)):
        pt = gwin.getMouse() #ensures stray click robustness
        
    if easy.clicked(pt):
        menubg.undraw()
        easy.undraw()
        easyImg.undraw()
        hard.undraw()
        hardImg.undraw()
        easyFilm.undraw()
        hardFilm.undraw()
        return 1 #for Easy level
    
    elif hard.clicked(pt):
        menubg.undraw()
        easy.undraw()
        easyImg.undraw()
        hard.undraw()
        hardImg.undraw()
        easyFilm.undraw()
        hardFilm.undraw()
        return 2 #for Hard level
    
    else:
        return "" #if Exit is clicked
        
def main():

    ##The graphic window, Exit button, trialDisplay and outcome display is setup##
    win = GraphWin("(^_^) Angry Camels!", 900,650)
    win.setCoords(0,0,900,650)
    exitB = Button(win, Point(872,630), 60,40,"Exit", "red3")
    exitB.undraw()
    catapult = Image(Point(103,185), "Images/catapult.gif")
    x0, h0, time = 100, 240, 0.001 #initial inputs for the Projectile class
    trialDisplay = Text(Point(130,20), "") #will display how many shots are left
    trialDisplay.setStyle("bold")
    trialDisplay.setFill("white")
    outcome = Text(Point(450,600), "") #will display the outcome at the end of the game
    outcome.setSize(20)
    outcome.setStyle("bold")

    pt = title(win)
    while not exitB.clicked(pt): #while Exit button is not clicked
        level = menuFunc(win) #menuFunc function is called to select difficulty level

        ##target co-ordinates appropriate to the level are setup##
        if level == 1:
            targetX, targetY = 700,300 #target center coordinates
            tRangeX1, tRangeX2 = 646.5,753.5 #width-span of target
            tRangeY1, tRangeY2 = 235.5,364.5 #height-span of target
            
        elif level == 2:
            targetX, targetY = 625,195
            tRangeX1, tRangeX2 = 585,665
            tRangeY1, tRangeY2 = 130.5,263
            
        else: #if exit was clicked
            break #break from loop and exit
        
        ##Game background setup with appropriate buttons and game images##   
        bg = Image(Point(450,325), "Images/Backgrounds/level"+str(level)+".gif")
        bg.draw(win)
        launch = Button(win, Point(37,20),70,40,"Launch!", color_rgb(51, 85, 153))
        launch.deactivate()
        exitB = Button(win, Point(872,630), 60,40,"Exit", "red3")
        catapult.draw(win)
        target = Image(Point(targetX,targetY), "Images/target.gif")
        target.draw(win)
        finalX, finalY = 100, 200
        trial = 0
        while True:
            if (tRangeX1<=finalX<=tRangeX2 and tRangeY1<=finalY<=tRangeY2): #if target was hit previously
                target.draw(win) #draw the target again
                
            camel = Image(Point(x0,h0), "Images/camel.gif") #ammo drawn
            camel.draw(win)
            vel = 0
            angle = 0
            x1, h1 = x0, h0
            trialDisplay.setText("Shots left: "+str(3-trial)) #no. of shots left are displayed
            trialDisplay.draw(win)
            
            pt = win.getMouse()
            if exitB.clicked(pt):
                break
            while not (launch.clicked(pt) or exitB.clicked(pt)): #setting the angle and velocity of the Projectile visually   
                camel.undraw()

                ##New ammo drawn at the point of user-click. Velocity of projection is setup
                #using the distance of click from the initial point as a scale for velocity and the angle is inputted as per
                #the angle formed between the user-click and the initial point from the horizontal.##
                x1 = pt.getX()
                h1 = pt.getY()
                diffY = h0 - h1
                diffX = x0 - x1
                length = (diffY**2 + diffX**2)**(1/2) #length between initial position and user-click
                angle = atan((diffY)/(diffX)) #angle from horizontal calculated

                ##trigonimetric corrections are made##
                if diffX < 0:
                    angle = pi + angle            
                if length > 90: #length is capped at 90 and appropriate recalculations are made
                    length = 90
                    diffX = 90*cos(angle)
                    diffY = 90*sin(angle)
                    x1 = x0 - diffX
                    h1 = h0 - diffY

                #two lines are drawn to give a sling-shot look
                string1 = Line(Point(x1,h1),Point(71.08,243.34))
                string2 = Line(Point(x1,h1),Point(129.14,245.34))
                string1.setWidth(3)
                string2.setWidth(3)
                string1.draw(win)
                string2.draw(win)
                camel = Image(Point(x1,h1), "Images/camel.gif")
                camel.draw(win)
                launch.activate()
                vel = 1.5*length
                pt = win.getMouse()
                string1.undraw()
                string2.undraw()
                
            if exitB.clicked(pt):
                break
            
            cball = Projectile(angle, vel, x1, h1) #Projectile class is called
            
            if level == 1:
                ## for level 1, while not ground is hit, or target is hit or stone is hit##
                while not (cball.getYpos() <= (113) or (646.5<=cball.getXpos()<=753.5 and 235.5<=cball.getYpos()<=364.5)\
                           or (550.12<=cball.getXpos()<=839.41 and 84<=cball.getYpos()<=260.5)):
                    
                    cball.update(time) #keep updating values
                    x,y = cball.getMoveX(), cball.getMoveY()
                    camel.move(x,y) #move according to the updated values
            else:
                ## for level 2, while not ground is hit, or target is hit or stone is hit##
                while not (cball.getYpos() <= (113) or (500.07<=cball.getXpos()<=753.32 and 84<=cball.getYpos()<=263)):
                    cball.update(time)
                    x,y = cball.getMoveX(), cball.getMoveY()
                    camel.move(x,y)
                    
            finalX = cball.getXpos()
            finalY = cball.getYpos()
            trial +=1 #trial is incremented
            trialDisplay.undraw()
            camel.undraw()
            
            if (tRangeX1<=cball.getXpos()<=tRangeX2 and tRangeY1<=cball.getYpos()<=tRangeY2) or trial == 3: #if target is hit or allowed trials end
                if (tRangeX1<=cball.getXpos()<=tRangeX2 and tRangeY1<=cball.getYpos()<=tRangeY2): #if target is hit

                    ##draw appropriate rewards##
                    if level == 1:
                        bucket = Image(Point(492.5,405), "Images/Buckets/bucket" + str(trial-1) + ".gif")
                        bucket.draw(win)
                    else:
                        bucket1 = Image(Point(357.5,405), "Images/Buckets/bucket" + str(trial-1) + ".gif")
                        bucket2 = Image(Point(627.5,405), "Images/Buckets/bucket" + str(trial-1) + ".gif")
                        bucket1.draw(win)
                        bucket2.draw(win)
                    outcome.setText("Great Job Camel!")
                    outcome.setFill("green3")
                    outcome.draw(win)
                    target.undraw()
                    
                else: #if allowed trials end

                    ##draw appropriate penalties##
                    if level == 1:
                        bucket = Image(Point(492.5,405), "Images/Buckets/bucket" + str(trial) + ".gif")
                        bucket.draw(win)
                    else:
                        bucket1 = Image(Point(357.5,405), "Images/Buckets/bucket" + str(trial) + ".gif")
                        bucket2 = Image(Point(627.5,405), "Images/Buckets/bucket" + str(trial) + ".gif")
                        bucket1.draw(win)
                        bucket2.draw(win)
                    outcome.setText("It's okay...try again!")
                    outcome.setFill("red3")
                    outcome.draw(win)
                                 
                launch.deactivate()

                #play and menu buttons are setup
                play = Button(win, Point(375,275), 100,40, "Play Again!", "orange")
                menu = Button(win, Point(525,275), 100,40, "Main Menu", "green3")                        
                pt = win.getMouse()

                while not (exitB.clicked(pt) or play.clicked(pt) or menu.clicked(pt)):
                    pt = win.getMouse() #stray click robustness
                
                #if any of the above buttons are clicked
                trial = 0 #trial reset to 0
                outcome.undraw()
                if level == 1:
                    bucket.undraw()
                else:
                    bucket1.undraw()
                    bucket2.undraw()

                if exitB.clicked(pt) or menu.clicked(pt):
                    #screen cleared out
                    bg.undraw()
                    launch.undraw()
                    catapult.undraw()
                    target.undraw()
                    menu.undraw()
                    play.undraw()
                    break #this loop breaks. For exitB, the next loops breaks too and program ends.
                          #For menu, the next loop doesn't break and thus program reaches the top again.
                menu.undraw()
                play.undraw()
                
    win.close()

main()
