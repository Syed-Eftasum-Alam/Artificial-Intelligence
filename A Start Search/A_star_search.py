from queue import PriorityQueue

node_map =	{
  0: 'S',
  1: 'A',
  2: 'B',
  3: 'C',
  4: 'D',
}


parent_map =	{
  0: None,
  1: 0,
  2: 1,
  3: 2,
  4: 3,
}

cost_map =	{
  (0,1): 1,
  (0,2): 4,
  (1,2): 2,
  (1,3): 5,
  (1.4): 12,
  (2,3): 2,
  (3,4): 3
}


def calculate_cost(path):
    path_size=len(path)
    total_cost=0
    
    for i in range (0,path_size-1):
      total_cost=total_cost+(cost_map[  path[i],path[i+1]   ]  )

    return total_cost  
      

    



adjacent_nodes =[ [  1,1,2,4 ] , [   2,2,3,5,4,12   ] , [ 3,2  ] , [ 4,3 ]  ]

heuristic_values= [ 7,6,2,1,0  ]




class node:
  
  def __init__(self, node_no, prev_node, actual_cost, total_cost):
    self.node_no = node_no
    self.prev_node = prev_node
    self.actual_cost = actual_cost
    self.total_cost =total_cost
    
  


node_0= node( 0, None ,  0, 7) 
node_1= node( 1, 0 ,  1, 7) 
node_2= node( 2, 0 ,  4, 6) 
node_3= node( 2, 1 ,  3, 5) 
node_4= node( 3, 1 ,  6, 7) 
node_5= node( 3, 2,   5, 6)
node_6= node( 4, 1,   13, 13)
node_7= node( 4, 3,   8, 8)


minq= PriorityQueue()

minq.put((node_0.total_cost,node_0))

while not minq.empty() :
   
    obj =minq.get()
   ## print(obj[1].node_no)
   
    if obj[1].node_no==4:
      print("path found")
      path=[4]
      current_node=4;
      while True:

          
          current_node=parent_map[current_node]
          if current_node==None:
           break
          path.insert(0,current_node)

      print(path)
      print("path cost: ")
      print(calculate_cost(path))
      break
    



    else:
      
      sz=len(adjacent_nodes[obj[1].node_no])

      for num in range(0,sz-1,2):
        pushing_node=adjacent_nodes[obj[1].node_no][num]
        print("pushing node: ")
        print(pushing_node)

        if pushing_node==1 and obj[1].node_no==0:
           minq.put((node_1.total_cost,node_1))

        elif pushing_node==2 and obj[1].node_no==0: 
           minq.put((node_2.total_cost,node_2))

        elif pushing_node==2 and obj[1].node_no==1: 
           minq.put((node_3.total_cost,node_3))  

        elif pushing_node==3 and obj[1].node_no==1: 
           minq.put((node_4.total_cost,node_4))  

        elif pushing_node==3 and obj[1].node_no==2: 
           minq.put((node_5.total_cost,node_5)) 

        elif pushing_node==4 and obj[1].node_no==1: 
           minq.put((node_6.total_cost,node_6)) 

        elif pushing_node==4 and obj[1].node_no==3: 
           minq.put((node_7.total_cost,node_7))             
