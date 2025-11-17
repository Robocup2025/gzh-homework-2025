#第一题
i=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and b != c and a !=c:
                number=a*100+b*10+c
                print(number)
                i=i+1
print(f"数字1,2,3,4能组成{i}个不同的三位数")

#第二题
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
list=[x,y,z]
list.sort()
print(f"{list[0]},{list[1]},{list[2]}")

#第三题
def a(n):
    a=[1,1]
    while len(a)<n:
        a.append(a[-1]+a[-2])
    return a
print("前二十项为：",a(20))

#第四题
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()