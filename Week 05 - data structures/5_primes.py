# A program to generate prime numbers and append them to a list called primes.
# and then print the output
# Author: Jon Ishaque

#initiate list
primes =[]
 
#set the maximum value the program will generate primes to
upto = 100000

#every number between 3 and 99999 is a candidate
#interate through the range 3-99999 
for candidate in range(2, upto):
    #default boolean the number is prime. As soon as it is determined to be false we will exit the loop.
 
    isPrime=True
    #test for prime
    #only check if divisible by prime
    #print("here",primes)
    exit
    for divisor in primes: #initially primes is empty, but 2 % ==0

        #this nested loop will take increasingly longer as the primes list increases in length
        #if divisible by a prime then not prime
        if (candidate % divisor==0):
            #set to isPrime to false and exit loop
            isPrime=False
            break

    if isPrime:
    #append to primes
        primes.append(candidate)

#print prime numbers
print(primes)