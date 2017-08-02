def solved_fib(n, memo = {}):
    if n < 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = solved_fib(n - 1, memo) +\
                 solved_fib(n - 2, memo)
        memo[n] = result
        return result