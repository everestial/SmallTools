
**Algorithm are means to finding ends to the problem.** While there are several good tutorials in programming I have been little underwhelemed by the available documents that show how a designed algorithm integrates with the programming/coding and how further algorithm optimization are approached to save two most important resources of computer - i.e "computation time" and "memory".

For a newbie the concept of algorithm and it's translation to working code (in any language) can be both exciting and frustrating - I speak this from my experience because I spent most of my life staying as an emperical biologist, then transitioned to bioinformatics as front end user, then jumped to backend bioinformatics application development. Most importantly and frustratingly my ride was solo, navigating only by means of stackoverflow and google.

**Understanding an algorithm and it's translation to code should go hand in hand:**
  - because a working code that solves a problem at hand can never be written without a working algorithm.
  - because it also helps us find "the devil in the details". With the trend of increase in high level programming we adhere by the assumption that the provided "black box" (packages, libraries or even a written code) will work. But, often times it won't; so a perspective of algorithmic details and it's translation into code is always a most for programmer's career.

**Codes for this tutorial can be found at [FindMeAprime](https://github.com/everestial/SmallTools/tree/master/FindAprime) on my GitHub repo.**

<br>

# Tutorial on "Primality Test"
Today, I will talk about a simple mathematical problem - "Test of Primality" i.e if a given natural positive number is a prime or not. Additionally, this test will also provide a "proof of principle" for the test method that utilizes (O(sqrt(N)).

Finding a prime has been one of the challenging mathematical rigor to humans since the time the numbers were invented. And the test of primality has always fascinated us.

**In this tutorial :**
  - I will first take the existing definition of a "prime number" and use it as a base algorithm to write a code in python.
  - Subsequently, I will show how an existing algorithm could be optimized and translated into optimized code to acheive the same result.
  - Additionally, this tutorial has minor goal of showing how "for loop" vs. "while loop" can be used for the same set of problem and why a particular loop becomes more appropriate for a given problem. ***Compare the codes for "level 02 and level 03".***

So, overall we will evolve both in the terms of thinking about an algorithm and and it's translation into workable coding in python.


```
Purpose of the tutorial: 
    - Convert algorithms for primality test to python codes. 
    - Use "for" vs. "while" loop for the same set of problem to understand their differences.
    - Algorithm and code optimization. 
```


**Definition of a prime:**
  - num(x) is prime if "x" is divisible only by 1 and itself. 
  - ***Expressing mathematically,*** 
  $$
  natural\ positive\ number\ "x"\ is\ a\ prime \ if, \\ f\left( x\% n\right) =0 \,, {only \ when}
  \begin{cases}n=1\\ n=x\end{cases}
  $$
  - i.e the number cannot be split into two or more number of positive integers. 
  - So, the given input number has to be divided by 2 to n-1.

<br>

## Level 01 : Primality testing using the simplest algorithm 
We will covert the above definition of prime into an algorithm and python code below.

```python
import sys
import time

my_num = input("input a number: ")
my_num = int(my_num)
print()
print('The input number is %s' %my_num)


# writing a small function to test the primality of the input number
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
            print('Completed primality test.')

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
```

<br>

**Begin test for level 01:**
<pre>
$ python3 FindMeAprime.py 
input a number: 31

The input number is 31

Level 01 primality test.
the input number 31 is a prime
Completed primality test in 5.888938903808594e-05
</pre>

**Result:** We can see that primality test was completed in almost no time.

<br>


## Level 02: Now, let's take algorithm to a next level
Earlier when we tested if a number is a prime or not, we divided the number (x) by all the numbers from **n=2 to n=(x-1)**. To save computation time for the primality test, we can simply divide the number (x) by numbers from **n=2 to n=(x-1)/2**.
    - because if the number isn't divided by 2 it cannot be divided by any integer bigger than (x-1)/2.
    - by reducing the "maximum required divisor" from "x-1" to "(x-1)/2", we just simply reduced the size of the divisor and thus updated our algorithm.


### Now, let's update the above code

```python
def test_primeL2(num):
    set_timer = time.time()
    print()
    print("Level 02 primality test.")
    
    # largest factor to divide the number of interest
    max_factor = round((num-1)/2)
    is_prime = ''  # to store the boolean logic

    # here (in python) the upper limit of the range is n-1
    for nth in range(2, max_factor):
        if num % nth == 0:
            # if a number gets divided into two positive natural numbers
            print('the input number %s is not a prime' % num)
            print('Completed primality test.')

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
```

<br>

**Begin test for both level 01 and level 02 with a large prime number:**
<pre>
$ python3 FindMeAprime.py 
input a number: 145897

The input number is 145897

Level 01 primality test.
the input number 145897 is a prime
Completed primality test in 0.01402425765991211

Level 02 primality test.
the input number 145897 is a prime
Completed primality test in 0.006134748458862305.
</pre>

<br>

<pre>
$ python3 FindMeAprime.py 
input a number: 15487457

The input number is 15487457

Level 01 primality test.
the input number 15487457 is a prime
Completed primality test in 1.3484265804290771

Level 02 primality test.
the input number 15487457 is a prime
Completed primality test in 0.6822659969329834.
</pre>

**Result :** You can see that the optimized algorithm (**test_primeL2()**) actually completes the test in much shorter time. 


<br>
## Level 03: Testing primality using while loop
Now, it's time to see if we can implement the algorithm for the test of primality using "while loop". Also take care of the following points.
  - Coming from a long biological background, I personally found while-loop to be a little difficult to comprehend in the beginning.
  - Another problem with while loop is that if condition isn't handled properly while loops can turn into infinite loop issues.
  - For the test of primality 'while loop' works better, you will see why.


```python
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
```

<br>

**Begin test for primality using both For and While loops:**

<pre>
$ python3 FindMeAprime.py 
input a number: 15487457

The input number is 15487457

Level 01 primality test.
the input number 15487457 is a prime
Completed primality test in 1.303039312362671

Level 02 primality test.
the input number 15487457 is a prime
Completed primality test in 0.6651513576507568.

Primality test using while loop.
the input number 15487457 is a prime
Completed primality test in 0.9351861476898193.

</pre>

**Result :** We can see that optimized "for-loop i.e level 02" was the fastest of all. The same algorithm (Level 02) when implemented in `while loop` was slower compared to when implemented on a `for-loop` method. 
I am not very sure if `while loop` are generally slower, so there is more testing and reading that can be done on this matter.

***But, 'while loop' is a more fitting loop to this problem because down the road we will deal with dynamically reducing the size of the "maximum divisor".***

<br>

**Test for primality using both For and While loops with another large number:**
<pre>
$ python3 FindMeAprime.py 
input a number: 49979591

The input number is 49979591

Level 01 primality test.
the input number 49979591 is a prime
Completed primality test in 4.481180906295776

Level 02 primality test.
the input number 49979591 is a prime
Completed primality test in 2.3850677013397217.

Primality test using while loop.
the input number 49979591 is a prime
Completed primality test in 3.1510345935821533.
</pre>

<br>


## Level 04: Further optimization of the algorithm (using dynamic "max factor" implementation).
Previously, while setting a "max factor" did decrease our computation time, it may not be the fast way to run the primality test if the number in test is very large.
To assist the process we can update our algorithm that would dynamically update the "max factor" as the test progresses.

**Concept behind the updated (dynamic max factor reduction) algorithm :**
  - Previously when the input natural positive number isn't divisible by 2, we reduced the max factor to half of the input number since it couldn't be divided by any number larger than half of it's size.
  - Similarly if the input natural number isn't divisible by 2 and also not divisible by 3 the input number isn't really divisible by any factors less than half it's size and also not divisible by any factor larger than 1/3 its size.
  - So, this provides us with the opportunity to reduce the size of "max factor" as the size of the factor increases.

```python
def test_prime_dmf(num):
    # dmf = dynamic max factor
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
```
<br>

**Now, lets test the primality using "max factor reduction" implementation :**

<pre>
$ python3 FindMeAprime.py 
input a number: 49979591

The input number is 49979591

Level 01 primality test.
the input number 49979591 is a prime
Completed primality test in 4.220755338668823

Level 02 primality test.
the input number 49979591 is a prime
Completed primality test in 2.097686290740967.

Primality test using while loop.
the input number 49979591 is a prime
Completed primality test in 3.07643723487854.

Primality test using dynamic max factor on while loop.
the input number 49979591 is a prime
Completed primality test in 0.0027065277099609375.
</pre>


<br>

**Another test using even larger prime : **

<pre>
python3 FindMeAprime.py
input a number: 573259321

The input number is 573259321

Level 01 primality test.
the input number 573259321 is a prime
Completed primality test in 50.32965445518494

Level 02 primality test.
the input number 573259321 is a prime
Completed primality test in 24.995513439178467.

Primality test using while loop.
the input number 573259321 is a prime
Completed primality test in 35.36520004272461.

Primality test using dynamic max factor on while loop.
the input number 573259321 is a prime
Completed primality test in 0.008965015411376953.
</pre>

**Result :** Wow, you can see that dynamic "max factor reduction" implementation actually reduces the run time significantly.

<br>

## Level 05: Primality test using O(sqrt(N)) implementation
If you take the code from the "dynamic max factor" implementation and activate the line
`print('factor, max factor:', factor, max_factor)`

and test a prime; let's say 49979591 ...

<pre>
$ python3 FindMeAprime.py 
input a number: 49979591

The input number is 49979591

Level 01 primality test.
the input number 49979591 is a prime
Completed primality test in 4.343443870544434

Level 02 primality test.
the input number 49979591 is a prime
Completed primality test in 2.1754212379455566.

Primality test using while loop.
the input number 49979591 is a prime
Completed primality test in 3.0253350734710693.

Primality test using dynamic max factor on while loop.
....................
....................
....................
factor, max factor: 7066 7073
factor, max factor: 7067 7072
factor, max factor: 7068 7071
factor, max factor: 7069 7070
factor, max factor: 7070 7069

the input number 49979591 is a prime
Completed primality test in 0.0029039382934570312.

</pre>

... you can see how the 'factor' and 'max factor' value changes as the test progresses. One thing to note is that the 'factor' is increasing and 'max factor' is decreasing and converging towards the `square root(N)` of the input number.

This shows that for a "primality test" we can set the `max factor` directly at the rounded square root of the input number. - The aaahaaa moment, isn't it !!! :).
Hence the `O(sqrt(N))` test.

<br>
**SourceCode for `O(sqrt(N))` implementation:**
```python
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
```


<br>
**Lets begin some test with Sqrt(N) implementation.**
<pre>
$ python3 FindMeAprime.py 
input a number: 49979591

The input number is 49979591

Level 01 primality test.
the input number 49979591 is a prime
Completed primality test in 4.27828311920166

Level 02 primality test.
the input number 49979591 is a prime
Completed primality test in 2.130234956741333.

Primality test using while loop.
the input number 49979591 is a prime
Completed primality test in 3.227029800415039.

Primality test using dynamic max factor on while loop.
the input number 49979591 is a prime
Completed primality test in 0.003675699234008789.

Primality test using O(sqrt(N)) implementation.
max factor 7070
the input number 49979591 is a prime
Completed primality test in 0.0009083747863769531.
</pre>

<br>

**Another test : **

<pre>
$ python3 FindMeAprime.py 
input a number: 573259321

The input number is 573259321

Level 01 primality test.
the input number 573259321 is a prime
Completed primality test in 50.293437004089355

Level 02 primality test.
the input number 573259321 is a prime
Completed primality test in 24.826218366622925.

Primality test using while loop.
the input number 573259321 is a prime
Completed primality test in 36.55556273460388.

Primality test using dynamic max factor on while loop.
the input number 573259321 is a prime
Completed primality test in 0.00992727279663086.

Primality test using O(sqrt(N)) implementation.
max factor 23943
the input number 573259321 is a prime
Completed primality test in 0.0028390884399414062.
</pre>


**Result :** Wow, the sqrt(N) implementation worked like a flash. 

<br>

# Level 06 : Primality test using ***Sieve of Eratosthenes***
This method is mainly used to find the prime numbers with in a certain range. You can read about the details of the algorithm here [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) and apply it to python. I will add python implementation of this algorithm soon in the future.

**At the mean time you can take the above codes and update it if you can find a prime number within a given range of inputs (say between 101-10001).**


<br>
# Conclusion
**So, in this tutorial we were able to**
  - run a "primality test" using the base algorithm derived from the definiton of "prime number. 
  - update the algorithm and codes to reduce run time significantly.
  - apply the concept of for loop vs. while loop on the same problem and see why a particular loop is more suited.
  - learn algorithm optimization by starting with a simple concept of prime and primality test, then reduce the time for primality test by adding conditional measures.

**Finally, algorithms are simply a measure to find a means to the problem at hand. It is more of an art of finding a pattern to problem solving and adding more refined patterns for runtime and memory optimization.**
