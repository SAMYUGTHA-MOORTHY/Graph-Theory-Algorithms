#SCL FINAL PROJECT
#IMPORTING ALL THE LIBRARIES
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#INITIALLY THE PROGRAM VARIABLES
NoOfNodes=0
Nodes=[]
Graph={}
opt=0
bfs=""
dfs=""
#USER DEFINED FUNCTIONS
def chkOpt(x):
  if(x>0 and x<4):
    return 0
  else:
    return 1
#NODES ENTER
def NodesEnter():
    global NoOfNodes
    NoOfNodes = int(Input1.get())
    GUI.destroy()    
#NODES EDGE
def NodeEdge(Num):
    global Nodes
    temp = Input21.get()
    Nodes.append(temp)
    Edge = Input22.get()
    edge_list = Edge.split(" ")
    Edges = [x for x in edge_list]
    global Graph
    Graph[temp] = Edges
    GUI2.destroy()
#MENU OPTION SELECTION
def MenuOpt():
    #ERROR OK
    def ErrorOK():
        Error.destroy()
    global opt
    while(True):
        opt=int(Input31.get())
        #CHECKING IF THE ENTERED OPTION IS VALID
        if(chkOpt(opt)==0):
            break
        #IF THE ENTERED OPTION IS NOT VALID THEN CREATING AN ERROR WINDOW
        Error= tk.Toplevel()
        Error.title('ERROR')
        EFrame = tk.Frame(master=Error)
        LabelE = tk.Label(master=EFrame,text="INVALID OPTION SELECTED.CHOOSE VALID OPTION.")
        BUTTONE = tk.Button(master=EFrame,text="OK",width=23,height=1,command=ErrorOK)
        LabelE.grid(row=0,column=0,padx=5,pady=5)
        BUTTONE.grid(row=5,column=10,pady=5,padx=5)
        EFrame.grid()
        EFrame.mainloop()
    GUI3.destroy()
def Close():
    OUTPUT.destroy()
#BFS
def BFS(Graph, startNode):
    #USING SET CONSTRUCTOR TO CREATE AN EMPTY SET TO STORE THE VISITED VERTICES IN THE GRAPH
    Visited = set()
    #QUEUE FOR STORING BFS TRAVERSAL                                                             
    Queue = [startNode]  
    #MARK THE STARTING NODE AS VISITED                                                       
    Visited.add(startNode)                                                      
    #WHILE THE QUEUE IS NOT EMPTY
    global bfs
    while Queue:
        #REMOVE THE NEXT NODE IN THE QUEUE                                                                
        node = Queue.pop(0)                                                     
        print(node, end=' ')
        bfs=bfs+str(node)+" "
        #ADD ALL UNVISITED NEIGHBOURS OF THE CURRENT NODE TO THE QUEUE
        for neighbor in Graph[node]: 
            #IF THE VERTEX IS NOT VISITED           
            if neighbor not in Visited:
              #ADDING IT TO THE VISITED LIST AND APPENDING IT TO THE QUEUE                                         
                Visited.add(neighbor)                                           
                Queue.append(neighbor)
    return bfs
#DFS
def DFS(Graph, startNode, Visited=None):
    if Visited is None:
        #USING SET CONSTRUCTOR TO CREATE AN EMPTY SET TO STORE THE VISITED VERTICES IN THE GRAPH
        Visited = set()
    #MARK THE STARTING NODE AS VISITED                                                           
    Visited.add(startNode)                                                      
    print(startNode,end=' ')
    global dfs
    dfs=dfs+str(startNode)+" "              
    #RECURSIVE CALL TO UNVISITED VERTICES OF THE CURRENT VERTEX
    for vertex in Graph[startNode]:
        #IF THE VERTEX IS NOT VISITED
        if vertex not in Visited:                                               
            DFS(Graph, vertex, Visited)
    
    return Visited
#VERTEX COLORING
def VertexColoring(Graph):
    #DICTIONARY TO STORE THE COLORS ASSIGNED TO VERTICES
    Colours = {}
    #ASSIGN 1ST COLOR TO THE 1ST VERTEX
    Colours[list(Graph.keys())[0]] = 1
    for Vertex in list(Graph.keys())[1:]:
        #CREATE A SET FOR COLORS USED BY THE ADJACENT VERTICES
        Used_Colours = set(Colours.get(adj_vertex) for adj_vertex in Graph[Vertex])
        #ASSIGN SMALLEST AVAILABE COLOUR TO THE CURRENT VERTEX
        for colour in range(1, len(Graph)+1):
            if colour not in Used_Colours:
                Colours[Vertex] = colour
                break
    
    return Colours

#GETTING INPUT FOR THE GRAPH
Graph={}
#ORGANISING THE FIRST GUI WINDOW
GUI = tk.Tk()
GUI.title("GRAPH ALGORITHMS")
#FRAME1
Frame1 = tk.Frame(master=GUI)
Title = tk.Label(master=Frame1,text = "\tCREATE YOUR GRAPH\t\t\t\t\t\n\n\n\n")
Title.pack()
Frame1.grid(row=0,column=10)
#FRAME2
Frame2=tk.Frame(master=GUI)
Label1 = tk.Label(master=Frame2,text = "ENTER THE NUMBER OF NODES IN THE GRAPH : ")
Input1 = tk.Entry(master =Frame2,width=10)
Label1.grid(row=10,column=0,padx=5)
Input1.grid(row=10,column=1,padx=5)
Frame2.grid()
#FRAME3
Frame3=tk.Frame(master=GUI)
Entry = tk.Button(master=Frame3,text="ENTER",width=25,height=1,command=NodesEnter)
Entry.grid(row=15,column=1,pady=50)
Frame3.grid(row=11,column=0)

GUI.mainloop()
#---------------------
print(NoOfNodes)
#-----------------------
WindowTitle=[]
#CREATING WINDOW TITLES 
for i in range(NoOfNodes):
    temp = "NODE "+str(i)+" DETAILS"
    WindowTitle.append(temp)
#----------------------
print(WindowTitle)
#----------------------
#CREATING NEW GUI WINDOWS FOR EACH NODE
NodeNo=1
for title in WindowTitle:
    GUI2 = tk.Tk()
    GUI2.geometry('300x200')
    GUI2.title(title)
    #FRAME1
    Frame4 = tk.Frame(master=GUI2)
    Title = tk.Label(master=Frame4,text = "\tNODE - EDGE DETAILS OF GRAPH\t\t\t\t\t\n\n\n\n")
    Title.pack()
    Frame4.grid(row=0,column=10)
    #FRAME2
    Frame5=tk.Frame(master=GUI2)
    Label21 = tk.Label(master=Frame5,text = "ENTER THE NODE : ")
    Input21 = tk.Entry(master=Frame5,width=20)
    Label22 = tk.Label(master=Frame5,text="ENTER THE ADJACENT NODES : ")
    Input22 = tk.Entry(master=Frame5,width=20)
    Label21.grid(row=10,column=0,padx=5)
    Input21.grid(row=10,column=1,padx=5)
    Label22.grid(row=11,column=0,padx=5)
    Input22.grid(row=11,column=1,padx=5)
    Frame5.grid()
    #FRAME3
    Frame6=tk.Frame(master=GUI2)
    Entry = tk.Button(master=Frame6,text="SUBMIT",width=25,height=1,command= lambda: NodeEdge(NodeNo))
    Entry.grid(row=15,column=1,pady=50)
    Frame6.grid(row=11,column=0)
    GUI2.mainloop()
    NodeNo=NodeNo+1
 
#---------------------------    
print(Nodes)
print(Graph) 
#---------------------------

#SHOWING THE GRAPH IN THE TKINTER WIINDOW
Gwindow = tk.Tk()
Gwindow.title("YOUR GRAPH!!")
#CREATING GRAPH OBJECT WITH DICTIONARY
graph = nx.Graph(Graph)
#DRAWING THE GRPAH AND CREATING THE FIGURE OBJECT
fig, ax = plt.subplots()
nx.draw(graph, with_labels=True, ax=ax)
#CREATING FigureCanvasTkAgg OBJECT FROM THE Figure OBJECT
canvas = FigureCanvasTkAgg(fig, master=Gwindow)
canvas.draw()
# add the FigureCanvasTkAgg object to the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1,padx=15,pady=15)
Gwindow.mainloop()

#ASKING WHICH GRAPH FUNCTIONALITY THE USER WANTS TO USE BY DISPLAYING THE MENU
GUI3 = tk.Tk()
GUI3.title('MENU')
Frame7 = tk.Frame(master=GUI3)
Label31 = tk.Label(master = Frame7,text ="\t\t\t\t\t AVALILABLE ALGORITHMS \n\n[1].BFS\n[2].DFS\n[3].VERTEX COLORING\n\n")
Label32 = tk.Label(master=Frame7,text="ENTER YOUR CHOICE : ")
Input31 = tk.Entry(master=Frame7,width = 20)
Entry   = tk.Button(master = Frame7,text='ENTER',width=23,height=1,command=MenuOpt)
Label31.grid(row=0,column=0)
Label32.grid(row=5,column=0,padx=5)
Input31.grid(row=5,column=1,padx=5)
Entry.grid(row=15,column=1,pady=50)
Frame7.grid()
GUI3.mainloop()
#------------------------

print(opt)
#------------------------
#TO RUN THE MENU AND CREATING AN OUTPUT WINDOW TO SHOW THE RESULT OF THE GRAPH ALGORITHMS
OUTPUT = tk.Tk()
OUTPUT.title("GRAPH ALGORITHMS OUTPUT")
if(opt==1):
  #CALL BFS
  BFSOrder=BFS(Graph,Nodes[0])
  Frame8 = tk.Frame(master=OUTPUT)
  Label41=tk.Label(master=Frame8,text="\t\t BFS ORDER : ")
  Label42=tk.Label(master=Frame8,text=BFSOrder)
  Label41.grid(row=0,column=0,padx=5,pady=5)
  Label42.grid(row=0,column=1,padx=5,pady=5) 
  Close=tk.Button(master=Frame8,text="CLOSE",width=23,height=1,command=Close)
  Close.grid(row=5,column=1,padx=5,pady=5)
  Frame8.grid()
elif(opt==2):
  #CALL DFS
  DFS(Graph,Nodes[0])
  Frame8 = tk.Frame(master=OUTPUT)
  Label41=tk.Label(master=Frame8,text="\t\t DFS ORDER : ")
  Label42=tk.Label(master=Frame8,text=dfs)
  Label41.grid(row=0,column=0,padx=5,pady=5)
  Label42.grid(row=0,column=1,padx=5,pady=5) 
  Close=tk.Button(master=Frame8,text="CLOSE",width=23,height=1,command=Close)
  Close.grid(row=5,column=1,padx=5,pady=5)
  Frame8.grid()
elif(opt==3):
  #CALL VERTEX COLOURING ALGORITHM
  colours={}
  colours = VertexColoring(Graph)
  col = max(colours.values())
  Frame8 = tk.Frame(master=OUTPUT)
  Label41=tk.Label(master=Frame8,text="THE MAXIMUM NO. OF COLORS REQUIRED ARE : ")
  Label42=tk.Label(master=Frame8,text=str(col))
  Label41.grid(row=0,column=0,padx=5,pady=5)
  Label42.grid(row=0,column=1,padx=5,pady=5) 
  Close=tk.Button(master=Frame8,text="CLOSE",width=23,height=1,command=Close)
  Close.grid(row=5,column=1,padx=5,pady=5)
  Frame8.grid()
  
OUTPUT.mainloop()