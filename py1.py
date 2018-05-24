import py2
import sys
a = "fdsfds"
print(a)
b = range(0, 10, 2)
print(b)
c = ["google", "baidu", "biying", "apple"]
print(c)
print(c[1:3])
c[1] = "new one"
print(c)
del c[1]
print(c)
print(len(c))
if "apple" in c:
    for x in c:print(x)
print("if expression is end!!!!!!!!!!!!!!!!!!!!")
print(max(c))
c.append("overflowstack")
print(c)
print(c.count("apple"))
c.extend([1,2,3])
print(c)
tuple1 = ("tuple1", "tuple2", "tuple3")
print(type(tuple1))
print(tuple1)
print("rang is start:")
for i in range(1,11,2):
    print(i)
print("rang is end!!!!!!!!!!!!!!!!!!!!!!!")
for letter in "Runoob":
    if letter == "o":
        pass
        print("execute pass module")
    print("current sparacter is: ", letter)
print("test of pass module is end!!!!!!!!!!")
py2.moduleTest("This is module test code!")
print(sys.argv)
print(sys.path)