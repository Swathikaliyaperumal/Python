#1.Count word frequency:
##a="hello welcome to hello world your to welcome hello world"
##spl=a.split()
##dic={}
##for i in spl:
##    b=spl.count(i)
##    dic.update({i:b})
##print(dic)

#2.Unique Values:
##a={"a":1,"b":2,"c":3,"d":4,"e":2,"f":3}
##b=a.values()
##c=set(b)
##print(c)

#3.Default dict:
##a={'a','b','c'}
##b=0
##dic=dict.fromkeys(a,b)
##print(dic)

#4.Dictionary of list:
##dic={"Tamil":[56,78,54,89],"English":[45,89,79,91],"Maths":[32,65,48,67],"Science":[93,67,80,48]}
##a=[]
##b=[]
##key=[]
##c={}
##avg=0
##for i in dic:
##    a.append(dic[i])
##    key.append(i)
##for i in range(len(a)):
##    add=0
##    for j in range(len(a)):
##        val=a[i][j]
##        add+=val
##        if j==len(a):
##            break
##    avg=round(add/len(a))
##    b.append(avg)
##for i in range(len(a)):
##    c.update({key[i]:b[i]})
##print(c)

#5.Key removal:
##a={"a":1,"b":2,"c":3,"d":4}
##b=a.values()
##print(b)

#6.Key-value swap with conditions:
##dic={1:15,2:16,3:24,4:45}
##a=0
##b=0
##c={}
##for i in dic:
##    a=i
##    b=dic[i]
##    if a%2==0:
##        c.update({b:a})
##print(c)

#7.Find min and max:
##a={"a":41,"b":24,"c":3,"d":45}
##b=[]
##for i in a:
##    for j in i:
##        b.append(a[i])
##b.sort()
##print("min value: ",b[0])
##print("max value: ",b[-1])

#8.Group by keys:
##key=("a","b","c","d")
##val=(5,6,7,8)
##a=0
##for i in key:
##    for j in i:
##        print(i,":",val[a])
##        a+=1

#9.Intersection of dictionaries:
##a={'a':1,'b':2,'c':3,'d':4}
##b={'f':5,'g':6,'c':3,'h':7,'b':2}
##dic={}
##c=a.items()
##d=b.items()
##for i in c:
##    for j in d:
##        if i==j:
##            print(i)

#10.Dynamic input:


#1.Create and access a dictionary:
##dic={"Ram":"A","Sam":"C","anu":"A"}
##x=dic.get("Sam")
##print(x)

#2.Update an add elements:
##dic["sham"]="D"
##dic.update({"Sam":"B"})
##print(dic)

#3.Delete elements:
##dic.pop("sham")
##print(dic)
##dic.clear()
##print(dic)

#4.Iterate over a dictionary:
##item=dic.items()
##for i in item:
##    print(i)

#5.Key value operation:
##print(dic.keys())
##print(dic.values())

#6.Check for a key:
##dic={"Ram":"A","Sam":"C","anu":"A"}
##if "Sam" in dic:
##    print("Exist")
##else:
##    print("Not exist")

#7.Nested Dictionary:
##student={
##"Sam":{"age":23,"grade":"A"},
##"Ram":{"age":25,"grade":"C"},
##"Somu":{"age":24,"grade":"B"}
##}
##print(student.get("Sam"))

#8.Dictionary from list:
##name=["Sam","Ram","Somu"]
##grade=["A","C","B"]
##dic={}
##for i in range(len(name)):
##    dic.update({name[i]:grade[i]})
##print(dic)

#9.Frequency count:
##a="hello world"
##b=[]
##cot={}
##dic={}
##for i in a:
##    b.append(i)
##for i in b:
##    cot=b.count(i)
##    dic.update({i:cot})
##print(dic)

#10.Dictionary comprehension:
##a={i:i**2 for i in range(1,11)}
##print(a)

#11.Merge dictionary:
##dic1={"a":1,"b":2,"c":3}
##dic2={"d":4,"e":5,"a":6}
##dic={**dic1,**dic2}
##print(dic)

#12.sort a dictionary:
##a={'red':2,'yellow':4,'orange':5,'pink':9}
##b=list(a.items())
##b.sort()
##print(b)

#13.Default values:
##a={'red':2,'yellow':4,'orange':5,'pink':9}
##print(a.get("black",6))

#14.Reverse a dictionary:
##dic={"a":1,"b":2,"c":3}
##a=0
##b=0
##c={}
##for i in dic:
##    a=i
##    b=dic[i]
##    c.update({b:a})
##print(c)

15.Custom application:
##a={'red':2,'yellow':4,'orange':5,'pink':9}
##print("1. Add")
##print("2. Remove")
##print("3. Update")
##num=int(input("Enter number: "))
##if num==1:
##    a.update()















