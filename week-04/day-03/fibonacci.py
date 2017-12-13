def fibonacci_start_one(n):
    if n > 35:
        return "Too big!"
    if n <= 0:
        return None
    if n == 2 or n == 1:
        return 1
    return fibonacci_start_one(n - 1) + fibonacci_start_one(n - 2)
