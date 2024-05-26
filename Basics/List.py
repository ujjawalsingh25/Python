# list
print("\n------ List ---------")
print('\n')
l1=[12,6,"26",True,"Ujjawal"]
print(l1)
print(type(l1))
print("--------Search----------")

if 6 in l1 or "26" in l1:
    print("Yes")
if 25 not in l1:
    print("No")
print("------index place------------")

print(l1[:5])
print(l1[0:5])
print(l1[0:3])
print(l1[:-2])
print("----for/ condition in list--------------")

l2=[i for i in range(10) if i%2==0]
print(l2)
print("-----sort, reverse, count, index value-------------")

l2.sort()
l2.reverse()
print(l2)
print("index 4: ",l2.index(4))
print("count/no. of occurance of 6: ",l2.count(6))

print("----append, insert--------------")
l2.append(33)
print(l2)
l2.insert(3,13)  # insert 13 at 3rd position
lst=l2
lst[5]=46
print(l2)
print("Same as l2 since no copy: ",lst) # both lst and l2 change so use copy
lst2=l2.copy()  #COPY of list l2 is in lst2
lst2[5]=64
print("Real : ",l2)
print("Copy : ",lst2)

print("----extend, merge list--------------")
l1.extend(l2)
print("Added list l2 in l1 \n and list l1 increase or change: ",l1,"\n")
l3=["New","List", "Added", "L3"]
merge_list=l2+l3
print("New list made with both list \n merged and rest both list are same",merge_list,"\n")

print("--------------------------------------------------")
print("--------------------------------------------------")





