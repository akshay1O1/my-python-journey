
m=[82,82,93,"kaka"]
print(m.count(82))
k=0
print(m[k])
m.insert(2,99)#inserts 99 to the 2nd index
print(m)# prints all the elements in the list
print(99 in m)#checks if the element 99 is present in the list
a=input("enter your subject:")
if a=="maths":
    print("your score is",m[0])
elif a=="physics":
    print("your score is ",m[1])
elif a=="chemistry":
    print("your score is ",m[2])
else:
    print("wrong option")
print(m[0:2])#prints elements from 0th index to 1st index
m.append(85)#adds new element to the end of the list
#printing the entire list 

'''for i in m:
        print(i)'''
for j in range(len(m)):
    print("element no.",j,"is",m[k])#can also use m[j] then no need for increment
    k+=1
c=len(m)
print("length of the string is",c)