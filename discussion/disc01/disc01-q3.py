def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"

    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return True
        k = k + 1
    return False
