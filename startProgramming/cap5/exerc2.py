def elementwise_greater_than(L, thresh):
    for index, i in enumerate(L):
        if i > thresh:
            L[index] = True
        else:
            L[index] = False
    return L

list_numbers = [1,2,3,4]
thresh = 2

print(elementwise_greater_than(list_numbers, thresh))
