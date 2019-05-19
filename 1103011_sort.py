## Merge and Sort 2 list
 
#list1 = [8,1,5,3,4]
#list2 = [12,7,15,11]

list1 = []
list2 = []
list3 = []

num1= int(input("Enter the size for List 1:"))

for x in range(num1):
    num1= input("Enter Numbers for List 1: ")
    list1.append(num1)
    
num2= int(input("Enter the size for List 2:"))
    
for x in range(num2):
    num2= input("Enter Numbers for List 2: ")
    list2.append(num2)
    
list3 = list1 + list2
 
list3.sort(key=int)

print("Sorted List=",list3)