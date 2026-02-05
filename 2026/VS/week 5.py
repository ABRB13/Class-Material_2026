# iterative functions 

# def example():

#     #for loops
#     #while loops

# recursive function 

# functions that call themshelves

# recursive functions are infinite loops 

#iterative function 

def walk(steps):
    for step in range(1, steps+1):
        print(f"You took step #{step}")

walk(10)


#recursive function

def walk(steps):
     
     #base case (conditional statement)

     if steps == 0:
         return
     
     #infinite loop 

     print(f"You took step #{steps}") # iter 1 you took step 10, iter 2 = step 9, , step 8, steps = 0
     walk(steps-1)  #iter 1 = walk(9), iter 2 = walk(9-1) = walk(8). walk(8-1) = walk, walk(0-1)


walk(10)


#iterative: faster, complex

#recursive: slow, simpler 

#data structures
# 
# 


def factorial(n):

    result = 1

    for i in range(2, n+1):
        result *= i

    return result

start = time.time()
factorial(5)
end = time.time()

print(end-start)



#recursive 

import time


def factorial(n):
    if n == 1:
        return 1  #base case 
    else:
        return n * factorial(n-1)


start = time.time()
factorial(5)
end = time.time()

print(end-start)