from typing import List

def factorize(number: int) -> List[int]:
    i = 2
    result = []
    while i * i <= number:
        if number % i != 0:
            i += 1
        else:
            number //= i
            result.append(i)
    if number > 1:
        result.append(number)
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))