memo = {}

def solved_fib(n):
    if n < 2:
        return 1
    if(n in memo):
        return memo[n]
    result = solved_fib(n - 1) + solved_fib(n - 2)
    memo[n] = result
    return result