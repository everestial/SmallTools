
import sys
import time
import math


'''Purpose of the tutorial: 
    - To learn development of algorithms. 
    - To learn how to use for vs. while loop for the same problems and find their use differences. 
    - To learn some coding skills and algorithm optimization. '''


'''Writing a small python program to test if the given input positive natural number is a prime.'''

my_num = input("input a number: ")
my_num = int(my_num)
print()
print('The input number is %s' %my_num)


'''
Definition of a prime: num(x) is prime if x is divisible only by 1 and itself; 
i.e the number cannot be split into two or more number of positive integers. 

So, the given input number has to be divided by 2 to n-1.
'''

def test_prime(num):

    set_timer = time.time()

    print()
    print('Level 01 primality test.')
    is_prime = ''  # to store the boolean logic

    # here (in python) the upper limit of the range is n-1
    for nth in range(2, num):
        if num % nth == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test in %s.' %(time.time() - set_timer))

            # now, update the boolean logic
            is_prime = False

            # and if the input number is found to be a prime at some point
            # .. there is no point in testing it further. So, we can just break the for loop.
            break

    # now, if the boolean logic was not updated in all the divison tests in the above for-loop
    # we know the number is a prime.
    if is_prime == '':
        print('the input number %s is a prime' % num)
        print('Completed primality test in %s' %(time.time() - set_timer))


## Call the function to test the primality.
test_prime(my_num)




## Level 02: Now, let's take algorithm to a next level
'''When we test if a number is prime we don't have to divide the number by numbers 
2 to n-1. We can simply divide the number by numbers from 2 to (n-1/2).
    - because if the number isn't divided by 2 it cannot be divided by any integer bigger than (n-1)/2. 

We will also add a method to track the time required to test the prime.
'''

# now, let's update the above code


def test_primeL2(num):
    set_timer = time.time()
    print()
    print("Level 02 primality test.")
    max_factor = round((num-1)/2)
    is_prime = ''  # to store the boolean logic

    # here (in python) the upper limit of the range is n-1
    for nth in range(2, max_factor):
        if num % nth == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test in %s.' %(time.time() - set_timer))

            # now, update the boolean logic
            is_prime = False

            # and if the input number is found to be a prime at some point
            # .. there is no point in testing it further. So, we can just break the for loop.
            break

    # now, if the boolean logic was not updated in all the divison tests in the above for-loop
    # we know the number is a prime.
    if is_prime == '':
        print('the input number %s is a prime' % num)
        print('Completed primality test in %s.' %(time.time() - set_timer))


## Call the function to test the primality.
test_primeL2(my_num)

time.sleep(2)


## Level 03: Using while-loop
# Coming from a long biological background, I personally found while-loop to be a little difficult to comprehend
# Another problem with while loop is that if not used properly this can lead to infinite loops

def test_prime_W1(num):
    set_timer = time.time()
    print()
    print("Primality test using while loop.")
    max_factor = round((num-1)/2)
    is_prime = ''  # to store the boolean logic

    # instead of using for-loop on a range of numbers ..
    # in while loop we run the loop until a condition is met ..
    # i.e here we start dividing by factor 2 and then increase the factor ..
    # .. by 1 until it becomes equal to "max_factor"
    factor = 2
    while factor != max_factor:
        if num % factor == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test in %s.' %(time.time() - set_timer))

            # update the boolean logic
            is_prime = False

            # break the while loop if condition met
            break

        # update the factor size if above condition isn't met
        factor += 1

    if is_prime == '':
        print('the input number %s is a prime' % num)
        print('Completed primality test in %s.' % (time.time() - set_timer))

## Call the function to test the primality
test_prime_W1(my_num)


## Level 04: Using a dynamic maxfactor
# While setting a max factor did decrease our computation time, it may not be the fast way to ..
# .. run the primality test if the number in test is very large
# To assist the process we can update our algorithm that would dynamically update the "max factor" ..
# .. as the test progresses.

# Updated algorithm concept:
# If the input natural positive number isn't divisible by 2 ..
# .. previously we reduced the max factor to half of the input number since it couldn't be divided ..
# .. by any number larger than half of it's size.
# Similarly if the input isn't divisible by 2 and then again by 3 ..
# .. the input number isn't divisible by any factors less than half it's size and ..
# .. also not divisible by any factor larger than 1/3 its size.
# So, provides us with the opportunity to reduce the size of "max factor" as the size of the ..
# .. factor increases.

def test_prime_dmf(num):
    # *dmf = dynamic max factor
    set_timer = time.time()
    print()
    print("Primality test using dynamic max factor on while loop.")

    # we start with this max factor
    max_factor = round((num-1)/2)

    is_prime = ''  # to store the boolean logic

    factor = 2  # set the initial factor
    while factor <= max_factor:  # we update the condition here to avoid infinite looping
        if num % factor == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test in %s.' %(time.time() - set_timer))

            # update the boolean logic
            is_prime = False

            # break the while loop if condition met
            break

        # update the factor size if above condition isn't met
        factor += 1

        # also reduce the size of the "max factor" if above condition isn't met
        max_factor = round((num-1)/factor)

        #print('factor, max factor:', factor, max_factor)

    if is_prime == '':
        print('the input number %s is a prime' % num)
        print('Completed primality test in %s.' % (time.time() - set_timer))

## Call the function to test the primality
test_prime_dmf(my_num)



## Level 05 : sqrt(N) implementation
def test_primeSqrt(num):
    set_timer = time.time()
    print()
    print("Primality test using O(sqrt(N)) implementation.")
    max_factor = round(math.sqrt(num))
    is_prime = ''  # to store the boolean logic

    #print('max factor', max_factor)

    # instead of using for-loop on a range of numbers ..
    # in while loop we run the loop until a condition is met ..
    # i.e here we start dividing by factor 2 and then increase the factor ..
    # .. by 1 until it becomes equal to "max_factor"
    factor = 2
    while factor <= max_factor:
        if num % factor == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test in %s.' %(time.time() - set_timer))

            # update the boolean logic
            is_prime = False

            # break the while loop if condition met
            break

        # update the factor size if above condition isn't met
        factor += 1

    if is_prime == '':
        print('the input number %s is a prime' % num)
        print('Completed primality test in %s.' % (time.time() - set_timer))

## Call the function to test the primality
test_primeSqrt(my_num)














