first = "Hareesh"
#print("Hi! my name is",first)
bool = bool(first)
print(bool)

first_name = 'Hareesh'
First_name = 'Rohitha'
print("my name is", first_name)
# "%" is used for reminder
# "/" is used for quocient with decimals
# "//" is used for quocient without decimals
# "**" is used for power values

a=20
if (a<=30 and a>=15):
    print("correct")
else:
    print("not correct")

# Assignment operator???????
# =,+=,*=,/=
#usr1 = int(input())
#usr2 = int(input())

#print(usr1 and usr2)
#print(usr1 or usr2)
#print(usr1 | usr2)
#print(not usr1)

#bitwise
a = 17>>2
print(a)
# Swaping
A=10
B=12
print(A,B)
(A,B)=(B,A)
print(A,B)

#l= int(input())
#b= int(input())
#r= int(input())
c = int (input())
f = (c * 9/5) + 32
#print("Area of Square=",l*l)
#print("area of rectangle=",b*l)
#print("area of circle",(3.14)*r**2)
#print(f"fahrenheit is {f} 'f")

p= int(input("Enter principal amount:"))
t= int(input("Enter in months:"))
r= int(input("Enter the rate:"))
i=(p*t*r)/100
#print("simple intrest is:",i)

m = int(input())
hr = m//60
min = m%60
#print(f"{hr}hrs {min} mins")

if(m%2==0):
    print("Even")
else:
    print("Odd")


#learn square problem
class Solution:
    def calculateRectangleProperties(self, length, breadth):
        if length <= 0 or breadth <= 0:
            return "Invalid Dimensions"

        area = length * breadth
        perimeter = 2 * (length + breadth)

        return f"Area {area:.1f} Perimeter {perimeter:.1f}"


a = int(input())
b = int(input())
c = int(input())
if (a>b and a>c):
    print(f"{a} is largest")
elif (b>a and b>c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest")


marks=int(input())
if(marks>90):
    print("A")

#bit++
n = int(input())
x = 0

for _ in range(n):
    statement = input()
    if '+' in statement:
        x += 1
    else:
        x -= 1

print(x)