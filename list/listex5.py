# 4-3. Counting to twenty: Use a for loop to print the numbers from 1 to 20, inclusive
figures = []
for value in range(1, 21):
    figures.append(value)
print(figures)

"""
4-4. One million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window. Then use the min() and 
max() functions to make sure that your list starts from 1 and ends at 1,000,000. Also use the sum() function to see how
quickly Python can add a million numbers.
"""
one_million = []
for value in range(1, 1000001):
    one_million.append(value)
print(one_million)
print(min(one_million))  # 1
print(max(one_million))  # 1000000
print(sum(one_million))  # 500000500000

# 4-6. Odd numbers: Use the third argument of the range() function to make a list of odd numbers from 1 to 20. Use a for
# loop to print each number.
odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use the for loop to print the numbers in a list.
threes = []
for value in range(3, 30, 3):
    threes.append(value)
print(threes)  # [3, 6, 9, 12, 15, 18, 21, 24, 27]

"""
4-8. Cubes: A number raised to the third power is called a cube. Make a list of the first 10 cubes (that is the cube of
each integer from 1 through 10), and use a for loop to print out the value of each cube.
"""
cubes = []
for integer in range(1, 10):
    cubes.append(integer ** 3)
print(cubes)  # [1, 8, 27, 64, 125, 216, 343, 512, 729]

# 4-9. Cube comprehension: Use a list comprehension to generate a list of the first ten cubes
ten_cubes = [integer ** 3 for integer in range(1, 10)]
print(ten_cubes)  # [1, 8, 27, 64, 125, 216, 343, 512, 729]







