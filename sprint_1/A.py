
def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    # y = ax2 + bx + c
    y = (a * x**2) + (b*x) + c
    return y

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))