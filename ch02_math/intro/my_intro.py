# Me trying to develop some python code

import math

def extract_digit(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value = remaining_value // 10
        print(digit, end=" ")
    print()


def extract_digit2(number):
    remain_value = number
    while remain_value > 0:
        remain_value, digit = divmod(remain_value, 10)
        print(digit, end=" ")
    print()

def count_digits(number):
    remaining_value = number
    count = 0
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        #print(remaining_value)
        count += 1

    return count



"""
Understanding the Range:
Start (2)

The loop starts at 2 because 1 is already included in the divisors list.
End (value // 2 + 1)

The loop goes up to value // 2 + 1. This ensures we check all numbers from 2 up to value // 2 as possible divisors.
A number n cannot have any proper divisors greater than n // 2, except itself. For example:
For value = 10, the divisors are 1, 2, 5, and 10. The proper divisors (excluding 10) are 1, 2, 5. The largest proper divisor is 5, which is ≤ 10 // 2.
For value = 20, proper divisors are 1, 2, 4, 5, 10, and the largest (10) is ≤ 20 // 2.
"""

def find_proper_divisors(value):
    divisors = [1]
    for i in range(2, (value // 2) + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors

def find_proper_divisors_lc(value):
    return [i for i in range(1, value//2 + 1) if value%i == 0]



def is_prime(number):
    for i in range(2, number//2 +1):
        if number % i == 0:
            return False
    return True


def printing_primes(limit):
    primes = []
    for i in range(2,limit):
        if is_prime(i):
            primes.append(i)
    return primes


def is_multiple_of(test_num, num):
    """Is "test_num" a multiple of "num" ?

    Args:
        test_num (_type_): the number to check if it's multple of <num>
        num (_type_): the number to check multiples

    Returns:
        _type_: returns True if test_num is a multiple of num
    """
    return test_num % num == 0 


# This was my first try - the time complexity is pretty bad ...
def sieve_of_eratosthenes_v1(limit):
    num_list = [x for x in range(2, limit+1)]
    # print(num_list)
    to_remove = set()

    for i in range(len(num_list)):
        for num in num_list[i+1:]:
            if is_multiple_of(num,num_list[i]):
                to_remove.add(num)

    # print(to_remove)
    # x = [x for x in num_list if x not in to_remove]
    return [x for x in num_list if x not in to_remove]


# def sieve_of_eratosthenes(limit):
#     list_num = [x for x in range(2,limit+1)]
#     print(list_num)
#     print("len(list_num): ",len(list_num))
#     test_list = [True for x in range(2,limit+1)]
#     test_limit =  math.trunc(math.sqrt(limit)) # Ex: sqrt(15) = 3,84 --> = 3
#     print("test_limit:",test_limit)

#     for i in range(2,math.trunc(math.sqrt(limit)+1)):
#         print("n: ", i)
#         if test_list[i-2]:
#             for j in range(limit+1):
#                 print("j: ", j)
#                 k = i*i + j*i
#                 if k < limit:
#                     print(k)
#                     test_list[k-2] = False
        
#     print(test_list)
#     return [i for i in range(2,len(test_list)) if test_list[i-2] == True]


def sieve_of_eratosthenes_me(n):
    test_list = [True] * (n+1) # [0,1,2,...,n+1] -> contains all the numbers in n
    test_list[0] = test_list[1] = False # 0 and 1 are never prime numbers

    # NOTE: Numbers can only be primes until sqrt(n) ... after that they can't be primes
    for i in range(2, int(math.sqrt(n)+1)):
        if test_list[i]: # if it's still true, then it must be a prime
            for j in range(i*i, n+1, i): # Start with power of i which we already know it's the lowest, then we keep adding into all the multiples of i
                test_list[j] = False

    return [i for i, is_prime in enumerate(test_list) if is_prime]


"""
GPT optimized
"""

def sieve_of_eratosthenes(n):
    test_list = [True] * (n+1) # Boolean array for prime numbers
    print(len(test_list))
    print(test_list)
    test_list[0] = test_list[1] = False # 0 and 1 are not numbers

    for i in range(2, int(math.sqrt(n) + 1)): # primes can only be up to sqrt(n)
        if test_list[i]: # If it's stil true, it's a prime
            for k in range(i*i, n+1, i): # Start from i^2 and step by i
                test_list[k] = False # Mark multiples of i as non-prime
    
    # Extracting prime numbers for return

    return [i for i, is_prime in enumerate(test_list) if is_prime]


        

        


def main():
    # extract_digit(223344)
    # extract_digit2(33123)
    # print(count_digits(275876543))
    # print(find_proper_divisors_lc(972))
    # print(972//2)
    # print(printing_primes(25))
    # print(sieve_of_eratosthenes(25))
    #print(sieve_of_eratosthenes(25))
    print(sieve_of_eratosthenes_me(50))
    # print(is_multiple_of(4, 2))

if __name__ == "__main__":
    main()