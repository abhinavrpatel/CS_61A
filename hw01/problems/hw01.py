from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda x, y: sub(x, y)
    else:
        f = lambda x, y: add(x, y)
    return f(a, b)




def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a + b*b + c*c - min(a,b,c)**2






def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"

    if n <= 1:
        return 1

    i = n - 1
    found = False
    while not found:
        if n % i == 0 or i == 1:
            found = True
        else:
            i -= 1
    return i










def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result





def with_if_statement(): #THIS ONE MUST RETURN THE NUMBER ONE
    """
    #>>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f() #f() is not executed





def with_if_function():
    # Python will execute c(), t(), f() and pass the results
    # into if_function
    return if_function(c(), t(), f())




def c():
    "*** YOUR CODE HERE ***"
    return True


def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    print('hello darkness my old friend\n\n')
    print('f() is being executed right now and printing this line\n\n')
    return 0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps = 0
    while True:
        print(n)
        steps += 1 #one step = one iteration of the loop
        if n == 1:
            break #the only desired exit condition
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1



    return steps
