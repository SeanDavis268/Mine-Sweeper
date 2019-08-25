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
    startUp.size=size
    print(startUp.size)
    root.destroy()
    mainWin(startUp.size)

#############################################
#now for the main window
class mainWin():
    def __init__(self,size):
        self.root=Tk() #create window
        self.size=size
        self.score=0
        global fuck
        fuck=PhotoImage(file='minesweeperMine.png')


        Label(self.root,text='fuuuuuuck').pack()
        #packing
        packer(self.size,self.root)
        self.root.mainloop()






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
    global difficulty
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
        global fuck
        self.image=fuck
        Mine.creator(self.root,self.image,self.pos,self.active)
        #self.button=Button(self.root, text=str(self.pos), command=lambda:bombClick(self.button,self.active), height=2, width=3 )

        #self.button.pack(side=LEFT)
    def creator(root,image,pos,active):
        button=Button(root, image=image, command=lambda:bombClick(button,active) )
        button.pack(side=LEFT)

def bombClick(obj,active):
    obj.config(relief=SUNKEN)
    if active==True:
        print("game over function goes here")
    else:
        global score
        score+=100
        print("here tiles would clear and points would be added")
        print(score)

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
