def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    def gen():
        done = 0
        m_iter = iter(s)
        while done < k:
            yield next(m_iter)
            done += 1
        raise ValueError()
    return gen()


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    appeared = []
    try:
        for temp in t:
            if not appeared:
                appeared = [temp]
                continue


            if len(appeared) + 1 == k and temp in appeared:
                return appeared[0]
            elif temp in appeared:
                appeared.append(temp)
            else:
                appeared = [temp]
    except StopIteration:
        pass





def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
#     Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.

    while n > 1:
        yield n
        if n % 2 == 1:
            n = 1 + n * 3
            continue
        if n % 2 == 0:
            n //= 2
            continue
    yield 1 #base case ending
