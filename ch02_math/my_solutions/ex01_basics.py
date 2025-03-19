
#Exercise 1 a)
def calc(m:int,n:int):
    return ((m*n)//2)%7


#Exercise 1 b)
def count_all_numbers_div_by_2_or_7(max_exclusive):
    sum = 0
    nr_div_numbers = 0
    for num in range(1,max_exclusive):
        if num % 2 == 0 or num % 7 == 0:
            sum += num
            nr_div_numbers += 1
    # return (nr_div_numbers, sum)
    print("count:", nr_div_numbers)
    print("sum: ", sum)
    


#Exercise 1 c)
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return  not n % 2 == 0


#Exercise 2
def number_as_text(n):
    num_to_text = {
        0:"ZERO",
        1:"ONE",
        2:"TWO",
        3:"THREE",
        4:"FOUR",
        5:"FIVE",
        6:"SIX",
        7:"SEVEN",
        8:"EIGHT",
        9:"NINE",
    }

    value_to_text = ""
    while n > 0:
        remainder = n%10
        n = n // 10
        value_to_text = num_to_text[remainder] + " " + value_to_text
    
    return value_to_text


#Exercise 3

# Function that finds all divisors non inclusive of the num (all the nums are divisible by themselves)
def find_all_divisors(num):
    divisors = []
    test_num=num
    while test_num>1:
        test_num = test_num - 1
        #print(start)
        if num % test_num == 0:
            divisors.append(test_num)
    return divisors


# Highly optimized function that really finds all divisors (but it's not useful for this exercise)
# def find_all_divisors(num):
#     divisors = []
#     for i in range(1,int((num**0.5))+1):
#         if num % i == 0:
#             divisors.append(i)
#             if i != num//i:
#                 #print("i: ",i)
#                 #print("num//i: ", num//i)
#                 divisors.append(num//i)
#     #print("order they were added: ",divisors)
#     return sorted(divisors)


def calc_perfect_numbers(max_exclusive):
    perf_numbers = []

    for num in range(1,max_exclusive):
        if sum(find_all_divisors(num)) == num:
            perf_numbers.append(num)
    
    return perf_numbers


#Exercise 4
"""
Prime numbers are numbers that are exclusively divisible by themselves and by 1
Since I already developed the sieve of eratosthenes before starting the exercise part of the book I can
use the same approach for this function.

The sieve of eratosthenes removes all prime numbers that are multiples of the first prime numbers that appear in the normal order:
    - The first prime after 1 is 2, so the sieve of eratosthenes removes all multiples of 2 upwards
    - The second prime after 2 that is not removed by the first iteration of the sieve of eratosthenes is 3, the algorithm then removes
    all the multiples of 3 up to the max_number decided 
    - The algorithm executes until the sqrt(max_number), this because the biggest prime number under max_number is sqrt(max_number)
"""
def calc_primes_up_to(max_value):
    check_primes = [True]*(max_value+1)
    check_primes[0] = check_primes[1] = False
    #print("max_value: ", max_value) # For sanity checks
    #print("len(check_primes): ",len(check_primes)) # For sanity checks
    #print(check_primes) # For sanity checks
    #print(int(max_value**0.5)+1) # For sanity checks
    for i in range(2,int(max_value**0.5)+1): # loop with i from [2,sqrt(max_value)] (I didn't want to use math.sqrt())
        #print(i) # For sanity checks
        #print(i*i) # For sanity checks
        #print(max_value+1) # For sanity checks
        for j in range(i*i,max_value+1,i):
            #print(j) # For sanity checks
            #print("check_primes[j]: ",check_primes[j]) # For sanity checks
            if j % i == 0:
                check_primes[j] = False
                #print(check_primes[j]) # For sanity checks
        
    # print(check_primes) # For sanity checks
    
    return [i for i, is_prime in enumerate(check_primes) if is_prime]



#Exercise 5 Prime Number Pairs

"""Compute all pairs of prime numbers with a distance of 2 (twin), 4 (cousin), and 6 (sexy)
up to an upper bound for n. For twins then the following is true:
is_Prime(n) && is_Prime(n + 2) """

# for twins --> is_Prime(n) && is_Prime(n + 2)
# for cousins --> is_Prime(n) && is_Prime(n + 4)
# for sexy --> is_Prime(n) && is_Prime(n + 6)

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def prime_number_pairs(type,max_number):
    type_factor = {
        "twin": 2,
        "cousin": 4,
        "sexy": 6
    }

    factor = type_factor[type]
    print("factor: ",factor)


    primes = calc_primes_up_to(max_number)
    prime_number_pairs = []

    for i in range(len(primes)):
        if primes[i] + factor in primes:
            prime_number_pairs.append((primes[i],primes[i]+factor))
    
    return prime_number_pairs



#Exercise 6 Checksum (important for bankcard register and more)
import time

def calc_checksum(digits:str):
    if not digits.isdigit():
        raise ValueError("illegal chars: not only digits")
    
    sum = 0

    for i, curr_char in enumerate(digits):
        value = (int(curr_char))*(i+1)
        sum += value

    return int(sum%10)


#Exercise 7 a) from Roman Numbers -> Decimal Numbers

def from_roman_number(roman_number:str):
    roman_nums_code = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    sum = 0
    #print(roman_number[1+1])
    #print(type(roman_number[1+1]))
    #print(roman_nums_code["X"])
    for i,char in enumerate(roman_number):
        if i == len(roman_number)-1:
            sum += roman_nums_code[char]
        else:
            if roman_nums_code[char] >= roman_nums_code[roman_number[i+1]]:
                sum += roman_nums_code[char]
            else:
                sum += roman_nums_code[char]*-1
    return sum



def to_roman_number(value:int):
    int_to_roman_digit_map = {
        1:"I",
        5:"V",
        10:"X",
        100:"C",
        500:"D",
        1000:"M"
    }

    result = ""
    remainder = value

    for i in sorted(int_to_roman_digit_map.keys(), reverse=True):
        multiplier = i
        roman_digit = int_to_roman_digit_map[i]

        times =  remainder // multiplier
        remainder = remainder % multiplier

        result += roman_digit * times


    return result


#Exercise 8 Combinatorics

# a) Computation of a² + b² = c²

# This has time complexity of O(n³)
def solve_quadratic_simple():
    comb_nums=[]
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if a*a + b*b == c*c:
                    comb_nums.append((a,b,c))
    
    return sorted(comb_nums)

# Making the same implementation O(n²)
import math
import time
def solve_quadratic_optimized():
    comb_nums = []
    for a in range(1,100):
        for b in range(1,100):
            c = int(math.sqrt(a*a +b*b))
            if a*a + b*b == c*c and c<100:
                comb_nums.append((a,b,c))
                
     
    return sorted(comb_nums)

        
# b) Computation of a² + b² = c² + d²
def solve_cubic():
    comb_nums = []
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                under_sqrt = a*a + b*b - c*c
                if under_sqrt > 0:
                    d = int(math.sqrt(under_sqrt))
                    if d < 100 and a*a + b*b == c*c + d*d:
                        comb_nums.append((a,b,c,d))
    
    return comb_nums

# Exercise 9 Armstrong numbers
"""
Three-digit Armstrong numbers
these are ---> numbers for whose digits x, y, and z from 1 to 9 satisfy the following equation:
    x*100 + y*10 + z = x³ + y³ + z³

You should write a function calc_armstrong_numbers() to compute all Armstrong numbers for x, y and z (each < 10)
"""

def calc_armstrong_numbers():
    armstrong_numbers = []
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                if x*100 + y*10 + z == x*x*x + y*y*y + z*z*z:
                    number = x*100 + y*10 + z
                    armstrong_numbers.append(number)
    return armstrong_numbers



#Exercise 10 Max Change Calculator (level 4)
"""
Suppose you have a collection of coins or numbers of different values. Write function
calc_max_possible_change(values) that determines, for positive integers, what
amounts can be seamlessly generated with it starting from the value 1. The maximum
value should be returned as a result.
"""
def calc_max_possible_change(values):
    # we should wrap/copy the original values to another variable so we don't change it
    sorted_numbers = list(values)
    #print(sorted_numbers)
    sorted_numbers.sort()

    max_possible_change = 0

    for current_value in sorted_numbers:
        if current_value > max_possible_change + 1:
            break
        max_possible_change += current_value
    
    return max_possible_change


#Exercise 11 Related Numbers

"""
Two numbers n1 and n2 are called friends (or related) if the sum of their divisors is equal
to the other number:
                        sum(divisors(n1))=n2
                        sum(divisors(n2))=n1
"""

def divisors(num):
    divs = []
    divs.append(1)
    for i in range(2,int(num//2)+1):
        if num % i == 0:
            divs.append(i)
    # if num != 1:
    #     divs.append(num)
    return divs
        


def calc_friends(max_exclusive):
    friends_nums = []
    for n1 in range(1,max_exclusive):
        for n2 in range(1,max_exclusive):
            if sum(divisors(n1)) == n2:
                friends_nums.append((n1,n2))
    
    return friends_nums



def main():
    # # Testing Exercise 1 a)
    # print(calc(5,5))

    # # Testing Exercise 1 b)
    # # Returning a tuple (better imo)
    # print(count_all_numbers_div_by_2_or_7(3))
    # print(count_all_numbers_div_by_2_or_7(8))
    # print(count_all_numbers_div_by_2_or_7(15))
    # count_all_numbers_div_by_2_or_7(3)
    # count_all_numbers_div_by_2_or_7(8)
    # count_all_numbers_div_by_2_or_7(15)
    print()

    # # Testing Exercise 2
    # print(number_as_text(7))
    # print(number_as_text(42))
    # print(number_as_text(24680))
    # print(number_as_text(13579))

    # # Testing Exercise 3
    # print(find_all_divisors(6))
    # print(find_all_divisors(28))
    # print(find_all_divisors(12))
    # print(find_all_divisors(36))

    # print(calc_perfect_numbers(1000))
    # print(calc_perfect_numbers(10000))


    # # Testing Exercise 4
    # print(calc_primes_up_to(15))
    # print(calc_primes_up_to(25))
    # print(calc_primes_up_to(50))

    # # Testing Exercise 5
    # print(is_prime(23))
    # print(prime_number_pairs("twin", 50))
    # print(prime_number_pairs("cousin", 50))
    # print(prime_number_pairs("sexy", 50))


    # # Testing Exercise 6
    # print(calc_checksum("11111"))
    # print(calc_checksum("87654321"))

    # # Testing Exercise 7 a)
    # 
    # from Roman number to Number 
    # print(from_roman_number("XXX"))
    # print(from_roman_number("XVII")) 
    # print(from_roman_number("CDXLIV")) 
    # print(from_roman_number("MCMLXXI"))
    # print(from_roman_number("MMXX"))

    # # Testing Exercise 7 b)
    # 
    # from Number to Roman number 
    # Not 100% correct, still need to handle the edge cases
    # print(to_roman_number(147))
    # print(to_roman_number(17))
    # print(to_roman_number(444))
    # print(to_roman_number(1971))
    # print(to_roman_number(2020))

    # # Testing Exercise 8 a)

    # print(solve_quadratic_simple())
    # print("\n\n\FFF\n\n")
    # print(solve_quadratic_optimized())
    

    # # Testing Exercise 8 b)

    # print(solve_cubic())

    # # Testing Exercise 9
    # print(calc_armstrong_numbers())

    # # Bonus Exercise 9 *

    # # Testing Exercise 10 (Max Change Calculator)
    # print(calc_max_possible_change([1,2,3,7]))
    # print(calc_max_possible_change([1,2,3,8]))


    # # Testing Exercise 11 (Related Numbers)
    # print(divisors(1)) 
    # print(divisors(10))
    # print(divisors(15))
    # print(divisors(25))
    # print(divisors(26))
    print(calc_friends(300))
    x = calc_friends(300)
    print((284,220) in x)

    # print(sum(divisors(220)))
    # print("284")


    # print(divisors(220))









if __name__ == "__main__":
    main()