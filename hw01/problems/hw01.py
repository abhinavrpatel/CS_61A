from operator import add, sub


def a_plus_abs_b(a, b):
    if b < 0:
        f = lambda x, y: sub(x, y)
    else:
        f = lambda a, b: add(a,b)
    return f(a, b)




def two_of_three(a, b, c):
    return sub(add(a*a, b*b, c*c), min(a,b,c))






def largest_factor(n):
    if n <= 1:
        return 1

    i = n - 1;
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
    #>>> if_function(True, 2, 3)
    2
    #>>> if_function(False, 2, 3)
    3
    #>>> if_function(3==2, 3+2, 3-2)
    1
    #>>> if_function(3>2, 3+2, 3-2)
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
        return f()





def with_if_function():
    return if_function(c(), t(), f())




def c():
    "*** YOUR CODE HERE ***"
    return 1


def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    print('hello darkness my old friend')
    return 0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    #>>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    #>>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        print (n + '\n')
        steps += 1
    return steps
