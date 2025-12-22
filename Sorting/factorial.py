def factorial_iter(n):
    result = 1

    for i in range(n):
        result *= (i+1)
    
    return(result)


def factorial_recur(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n-1)


print(factorial_iter(5))
print(factorial_recur(5))