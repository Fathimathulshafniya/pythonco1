#generate positive list of numbers

list=[-1,-2,0,3,7]
newlist=[x for x in list if x>0]
print("positive numbers are:", newlist)

# square of N numbers

N=int(input("enter number of items:"))
list=[]
for x in range(N):
    x=int(input("enter the numbers:"))
    list.append(x)
print("N numbers are: " , list)
squarelist=[x**2 for x in list]
print("The square of N numbers are: ", squarelist)

#form a list of vowels selected from the list

word="tiger"
vowels="aeiou"
list=[x for x in word if x in vowels]
print("Vowels :",list)

#list ordinal values of each element

word="lion"
list=[ord(x) for x in word]
print("Ordinal value:", list)
