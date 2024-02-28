class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):
    line_item = ''
    total_amount = 0
    printing = self.category.center(30, "*") + "\n"
    
    for x in self.ledger:
      fl_amount = '{:.2f}'.format(x['amount'])
      
      total_amount = total_amount + float(fl_amount)
      
      number_length = len(fl_amount)
      description_length = len(str(x['description']))
      
      line_item = line_item + str(x['description'][:23]) + ' ' +  (' ' * (29 - number_length - description_length)) + fl_amount + '\n'
    printing = printing + line_item + 'Total: ' + str(total_amount)
    return printing

  def deposit(self, amount, description = ''):
    transaction = {'amount': amount, 'description': description}
    self.ledger.append(transaction)

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item['amount']
    return balance

  def check_funds(self, amount):
    bal = self.get_balance()
    if amount > bal:
      return False
    else:
      return True

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      transaction = {'amount': amount * - 1, 'description': description}
      self.ledger.append(transaction)
      return True
    else:
      return False

  def transfer(self, amount, target):
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to {}'.format(target.category))
      target.deposit(amount, 'Transfer from {}'.format(self.category))
      return True
    else:
      return False


def create_spend_chart(categories):
  spend = {}
  for category in categories:
    total_spend = 0
    for transaction in category.ledger:
      if transaction['amount'] < 1:
        total_spend = total_spend + (transaction['amount'] * - 1)
      spend[str(category.category)] = total_spend

  dictionary = {}
  overall = 0
  for key, value in spend.items():
    overall = overall + value

  for key, value in spend.items():
    num = round((value/overall) * 100, 0)
    dictionary[key] = int(num - (num % 10))

  dict_keys = []
  for k in dictionary.keys():
    dict_keys.append(k)

  row_labels = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| ', ' 30| ', ' 20| ',  ' 10| ',  '  0| ']

  chart = 'Percentage spent by category\n'

  bar_chart = [0 for x in range(len(dictionary))]

  letters = '0123'
  row_template = ''

  for x in range(len(dictionary)):
    row_template = row_template + letters[x] + '  '

  for row in row_labels:
    this_row = row + row_template + '\n'
    if this_row.startswith('100'):
      max_row_len = len(this_row)

    for idx, cat in enumerate(bar_chart):
      if cat == 0:
        if dictionary[dict_keys[idx]] == int(row.split('|')[0].lstrip()):
          this_row = str(this_row[:4]) + this_row[4:].replace(str(idx), 'o')
          bar_chart[idx] = 1
        else:
          this_row = str(this_row[:4]) + this_row[4:].replace(str(idx), ' ')
      elif cat == 1:
        this_row = str(this_row[:4]) + this_row[4:].replace(str(idx), 'o')

    chart = chart + this_row

  chart = chart + '    ' + ('-' * (max_row_len - 5))

  max_length = 0
  for name in dict_keys:
    name_len = len(name)
    if name_len > max_length:
      max_length = name_len

  titles = ''
  curr_row = 0
  while curr_row < max_length:
    this_row = '     '
    for x in dict_keys:
      if curr_row < len(x):
        this_row = this_row + str(x)[curr_row] + '  '
      else:
        this_row = this_row + ' ' + '  '
    titles = titles + this_row + '\n'
    curr_row += 1

  titles = titles.rstrip('\n')
  chart = chart + '\n' + titles
  return chart