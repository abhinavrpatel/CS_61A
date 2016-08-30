def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    lcm, found, multiplier = a, False, 1
    if b > a:
        lcm = b
    while not found:
        one_cond_met = lcm * multiplier % b == 0
        sec_cond_met = lcm * multiplier % a == 0
        if one_cond_met and sec_cond_met:
            lcm *= multiplier
            found = True
        else:
            multiplier += 1
    return lcm






def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    uniques = []
    divisor = 1
    while not divisor * 10 > n:
        divisor *= 10
    while divisor >= 1:
        digit = int(n // divisor)
        n -= divisor * digit
        exists = False
        for unique in uniques:
            if unique == digit:
                exists = True
        if not exists:
            uniques.append(digit)
        divisor //= 10
    return len(uniques)



