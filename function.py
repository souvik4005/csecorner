def add_num(a,b):
    return(a+b)
print(add_num(5,5))
print(add_num(45,5))

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

def square(num):
    return num ** 2

print(square(6))
#factorial
def factorial(n):
    fact=1
    for i in range (1,n+1):
      fact*=i
    return fact
print(factorial(4))

#prime number 
def is_prime(n):
    if n<=1:
       return False
    for i in range(2,int(n**0.5)+1):
        if i%2==0:
            return False
    return True
print(is_prime(3))
print(is_prime(8))

#reverse sting 
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

#sum number 
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4]))

# max number
def find_max(numbers):
    return max(numbers)

print(find_max([4, 9, 1, 7]))


#palindram 
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))

#fibonachi
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))  # Output: first 10 Fibonacci numbers
 
#length 
def word_count(sentence):
    words = sentence.split()
    return len(words)

print(word_count("I love Python programming"))

#gcd 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))

# Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

print(c_to_f(100))


# file handalng

# Writing student data to a file
students = ["Souvik", "Anita", "Rahul"]

with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

# Reading back
with open("students.txt", "r") as file:
    print(file.read())
