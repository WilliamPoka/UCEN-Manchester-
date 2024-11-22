#Factorial YEYYEYEYEY
def factorial(n):
    result = 1  
    for i in range(1, n + 1):  
        result *= i  
    return result  
 #hippity hoppwewe
num = int(input("Enter a non-negative integer: "))  
 #
while num < 0:
    print("Please enter a non-negative integer.")  
    num = int(input("Enter a non-negative integer: "))  
 
# Loop through numbers from 1 to the input number
for i in range(1, num + 1):  
    fact = factorial(i)  
    print(f"{i}:{fact}")  
    #this assignment hurt my brain man