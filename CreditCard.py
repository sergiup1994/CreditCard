class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit, balance = 0):

    
        """
        The initial balance is zero.

        customer   the name of the customer (e.g, 'John Bowman')
        bank       the name of the bank(e.g 'California Savings')
        acnt       the account identifier (e.g., '5391 0375 9387 5309')
        limit      credit limit (measured in dollars)
        """


        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

        def get_customer(self):
            """Return name of the customer"""
            return self._customer

        def get_bank(self):
            """Return the bank's name."""
            return self._bank


        def get_account(self):
            """Return the card identifying number (typically stored as a string)."""
            return self._account

        def get_limit(self):
            """Return current credit limit"""
            return self._limit

        def get_balance(self):
            """Return currrent balance"""
            return self._balance


        def charge(self, price):
            """ Charge given price to the card, assuming sufficient credit limit

            Return True if charge was processed, False if charge was denied 
            """
            if not isinstance(price, (int, float)):
                raise TypeError('price must be numeric')

            if price + self._balance > self.limit:
                return False
            else:
                self._balance += price
                return True
        
        def make_payment(self, amount):

            if not isinstance(amount,(int, float)):
                raise TypeError('amount must be numeric')
            """Process customer payment that reduces balance"""

            elif amount < 0:
                raise ValueError('amount must be positive')

            self._balance -= amount


        if __name__ == '__main__':
            wallet = []
            wallet.append(CreditCard('John Bowman', 'California Savings', '2343 2343 4754 4365', 2500))
            wallet.append(CreditCard('John Bowman', 'California Federal', '2343 2341 4353 0987', 3500))
            wallet.append(CreditCard('John Bowman', 'California Finance', '2343 5464 4353 0987', 5000))


            for val in range(1, 69):
                wallet[0].charge(val)
                wallet[1].charge(2*val)
                wallet[2].charge(3*val)

            for c in range(3):
                print('Customer = ', wallet[c].get_customer())
                print('Bank = ', wallet[c].get_bank())
                print('Account =', wallet[c].get_account())
                print('Limit =', wallet[c].get_balance())
                while wallet[c].get_balance()>100:
                    wallet[c].make_payment(100)
                    print('New Balance =', wallet[c].get_balance())
                print()

