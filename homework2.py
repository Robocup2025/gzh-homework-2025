#Q1
s=input("input:")
letters=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        letters=letters+1
    elif c.isspace():
        space=space+1
    elif c.isdigit():
        digit=digit+1
    else:
        others=others+1
print(f"letters:{letters}")
print(f"space:{space}")
print(f"digit:{digit}")
print(f"others:{others}")

#Q2
a=int(input("input 1:"))
b=int(input("input 2:"))
result=0
i=0
x=0
for i in range(b):
    x=x+a*pow(10,i)
    result=result+x
    i=i+1
print(f"{result}") 

#Q3
i=1
s=100
h=100
for i in range(9):
    h=h/2
    s=s+2*h
    i=i+1
print(f"{s}")
print(f"{h/2}")

#Q4
for x in range(100,1000):
    x1=x//100
    x2=(x-100*x1)//10
    x3=x-100*x1-10*x2
    if x==x1**3+x2**3+x3**3:
        print(x)

#Q5
for x in range(101,201):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x)