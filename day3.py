"""
For loop :
for i in range (5): prints -> 01234
for i in range (1,5): prints-> 1234
for i in range (1,5,2): prints-> 13 #because 3rd digit is steps to jump

While loop:
similar to foor but we have to initialize starting element 
then add condition and to get the initial element keep print above increment

"""
#5 table for loop
for i in range(1,11):
    print("5 *",i,"=",5*i)

n=int(input())
sum=0
for i in range(1,n+1):
   sum+=n
   print(":",sum)
   i+=n

#even only while loop
i=2
while i<=10:
    print(i)
    i+=2

#n=int(input())
sum=0
i=1
while i<=n:
   sum+=n
   print(":",sum)
   i+=1













"""
List:
list uses [] and everything was separated by ,
used to store multiple items in a single variable
it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
it allows duplication. and to check length we use len()
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

"""
to access items list 
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.
[2:5] is used to print ranged data it only print 2 3 4 index items
to check if item is there we use "if" and "in"
"""
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")