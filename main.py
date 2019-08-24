from tkinter import *
from math import *
from random import randrange
#print("yeet")
class startUp():
    def __init__(self):
        self.frame=Tk()
        self.size=0
        Label(self.frame,text="pick your board size").pack()
        Button(self.frame,text="32", command=lambda:choice(32,self.frame)).pack(side=LEFT)
        Button(self.frame,text="64", command=lambda:choice(64,self.frame)).pack(side=LEFT)
        self.frame.mainloop()

def choice(size,root):
    """should be a method of startUp but for some reason the buttons won't recognise it
       if its inside the class
    """
    startUp.size=size
    print(startUp.size)
    mainWin(startUp.size)
    root.destroy()
#############################################
#now for the main window
class mainWin():
    def __init__(self,size):
        self.root=Tk() #create window
        self.size=size
        self.score=0
        Label(self.root, text='YEET').pack()
        #packing
        packer(self.size,self.root)

def packer(size,root):
    """Part of mainWin
       packs the mines based on the board size"""
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
    bombList=bombNum(size) #this holds what pos are bombs, bombs are active when packed and match one of these pos's
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
        """this is where i left off, im working on a way
        to make random mines bombs"""
        self.pos=pos
        self.root=root
        self.active=active
        Button(self.root, text=str(self.pos), command=lambda:bombClick(self.active), height=2, width=3).pack(side=LEFT)

def bombClick(active):
    if active==True:
        print("game over function goes here")
    else:
        global score
        score+=100
        print("here tiles would clear and points would be added")
        print(score)

def bombNum(size):
    """picks random numbers to be bombs"""
    bombList=[]
    while len(bombList)<(size/5): #makes it so 20$ are bombs
        int=randrange(size)
        bombList.append(int)
    print(bombList)
    return bombList
##########variables
score=0


startUp()
