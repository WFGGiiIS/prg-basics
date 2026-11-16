def sum_natural(n):
    result = n
    if n > 1:
        return result + sum_natural(n-1)

print(sum_natural(10))