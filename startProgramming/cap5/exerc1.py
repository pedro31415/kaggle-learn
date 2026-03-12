def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False
        
numbers = [14,21,30,28]
numbers_null = []
print(has_lucky_number(numbers))
print(has_lucky_number(numbers_null))