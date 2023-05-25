def function():
    print("Hello World")

def primenumber(x):
    for i in range(2,x):
        if x % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

def OddEven(x):
    if x%2==0:
        print("Even number")
    else:
        print("Odd number")

def StringPalindrome(x):
    if x==x[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


def leapyear(x):
    if x%400==0:
        print("Leap year")
    elif x%4==0 and x%100!=0:
        print("Leap year")    
    else:
        print("Not a leap year")


print ("this is outside the function")
a=int(input("Enter a number: "))
b=input("Enter a string: ")
c=int(input("Enter a year: "))
primenumber(a)
OddEven(a)
StringPalindrome(b)
leapyear(c)