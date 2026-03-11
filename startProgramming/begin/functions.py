# help(print)

# help(pow)
# help(round)
def least_difference(a,b,c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return max(diff1, diff2, diff3)

help(least_difference)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), 
)

def my_name(name="pedro"):
    print("Hello, my name is", name)

my_name()