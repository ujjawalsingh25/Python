

a="Ujjawal"
b='Singh'
print(a[0])
print(a[3])
print(b[3])

# Multiple line print
print(''' Hello
    world '''+a)

# Length of string 
l1=len(a+b)
print(l1)


# Slicing
print("\n Slicing")
print(a[4:7])
print(b[0:3])           # Same as both start 
print(b[:3])            # from 0 (by default)

print("\n Slicing from lenght(len)")
print(b[0:-3])          # takes -3 from back or {len(b)-3 = 2} so it will be length - number.
print(b[0:len(b)-3])          # so both data is same.

print("\n Negative Slicing")
print(b[-4:-1])          # takes -3 from back or {len(b)-3 = 2} so it will be length - number.
print(b[1:4])





"""
--------------
 Immutable String (that do not change)
--------------------------


x="Ujjawal"
y="Singh"

# Upper & Lower Case
print("\nUpper & Lower Case")
print(x.upper())
print(y.lower())

# R/L Strip & Replace
z="***R/L Strip & Replace ****"
print(z.rstrip("*"))
print(z.lstrip("*"))
print(z.lstrip("*"))

print(z.replace("*","-"))
print(z.replace("Replace","Replaced, done"))

# Split (List the data)
print(z.split(" "))
print(z.split("e"))     # All 'e' will replaced with ',' or before and after 'e' there will be lists.
"""