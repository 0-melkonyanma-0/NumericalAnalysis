def trapezodial(f, a: float, b: float, n: int) -> float:
    # delta height of the trapezoid
    delta = (b-a)/n

    # integral summ
    # Kotes formula
    # ((f(a)+f(b))/2 + summa(1,n-1) f_i) * h:

    result = (f(a)+f(b))/2

    for i in range(1, n):
        result += f(a+delta*i)

    return delta*result
