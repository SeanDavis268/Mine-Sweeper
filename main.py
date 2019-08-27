from tkinter import *
from math import *
from random import randrange
import gc

#print("yeet")
class startUp():
    def __init__(self):
        self.frame=Tk()
        self.size=0
        Label(self.frame,text="pick your board size").pack()
        Button(self.frame,text="32", command=lambda:choice(36,self.frame)).pack(side=LEFT)
        Button(self.frame,text="64", command=lambda:choice(64,self.frame)).pack(side=LEFT)
        #below is the difficulty settings
        global difficulty

        difficulty=IntVar()
        Radiobutton(self.frame,variable=difficulty, value=15,text='easy').pack()
        Radiobutton(self.frame,variable=difficulty, value=25,text='medium').pack()
        Radiobutton(self.frame,variable=difficulty, value=33,text='hard').pack()


        self.frame.mainloop()



def choice(size,root):
    """should be a method of startUp but for some reason the buttons won't recognise it
       if its inside the class
    """
    #startUp.size=size
    #print(startUp.size)
    root.destroy()
    mainWin(size)

#############################################
#now for the main window
class mainWin():
    def __init__(self,size):
        self.root=Tk() #create window

        self.size=size
        global neighborSize
        neighborSize=size #this is for the neighbors function

        global score
        score=0
        #print('------------------------')
        global fuck
        fuck=PhotoImage(file='minesweeperMine.png')
        #print('DID I MAKE IT HERE--------------')
        global coveredMine
        coveredMine=PhotoImage(file='coveredMine.png')
        print(coveredMine)


        Label(self.root,text='fuuuuuuck').pack()
        #packing
        packer(self.size,self.root)
        self.root.mainloop()
    def destroy():
        '''this destroys the old window and makes another that
        can restart the game'''
        global top
        print('yay')
        top.destroy()
        #window is destroyed, opens box that shows final score
        GameOver(score)

class GameOver():
    def __init__(self,score):
        self.root=Tk()
        score=score
        Label(self.root,text=str(score)).pack()
        Button(self.root,text='Play Again?', command=lambda:restarter(self.root)).pack()


def restarter(root):
    root.destroy()
    oof=startUp()




def packer(size,root):
    """Part of mainWin
       packs the mines based on the board siz e"""
    global top
    top=root
    layer1=Frame(root)
    layer2=Frame(root)
    layer3=Frame(root)
    layer4=Frame(root)
    layer5=Frame(root)
    layer6=Frame(root)
    layer7=Frame(root)
    layer8=Frame(root)
    layer9=Frame(root)
    layerList=[layer1,layer2,layer3,layer4,layer5,layer6,layer7,layer8,layer9]

    square=int(sqrt(size))
    global difficulty
    print(difficulty.get()) #its currently having a difficulty of 0 when restarting
    global bombList
    bombList=bombNum(size,difficulty) #this holds what pos are bombs, bombs are active when packed and match one of these pos's
    position=0


    for i in range(square):
        layer=layerList[i]

        for digit in range(square):
            if position in bombList: #if the bomb is being placed in a pos marked active
                Mine(layer,position,True)
            else:
                Mine(layer,position)
            position+=1
    for each in layerList:
        each.pack()

class Mine():

    def __init__(self,root,pos,active=False):

        """This is the button that acts as the mines, either active or inactive"""
        self.pos=pos
        self.root=root
        self.active=active
        global coveredMine
        self.image=coveredMine

        Mine.creator(self.root,self.image,self.pos,self.active)
        #self.button=Button(self.root, text=str(self.pos), command=lambda:bombClick(self.button,self.active), height=2, width=3 )

        #self.button.pack(side=LEFT)
    def creator(root,image,pos,active):
        button=Button(root, text=str(pos), command=lambda:bombClick(button,active,pos))

        #button.config(image=image)
        button.pack(side=LEFT)



def bombClick(obj,active,pos):
    obj.config(relief=SUNKEN)
    if active==True:
        global fuck
        print("game over function goes here")
        obj.config(image=fuck)
        mainWin.destroy()
    else:
        global score
        score+=100
        print("here tiles would clear and points would be added")
        obj.config(text=str(neighbors(pos)))
        print(score)

def neighbors(pos):
    global bombList
    global neighborSize
    west=False
    north=False
    south=False
    east=False
    #if neighborSize==36: #small board
    if pos == [0,6,12,18,24,30]:    #when in leftmost spot
        west = False
    else:
        if (pos-1) in bombList: #bomb to the left is active
            west=True
            print(pos-1)
#
    if pos in [0,1,2,3,4,5]:
        north = False
    else:
        if (pos-6) in bombList: #bomb above  is active
            print(pos-6)
            north=True
#
    if pos in [30,31,32,33,34,35]:
        south = False
    else:
        if (pos+6) in bombList: #bomb to the left is active
            south=True
            print(pos+6)
#
    if pos in [5,11,17,23,29,35]:
        east = False
    else:
        if (pos+1) in bombList: #bomb to the left is active
            east=True

    neighborBombs=[west,north,east,south]
    #####################
    total=0
    for each in neighborBombs:
        if each == True:
            total+=1
    return total


def bombNum(size,difficulty):
    """picks random numbers to be bombs"""
    bombList=[]
    difficulty=difficulty.get()

    while len(bombList)<(size*(difficulty/100)): #makes it so 20$ are bombs
        int=randrange(size)
        bombList.append(int)
    print(bombList)

    return bombList
##########variables
score=0

oof=startUp()
