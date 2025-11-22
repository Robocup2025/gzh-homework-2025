#第三题 数字位数
x=input("输入一个整数：")
lenth=len(x)
print(f"位数是{lenth}")
print("逆序数字为：",x[::-1])

#第四题 回文数
x=input("输入一个整数：")
if x==x[::-1]:
    print("是回文数")
else:
    print("不是回文数")

#第六题 找bug
#问题：删掉后list长度会变
if __name__=="__main__":
    x=list(range(1000))
    jishu=[]
    for m in range(len(x)):
        if x[m]%2==1:
            jishu.append(m)
    for m in reversed(jishu):
        x.pop(m)

#类的继承与魔术方法
class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        def personInfo(self):
            print(f"姓名：{self.name},年龄：{self.age},性别：{self.gender}")
class student(Person):
    def __init__(self,name,gender,age,college,class_):
        super().__init__(name,gender,age)
        self.college=college
        self.class_=class_
    def personInfo(self):
        super().personInfo()
        print(f"学院:{self.college},班级:{self.class_}")
    def __str__(self):
        return f"学生信息：姓名：{self.name},年龄：{self.age},性别：{self.gender}，学院：{self.college},班级：{self.class_}"

#第一题 文件输入
import random
import statistics
f=open("data.txt","w")
for i in range(10):
    n1=random.randint(0,9)
    n2=random.randint(0,9)
    n3=random.randint(0,9)
    f.write(f"{n1},{n2},{n3}\n")
f.close()
x2_list=[]
f=open("data.txt","r")
for line in f:
    x2=int(line[1])
    x2_list.append(x2)
f.close()
print("最大值：",max(x2_list))
print("最小值：",min(x2_list))
print("平均值：",sum(x2_list)/10)
print("中位数：",statistics.median(x2_list))

#第二题 文件复制
import random
lines=int(input(""))
with open("test.txt","w") as f:
    for i in range (lines):
        m=random.randint(32,126)
        char=chr(m)
        f.write(char+"\n")
with open("test.txt","r") as copy,open("copy_test.txt","w") as file:
    file.write(copy.read())

#第三题 文件修改
with open("test.txt","r+")as f:
    content=f.read()
    f.seek(0)
    f.write("python"+content+"python")

#第四题 文件对比
with open("test.txt","r") as f1,open("copy_test.txt","r") as f2:
    line1=f1.readlines()
    line2=f2.readline()
    for n in range(max(len(line1),len(lien2))):
        l1=line1[n].strip()
        l2=line2[n].strip()
        if l1!=l2:
         print(f"第{n+1}行不同") 

#第五题 文件批量创建
import os
import random
import string
os.makedirs("test",exist_ok=True)
num=init(input(""))
for i in range(num):
    fn=f"test/file_{i+1}.txt"
    with open(fn,"w") as f:
        c=random.choice(string.printable.strip())
        f.write(c+"\n")
for fn in os.listdir("teat"):
    op=os.path.join("test",fn)
    if os.path.isfile(op):
        nn=fn.replace(".txt","-python.txt")
        np=os.path.join("test",nn)
        os.rename(op,np)
        with open(np,"r++") as f:
            ls=f.readlines()
            f.seek(0)
            for l in ls:
                f.write(l.strip()+"-python\n")