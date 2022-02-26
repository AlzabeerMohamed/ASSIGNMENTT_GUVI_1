#1.Python program to check whether the given number is even or not
N=int(input())

if N==0:
    print('zero')
elif N%2 == 0:
    print('even')
else:
    print('odd')
    
 #2.Python program to convert the temperature in degree centigrade to Fahrenheit.
Cel=float(input())
Frh=(Cel*1.8)+32
print("%.2f"%Frh)


#3.Python program to find the product of a set of real numbersN=1
realno=int(input())
for i in range(realno):
    N=N*(i+1)
print(N)

#4.Python program to find the factorial of a number using recursion
N = int(input())
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
result = factorial(userInput)
print(result)


#5.Python program to implement linear search.
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr=[1,2,3,4,5,6,7,8]
x=8
print(search(arr,x))
#6.Python program to implement Binary search.
r=[1,2,3,4,5]
y=5

def binary(arr,l,z,y):
    if z>=l:
        mid = l+(z-l)//2
        if arr[mid]==y:
            return mid
        elif arr[mid] > y:
            return binary(arr,l,mid-1,y)
        else:
            return binary(arr,mid+1,z,y)
    else:
        return -1
result=binary(arr,0,len(arr)-1,y)
if result != -1:
    print(result)
else:
    print("Element is not present in array")
    
#7.Python program to find the largest number in a list without using built-in functions
arr=[10,30,20]
maxi=arr[0]

for i in arr:
    if i>maxi:
        maxi = i
print(maxi)

#8.Python program to delete an element from a list by index.
N=[10,30,20,4,5,6,7]
index = int(input())
N.pop(index)
print(N)

#9.Python program to print all the items in a dictionary.

CLASS = {
    "Ram" : 56,
    "Rose": 23,
    "Rob"  : 43,
}
# Iterate over all values of a dictionary 
# and print them one by one
for value in CLASS.values():
    print(value)
    
#10.Python program to find the average of 10 numbers using while loop.
n = 20
total_numbers = n
sum = 0
while n >= 0:
    sum += n
    n -= 1

average = sum / total_numbers
print("Average = ", average)
