#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction_price = 0
    self.last_transaction_quantity = 1

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
      self.last_transaction_price = price
      self.last_transaction_quantity = quantity

  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total * (1 - self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_price * self.last_transaction_quantity
    for i in range(self.last_transaction_quantity):
      self.items.remove(self.items[-1])
    if len(self.items) == 0:
      self.total = 0


