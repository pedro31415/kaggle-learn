print("Hello World")
print(3 ** 3)

partition = 10
result = 10 + partition

print(result)

# functions 
def add_three(input_var):
    final_result = input_var + 3
    return final_result

first_value = 12
result_function = add_three(first_value)
print(result_function)

def print_hello():
    print("Hello World")

print_hello()
print_hello()

# Question 1
def get_expected_cost(beds, baths):
    beds = beds * 30000
    baths = baths * 10000
    house = 80000
    final_house = house + baths + beds

    return final_house

my_house = get_expected_cost(3,1)
print(my_house)

# Data Types
number = 23
float_number = 34.5
name = "Pedro"
phrase = "My name is Pedro"
booleanvalue = True
chactere = "P"

test_number = 4 > 5

print(test_number)

print(type(number))
print(type(float_number))
print(type(name))
print(type(phrase))
print(booleanvalue)
print(type(chactere))

# Conditions 
def add_three_or_eight(inputValue):
    if(inputValue < 10):
        result = inputValue + 3
    elif(inputValue >= 10):
        result = inputValue + 8   
    
    return result


teste = add_three_or_eight(40)
print(teste)

# Question 1

def get_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = 'C'
    elif score >= 60 and score <= 69:
        grade = 'D'
    else:
        grade = 'F'

    return grade 


my_result_school = get_grade(97)
print(my_result_school)

# List in python
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
print(type(flowers_list))

print(flowers_list[5])

tuplas = (1, 'Name', True)
print(type(tuplas))