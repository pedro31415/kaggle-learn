def is_valid_zip(zip_code):
    zip_code = str(zip_code)

    if len(zip_code) == 5:
        for char in zip_code:
            if char < '0' or char > '9':
                return False
        return True
    else:
        return False


ex1 = "1234x"
print(is_valid_zip(ex1))
ex2 = "12344"
print(is_valid_zip(ex2))
ex3 = "12344444"
print(is_valid_zip(ex3))