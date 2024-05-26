# Set
'''
Do not contain order
Show or give DISTINCT objects.
Tuple are in ( ) bracket and list in [ ] bracket and Set in { } bracket.
'''

print("--------------Multiple input in Set or in Loop----------")
n1=int(input())
s1=set()
for i in range(n1):
    s1.add(int(input()))
print(s1,type(s1))



s={2,7,2,"Ujjawal",3,"Kumar",'Kumar'}
print("No repetation, no order only Distict object: ",s) 

s1={1,2,3,4,5,6}
s2={2,5,7,8}

print("\n-----Union, Intersection, Difference, ----- \n --------Symmetric_difference {(A U B) - (A ∩ B)} , -------------")

s_diff=s1.difference(s2)
print("Difference (A - B) : ",s_diff)

s_sydiff=s1.symmetric_difference(s2)
print(" Symmetric_difference {(A U B) - (A ∩ B)} :- ",s_sydiff)

s_intersection=s1.intersection(s2)
print("Intersection :",s_intersection)
s1.intersection_update(s2)
print("Intersection of S2 update or added s1 : ",s1,s2)

s_union=s1.union(s2)
print("Union :",s_union)
s1.update(s2)
print("S2 update or added s1 : ",s1,s2)

print("\n--------- IsDisJoint, IsSuperSet, IsSubSet ---------")

is_disjoint=s1.isdisjoint(s2)
print("Isdisjoint (As there is intersection so False) :",is_disjoint)

is_superset=s1.issuperset(s2)
print("is_superset :",is_superset)

is_subset=s1.issubset(s2)
print("is_subset :",is_subset)

print("\n--------- Add, Remove/Discard()---\n ----Remove will throw an error if item is not in set but discard will not show any error---")
s1.add("Ujjawal")
print(s1)
s1.remove("Ujjawal")
print(s1)
s1.discard("Ujjawal")      # Remove will throw an error if item is not in set but discard will not show any error
print(s1)

print("\n--------- POP, DEL, Clear ---------")
s_pop=s1.pop()
print(s_pop)
s1.clear()
del s1


print("----------------- Ques -----------------")

"""print(''' A list of data and we need to find the number that is not repeated 
            Take two set s1 and s2 both empty
           So, start a loop from 0 to last loop and take all no. to s1 first (s2 which was empty)
            Now check of no. already present in s1 then send to s2.
            So, all data of s1 are unique and data of s2 are of list
            Then we use difference to get the no that is not repeated''')


n = int(input())
lst = list(map(int, input().split()))

s1 = set() #unique room no
s2 = set() # room no which repeats more than once

for i in lst:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)

s = s1.difference(s2)
print(*s)

"""
