def mid_rect(f, a: float, b: float, n: int) -> float:
    # delta height of rectangles
    delta = (b-a)/n
    result = .0

    # integral sum
    # summa = deltaf(xi-1+xi)/2 from 1 to n-1
    for i in range(n):
        result += f(a+(1/2+i)*delta)*delta

    return result
