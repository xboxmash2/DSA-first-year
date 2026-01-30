def is_armstrong(num):
    original = num
    num_digits = len(str(num))
    sum_of_powers = 0

    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_digits
        num //= 10

    return original == sum_of_powers


test_num = 153
print(f"{test_num} is armstrong: {is_armstrong(test_num)}")

def is_palindromic(num):
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num


test_num = 12321
print(f"{test_num} is palindromic: {is_palindromic(test_num)}")

num = 345621
r_num = 0

while num > 0:
    digit = num % 10
    r_num = r_num * 10 + digit
    num //= 10

print(r_num)

n = 345621
counter = 0

while n > 0:
    n //= 10
    counter += 1

print(counter)

binary="1011"
dec=""
for i in range(len(binary),0,-1):
    dec= dec+binary[i]*2**i
