planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet)

# use tuple -> immmutable value
multiplicands = (2,2,2,3,3,5)
product = 1

for mult in multiplicands:
    product = product * mult

print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

for i in range(5):
    print(f"Brazil is {i} cup world")

# list comprehensions
squares  = [n**2 for n in range(10)]

even_numbers = [n * 2 for n in range(11)]

print(squares)
print(even_numbers)

numbers = [0,1,2,3,4,5,6,7,8,9,10]

square_even_numbers = [number**2 for number in numbers if number % 2 == 0]
print(square_even_numbers)
    