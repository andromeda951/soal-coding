#         0 1 2 3 4 5
mylist = [1,5,3,6,7,3]

print(mylist)
print(mylist[0])
print(mylist[3])

# range(start,end,step)
# mylist[start:end:step]

print(mylist[0:3])
print(mylist[2:5])

print(mylist[1:7])  # 

print(mylist[3:])
print(mylist[:4])
print(mylist[:])

#         0 1 2 3 4 5
mylist = [1,5,3,6,7,3]
#        -6-5-4-3-2-1

print(mylist[0:4:2])
print(mylist[4::-1])
print(mylist[4:1:-1])
print(mylist[::-1])
print(mylist[::1])
print(mylist[::])

print(mylist[-1])
print(mylist[len(mylist)-1])
print(mylist[-1:-3])
print(mylist[5:1])
print(mylist[5:1:-1])
print(mylist[-1:-3:-1])
print(mylist[-1::-1])
print(mylist[::-1])
print()

#        012345678
mystr = "andromeda"
 
print(mystr[0])
print(mystr[-1])
print(mystr[1:5])
print(mystr[::-1])
print()

for i in mystr:
    print(i)
 
print()
mylist = [1,2,3,4,5]

for i in mylist:
    print(i)
    
for i in mylist[::-1]:
    print(i)








