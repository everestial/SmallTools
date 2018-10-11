
import math
import sys

## Let's make a list of prime number from 0-10000

num_range = (2, 10000)

odd_prime_list = [] # create empty list
odd_composite_list = []
min_factor_list = []

count = 0
for num in range(4000, 5000):

    # skip the test of even numbers, numbers ending in 5
    last_digit = list(str(num))[-1]
    if int(last_digit) % 2 == 0 or last_digit == "5":
        continue


    ### now, run the primality test

    # find the maximum possible factor for the current number
    max_factor = round(math.sqrt(num + 1)) + 1
    current_factor = 2

    while current_factor <= max_factor:
        if num % current_factor == 0:
            '''We found a composite number. We append it to the 
            composite list and we break the loop.'''
            odd_composite_list.append(num)
            min_factor_list.append(current_factor)
            break

        else:
            '''The running number wasn't divisible by the current number. 
            We now plan to test it using another higher factor. '''
            current_factor += 1


    '''if the running number wasn't divisible by any numbers upto "max factor" 
    , the variable "min_factors" will remain empty since we didn't find any factors. 
    So, we found a prime number. We append it to the prime list and test the next number. '''

    if current_factor > max_factor:
        odd_prime_list.append(num)
        count += 1


    ## just a break. If we have found 7 prime numbers break the loop
    #if count >= 7:
        #sys.exit()


### now, print the data
print(len(odd_prime_list))
print(odd_prime_list)
print()

print(len(odd_composite_list))
print(odd_composite_list)
print(min_factor_list)







