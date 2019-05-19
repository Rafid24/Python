##Odd_Even Number Sorted in list

##List = [1,2,3,4,5,6]

list=[]
oddlist=[]
evenlist=[]

n=int(input("Enter the size for List:"))

print("Enter number for List:")

for i in range(0,n):
        number=input()
        list.append(int(number))
        
print("List=",list)

for i in range(0,n):
        if(list[i]%2==0):
                evenlist.append(list[i])
        else:
                oddlist.append(list[i])
                
print("OddList=",oddlist)

print("EvenList=",evenlist)
