str1 = "mango"
str2 = "apple"
a= list(str1)
b= list(str2)
temp = a[1]
a[1] = b[1]
b[1] = temp
print("Before exchanging elements:", str1, str2)

print("string after exchanging charecter at position 1:", "".join(a), "".join(b))
