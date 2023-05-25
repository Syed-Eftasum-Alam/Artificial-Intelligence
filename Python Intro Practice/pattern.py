n= int(input("Enter a number: "))
x=int(input("Enter a number: "))

for i in range(n,0,-1):
    for j in range(2*i-1,0,-1):
        print('*',end=" ")
    print()
print()    
print("x=",x)
for i in range(0,n):
    for j in range(2*i,0,-1):
        print("* ",end=" ")
    print()   