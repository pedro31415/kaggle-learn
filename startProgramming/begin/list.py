primes = [2, 3, 5, 7]

print(primes)
print(type(primes))

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

print(hands[2][2])

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Using slicing
close_sun = planets[0:3]
print(close_sun)

close_earth = planets[1:4]
print(close_earth)

primes.append(11)
print(primes)

print(sorted(primes))

print(len(primes))

first_number = bin(5)
print(first_number)

real_number = (5).bit_length()
print(real_number) 