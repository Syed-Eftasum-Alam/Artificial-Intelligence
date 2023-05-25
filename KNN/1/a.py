import numpy as np
import pandas as pd

import random

from scipy.spatial import distance

data = np.genfromtxt('diabetes.csv',dtype=None,skip_header=1,delimiter=',',usecols=(0,1,2,3,4,5,6,7,8,9,10))

# shuffling 2d array
# print(data)

np.random.shuffle(data)


# converting into list
dataList = data.tolist();  


X_train=[]

y_train=[]

X_test=[]

y_test=[]

X_val=[]

y_val=[]




for data in dataList:
  r_num=random.random()

  if r_num>=0.0 and r_num<=0.7:
    X_train.append(data[0:10])  
    y_train.append(data[10])
  elif r_num>0.7 and r_num<=0.85:
    X_test.append(data[0:10])
    y_test.append(data[10])
  else:
    X_val.append(data[0:10])
    y_val.append(data[10])  


Mean_Squared_Errors={
    
}

for k in range(1,50,2):

 error=0
 for i in range(len(X_val)):
   All_euclidean_dist = []
   for j in range(len(X_train)):
     Eudis = distance.euclidean(X_val[i], X_train[j])
     All_euclidean_dist.append([Eudis, y_train[j] ])
   All_euclidean_dist.sort()
   sum=0
   for pt in range(k):
     sum=sum+All_euclidean_dist[pt][1]
   avg=(sum*1.0)/k
   dif=y_val[i]-avg
  #  error count from diffarance of previoues score an current score(avg)
   error=error+(dif*dif)

 #  print(error)
 # multiply  .01 for converting error into float
 
 Mean_Squared_Error=(error*1.0)/len(y_val)
 Mean_Squared_Errors[k]=Mean_Squared_Error


minimum_Mean_Squared_Error=Mean_Squared_Errors[1]
minimum_Mean_Squared_Error_k=1
for i in Mean_Squared_Errors:
  if(Mean_Squared_Errors[i]<minimum_Mean_Squared_Error):
    minimum_Mean_Squared_Error=Mean_Squared_Errors[i]
    minimum_Mean_Squared_Error_k=i
# print(Mean_Squared_Errors)
a=Mean_Squared_Errors.keys()
b=Mean_Squared_Errors.values()
# print(b)


df = pd.DataFrame({"K" : a, "Mean_Squared_Errors" : b})


df.to_csv("KvsMean_Squared_Errors.csv", index=False)
import matplotlib.pyplot as plt
x=[]
y=[]
for xx in a:
  x.append(xx)
for yy in b:
  y.append(yy)  


plt.plot(x, y)
plt.xlabel('k')
plt.ylabel('Mean_Squared_Errors')
error=0
for i in range(len(X_test)):
   All_euclidean_dist = []
   for j in range(len(X_train)):
     Eudis = distance.euclidean(X_test[i], X_train[j])
     All_euclidean_dist.append([Eudis, y_train[j] ])
   All_euclidean_dist.sort()
   sum=0
   for pt in range(minimum_Mean_Squared_Error_k):
     sum=sum+All_euclidean_dist[pt][1]
   avg=(sum*1.0)/k
   dif=y_test[i]-avg
   error=error+(dif*dif)

print(error)
Mean_Squared_Error=(error*1.0)/len(y_test)
print(Mean_Squared_Error)