#        0    1   2   3   4
nums = [100, 90, 85, 50, 95]

print(nums)
print(nums[0])
print(nums[4])
# print(nums[5])
print()

# inisialisasi semua index list dengan nilai 0
mylist = []
for i in range(10):
    mylist.append(i*10)
    
print(mylist)

# cetak semua nilai list
for i in range(9,-1,-1):
    print(mylist[i])

print()


# inisialisasi semua element list dengan pembacaan pada input
# mylist = []
# for i in range(5):
#     x = int(input("masukan element list: "))
#     mylist.append(x)
    
# print(mylist)


# jumlah element list sebanyak n
mylist = [2, 7, 1, 5, 5, 8]
total = 0
for i in range(len(mylist)):
    total += mylist[i]
    
print("total=", total)
print("leght=", len(mylist))
print("avg=", total/len(mylist))
print()

mylist = [1,2,3]
print("length=", len(mylist))
# print(mylist[5]) # IndexError: list index out of range

mylist.append(100)
print(mylist)
print("new length=", len(mylist))