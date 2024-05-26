'''
for i in range(1,3):
    if i==3:
        continue
    elif i==7:
        break
    print (i)
'''


def maximum(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return ("Equal \n")

def cube(a,b):
    # if maximum(a,b)=="Equal":
    #     return (a**3)
    # else:
    #     return (maximum(a,b)**3)
    m=maximum(a,b)
    if m=="Equal":
        return a**3
    else:
        return m**3

x=int(input("Enter a: "))
y=int(input("Enter b: "))

print("Max_term : ",maximum(x,y))
print("Cube_Max_term : ",cube(x,y))



