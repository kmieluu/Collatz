#The number we will perform Collatz operation on
n = int(input("Enter a positive integer: "))

#Keep looping untill we reach 1
#Note: this assumes the Collatz conjecture is true.

while n != 1:
    #Print the current value of n
    print(n)
    #Check if n is even
    if n % 2 == 0:
        #If n is even divide it by 2
        n = n // 2
    else:
        #if n is odd multiply by 3 and add 1
        n = n * 3 + 1
        
#Finally print n
print(n)

