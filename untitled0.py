#factorial no
n=int(input("enter no "))
i=1
r=1
while(i<=n):
    r=r*i        
    i=i+1
print("factorial is",r)

#armstrong no
n=int(input("enter any no"))
number=n
cube=0
while(n>0):
    remainder=n%10
    cube+=remainder*remainder*remainder
    n=n//10
if(number==cube):
    print("armstrong no")
else:
    print("not a armstrong no")
    

for x in range(1,6):
    print(x)
    end=" "
for y in range(10,1,-1):
    print(y)
    end=" "
for z in range(1,6):
    print(z*z)
    end=" "

for x in range(1,1):
    print(x)