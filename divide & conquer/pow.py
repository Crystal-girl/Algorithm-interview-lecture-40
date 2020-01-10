"""
leetcode 50
Pow
"""

"""
recursion solution
"""
def pow(self, x: float, n: int) -> float:
    if not n:
        return 1
    if n < 0:
        return 1 / self.pow(x, -n)
    if n % 2:
        return x * self.pow(x*x, (n-1)/2)
    return self.pow(x*x, n/2)


"""
non-recursion solution
"""
def pow(self, x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
