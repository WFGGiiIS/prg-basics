e_n = int(input("Enter the number to convert: "))
result = []

def divide(k):
    k = k / 2
    return int(k)


while e_n > 1:
    if e_n % 2 == 0:
        result.append("0")
        e_n = divide(e_n)
    elif e_n % 2 != 0:
        result.append("1")
        e_n = divide(e_n)

if e_n == 1:
    result.append("1")
reversed_result = result[::-1]
print(reversed_result)