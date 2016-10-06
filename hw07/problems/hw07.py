class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """
    def __init__(self):
        self.value = 0

    def next(self):
        if self.value == 0:
            fib = Fib()
            fib.previous = self.value
            fib.value = 1
            return fib
        self.value, self.previous = self.previous + self.value, self.value
        return self


    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, food_type, unit_price):
        self.food = food_type
        self.price = unit_price
        self.credit = 0
        self.inventory = 0

    def vend(self):
        if self.inventory == 0:
            if not self.credit:
                return 'Machine is out of stock.'
            c = self.credit
            self.credit = 0
            return 'Machine is out of stock. Here is your ${0}.'.format(c)

        if self.credit >= self.price:
            self.credit -= self.price
            self.inventory -= 1
            if self.credit == 0:
                return 'Here is your {0}.'.format(self.food)
            else:
                change = self.credit
                self.credit = 0
                return 'Here is your {0} and ${1} change.'.format(self.food, change)
        return 'You must deposit ${0} more.'.format(self.price - self.credit)


    def deposit(self, amount):
        self.credit += amount
        if self.inventory == 0:
            c = self.credit
            self.credit = 0
            return 'Machine is out of stock. Here is your ${0}.'.format(c)
        return 'Current balance: ${0}'.format(self.credit)

    def restock(self, amount):
        self.inventory += amount
        return 'Current {0} stock: {1}'.format(self.food, self.inventory)


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        message = message[len(magic_word):]
        if hasattr(self.obj, message):
            return getattr(self.obj, message)(*args)
        return 'Thanks for asking, but I know not how to ' + message + '.'
