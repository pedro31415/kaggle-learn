# Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!
# In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(numerical):
    if numerical > 0:
        return 1
    elif numerical == 0:
        return 0
    else:
        return -1

print(sign(0))