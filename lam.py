def math(func, iter):
    result = []
    for item in iter:
        new_item = func(item)
        result.append(new_item)
    return(result)

lam = [3, 5, 7, 9]

cubed = math(lambda x: x**3, lam)

print(cubed)