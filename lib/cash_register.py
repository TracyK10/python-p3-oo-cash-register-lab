#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.items = []
        self.transactions = []
        self.total = 0

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append(item)
        transaction_total = price * quantity
        self.total += transaction_total
        self.transactions.append(transaction_total)
        return self.total

    def apply_discount(self):
        if self.discount:
            discount_amount = int(self.total * self.discount / 100)
            self.total -= discount_amount
            self.total = int(self.total)  # Ensure the total is an integer
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
        return self.total

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
        else:
            print("No transactions to void.")
        return self.total
