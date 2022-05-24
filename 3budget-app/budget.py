class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(abs(amount)):
      amount = -abs(amount)
      self.ledger.append({"amount": amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_cat.category}")
      budget_cat.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    balance = self.get_balance()
    if balance >= amount:
      return True
    else:
      return False

  def __str__(self):
    line = f"{self.category}"
    line = line.center(30, "*") + '\n'

    for item in self.ledger:
      left = f"{item['description'][:23]}"
      left = left.ljust(23, " ")
      right = f"{item['amount']:.2f}"
      right = right.rjust(7, " ")
      line += left + right + '\n'

    total = float()
    for item in self.ledger:
      total += item['amount']
    line += f"Total: {total}"
    return line



def create_spend_chart(categories):
  line = "Percentage spent by category\n"

  cat_percentages = {}
  total_expenses = float()
  
  for category in categories:
    category_expenses = float()
    for item in category.ledger:
      if item['amount'] < 0:
        category_expenses += abs(item['amount'])
        total_expenses += abs(item['amount'])
    cat_percentages[f'{category.category}'] = category_expenses

  for each in cat_percentages:
    cat_percentages[each] = cat_percentages[each] / total_expenses * 100

  percent_tranches = [*range(0, 101, 10)]
  percent_tranches.reverse()

  
  for each in percent_tranches:
    row = str(each).rjust(3)
    nline = f'{row}| '
    for x in cat_percentages:
      if cat_percentages[x] >= each:
        nline += "o  "
      else:
        nline += "   "
    line += nline + '\n'    

  #break
  dash_break = "    -" + (len(cat_percentages))*"---"
  line = line + dash_break + '\n'

  category_list = []
  for x in cat_percentages:
    category_list.append(x)
  max_len = len(max(category_list, key=len))

  for i in range(max_len):
    nline = " "*5
    for x in category_list:
      if i < len(x):
        nline += x[i] + " "*2
      else:
        nline += " "*3
    line += nline + '\n'
  line = line[:-3] + ' '*2
  
  return line