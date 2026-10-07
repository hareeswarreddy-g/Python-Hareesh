a = int(input())
#b = int(input())

#print("Addition",a+b)
#print("sub:",a-b)
#print("multiplication:",a*b)
#print("div:",a/b)
#print("rem:",a%b)

#elephant problem from codeforces
print((a + 4) // 5)

    
# Read the two weights from standard input
a, b = map(int, input().split())

years = 0

# Keep simulating years as long as Limak is not strictly heavier than Bob
while a <= b:
    a *= 3 
    b *= 2  
    years += 1

print(years)