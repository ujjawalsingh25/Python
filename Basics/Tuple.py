# Tuple
'''
Tuple are in ( ) bracket and list in [ ] bracket and Set in { } bracket.
Tuple do not change directly (immutable) 
but can be done by typecasting it to list.
'''

print("\n ------ Append, POP ------ ")
t1=(12,3,1,"Kolkata")
# t1.append(4)          """ Error as Tuple cannot change or modify (do not follow operation) """  
t2=list(t1)
t2.append(4)
print(t2)
t2.pop(2)
t2[2]="Salt Lake"
print(t2)

print("\n ------ Merge tuple ------ ")
tp2=(25,3,"Techno")
merge_tuple=t1+tp2                   # merge both tuple in a new tuple
print("Merge tuple: ",merge_tuple)

print("\n ------ Count,Index Length ------ ")
c1=merge_tuple.count(3)
print("Count or occurance of no 3: ",c1)
i1=merge_tuple.index(3)
print("Index 3: ",i1)
len1=len(merge_tuple)
print("Length of merge tuple: ",len1)

print("\n ---------INDEX within a range in Tuple------ ")
i2=merge_tuple.index(3,1,6)   # show the index position of first occurance of 3 in range of index 1 to index 6
print("Index position of first occurance of 3 \n in range of index 1 to 6",i2)


