def simpson_n(f, a: float, b: float, n: int) -> float:
    delta = (b-a)/n

    # integral = (f(a) + f(b) + 4summa(f((a+b)/2)))*(b-a)/6

    result = .0
    for i in range(n):
        result += f(a+i*delta) + 4*f(a+(i+0.5)*delta) + f(a+(i+1)*delta)

    return delta*(result)/6


def simpson_2n(f, a: float, b: float, n: int) -> float:
    delta = (b-a)/n
    result = f(a)+f(b)

    # integral = (b-a)/3(f(0)+f(2i) + 4*summa(f(2i-1)) + 2*summa(f(2i)))
    # from 1 to N-1

    for i in range(1, n):
        odd_even = 2 + 2*(i % 2)
        result += odd_even*f(a+i*delta)

    return result*delta/3
