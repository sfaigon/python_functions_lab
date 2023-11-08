# Challenge 1
def sum_to(num):
    total = 0
    while num > 0:
        total += num
        num -= 1
    print(total)
sum_to(6)
sum_to(10)

# Challenge 2

def largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    print(largest)
largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])

# Challenge 3

def occurrences(string, occ):
    count = 0
    while occ in string:
        string = string.replace(occ, "",1)
        count += 1
    print(count)
occurrences('fleep floop', 'e')
occurrences('fleep floop', 'p')
occurrences('fleep floop', 'ee')
occurrences('fleep floop', 'fe')

# Challenge 4

def product(*args):
    sum = 1
    for num in args:
        sum *= num
    print(sum)

product(-1, 4) 
product(2, 5, 5) 
product(4, 0.5, 5) 

# Bonus

def steps_to_zero(num):
    next_num = 0
    count = 1
    while num != 0:
        if num % 2 == 0:
            next_num = int(num / 2)
            print(f"Step {count}) {num} is even; divide by 2 and obtain {next_num}")
            count +=1
            num = next_num
        else:
            next_num = num - 1
            print(f"Step {count}) {num} is odd; subtract 1 and obtain {next_num}")
            count += 1
            num = next_num
steps_to_zero(14)