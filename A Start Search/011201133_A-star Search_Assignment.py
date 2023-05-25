from queue import PriorityQueue

adjacency_list = {
    'S': [('A', 1), ('B', 4),],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0,
}

class Node:
  def __init__(self,nodeName,parent,actualcost,huristic,pathocost):
    self.nodeName=nodeName
    self.parent=parent
    self.actualcost=actualcost
    self.huristic=huristic
    self.totalcost=actualcost+huristic
    self.pathcost=pathocost

  def __lt__(self, o):
      return self.totalcost < o.totalcost

  def __str__(self):
        return f'{self.nodeName}'    
  


node0=Node('S',None,0,7,0)


Queue = PriorityQueue()

Queue.put(node0)
path=[]

while not Queue.empty() :

  obj=Queue.get()
  
  if obj.nodeName=='D':
    while True:
      path.append(obj)
      if obj.parent == None:
        break
      obj=obj.parent     
    break
  

  else:
     for neighbour in adjacency_list[obj.nodeName]:
      newCost= obj.actualcost+neighbour[1]
      nodeX=Node(neighbour[0],obj,newCost,H[neighbour[0]],neighbour[1])
      Queue.put(nodeX)

path.reverse()      
for i in range (len(path)):
  print(path[i].nodeName,"->",end='')   

total=0
for i in range (len(path)):
  total = total+path[i].pathcost   

print('\n')
print('Path Cost:-',total)