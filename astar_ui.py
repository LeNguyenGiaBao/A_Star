import tkinter as tk 
from astar import * 
import time

color = 'white'
path=[]
maze=[]
listButton=[]

size = 0


def mazeN():
	"""create the game with size if the number input"""
	global size
	if(entrySize.get().isdigit()):		#check input is a number
		size = int(entrySize.get())
		CreateGame(size)				#call CreateGame


def ClickOK():
	"""from input is the buttons, find the path """
	global maze
	maze=[]
	for i in range(size):
		maze.append([0]*size)			#create maze is list of zeros
	global path
	path = []
	start = None	#create start
	goal = None		#creata goal
	for i in range(size):
		for j in range(size):
			if(listButton[i][j]['bg']=='red'):			#if this button is the step of the solution, clear it
				listButton[i][j]['bg']='white'
			if(listButton[i][j]['bg']=='black'):		#wall
				maze[i][j]=1
			if(listButton[i][j]['bg']=='yellow'):		#start
				start = tuple([i,j])
			if(listButton[i][j]['bg']=='green'):		#goal
				goal = tuple([i,j])
	if(start!=None and goal !=None):
		begin = time.time()
		path = astar(maze, start, goal)
		end = time.time()
		if(path!=None and path !=[]):
			lbPath['text'] = len(path)		#show the path cost
			lbTime['text'] = "{:.7f}".format(float(end-begin))		#show time
			path = path[1:-1]				#return the path without start and goal
		else:
			lbPath['text'] = 'None'
			lbTime['text'] = 'None'


def SetUpStart():
	global color
	color = 'yellow'			#the color of the start is yellow
	lbColor['bg']=color 		#Change the color of the label color, for current status

def SetUpGoal():
	global color
	color = 'green'				#the color of the goal is green
	lbColor['bg']=color 		#Change the color of the label color, for current status

def SetUpWall():
	global color
	color = 'black'				#the color of the wall is black 
	lbColor['bg']=color 		#Change the color of the label color, for current status


def SetUpColor(index):
	""" to set up the color of the button when click"""
	if listButton[int(index/size)][int(index%size)]['bg']== 'white':		#default color
		listButton[int(index/size)][int(index%size)]['bg']= color 			#set color
	else:
		listButton[int(index/size)][int(index%size)]['bg']= 'white'			#return default color


def CreateGame(size):
	"""set up size x size button"""
	global listButton
	listButton=[]
	for i in range(size):
		li = []
		for j in range(size):
			bt = tk.Button(frame, bg='white', command = lambda position=(i*size + j):SetUpColor(position)) 	#create size x size button and set event click
			bt.place(relx=j/size, rely=i/size, relwidth=1/size, relheight=1/size)		
			li.append(bt) 				#append in the temp list
		listButton.append(li)			#append in the list button

def move():
	"""get the path and show in the game"""
	if(path!=[] and path != None):
		step = path.pop(0)
		listButton[step[0]][step[1]]['bg']='red'	#show the route	

def reset():
	CreateGame(size)


def Auto():
	"""show the route when click, like auto click button next step"""
	ClickOK()
	if(path!=None and path !=[]):
		for i in range(len(path)):
			move()
			time.sleep(0.05)
			root.update()

root = tk.Tk()

#add widget
canvas = tk.Canvas(root, height=500, width=530)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relwidth=0.8, relheight=1)

rightFrame = tk.Frame(root, bg='#8ad4e1')
rightFrame.place(relwidth=0.2, relheight=1, relx=0.8, rely=0)


lbEnterSize = tk.Label(rightFrame, text='Enter size: ')
lbEnterSize.place(relx=0.1, rely=0.05)

entrySize = tk.Entry(rightFrame)
entrySize.place(relx=0.1, rely=0.1, relwidth=0.8, height=30)


btSetUp = tk.Button(rightFrame, text='Set Up', command = mazeN)
btSetUp.place(relx=0.1, rely=0.17)

lbColor = tk.Label(rightFrame, bg=color)
lbColor.place(relx=0.1, rely=0.25, width = 50)


btSetUpStart = tk.Button(rightFrame, text='Set up Start', command = SetUpStart)
btSetUpStart.place(relx=0.1, rely=0.3)

btSetUpGoal = tk.Button(rightFrame, text='Set up Goal', command = SetUpGoal)
btSetUpGoal.place(relx=0.1, rely=0.36)

btSetUpWall = tk.Button(rightFrame, text='Set up Wall', command = SetUpWall)
btSetUpWall.place(relx=0.1, rely=0.42)

btOK =tk.Button(rightFrame, text='OK', command=ClickOK)
btOK.place(relx=0.1, rely=0.54)

btAuto = tk.Button(rightFrame, text='Auto', command = Auto)
btAuto.place(relx=0.5, rely=0.54)

btNextstep = tk.Button(rightFrame, text='Next Step', command = move)
btNextstep.place(relx=0.1, rely=0.6)

btReset = tk.Button(rightFrame, text='Reset', command = reset)
btReset.place(relx=0.1, rely=0.66)

lbPathcost = tk.Label(rightFrame, text='Path cost: ')
lbPathcost.place(relx=0.1, rely=0.85)

lbPath = tk.Label(rightFrame)
lbPath.place(relx=0.65, rely=0.85)

lbTime1 = tk.Label(rightFrame, text = "Time: ")
lbTime1.place(relx=0.1, rely=0.8)

lbTime = tk.Label(rightFrame)
lbTime.place(relx=0.45, rely=0.8)

root.mainloop()


