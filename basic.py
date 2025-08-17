print("souvik")

## opertion
a=7
b=9
sum=(a+b)
print(sum)

diff=(a-b)
print(diff)

print(a//b)
print(a**b)

#if else

age=int(input("enter number:"))
if age<18:
    print("minor")
elif age >= 18:
     print("adult")
elif age<=50:
     print("senior")

else:
     print("you know")

loop 

for i in range (7):
     print(i)

for i in range(0,4):
    print(i)


# while loop
i=0
while(i<=5):
     print("souvik", i)
     i+=1
#list && tuple 
fruits = ["apple", "banana", "mango"]
print(fruits[0])    
print(fruits[-1])  

fruits[1]="orange"
print(fruits)

fruits.append("grape")
print(fruits)

fruits.pop(2)
print(fruits)

print(len(fruits))
print(fruits)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   
print(numbers[:3])    
print(numbers[2:])    