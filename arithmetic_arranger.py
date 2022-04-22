def arithmetic_arranger(problems, answer=False):

  ## Check number of equations
  if len(problems) > 5:
    return "Error: Too many problems."

  ## break out the equations
  first_operand = []
  operator = []
  second_operand = []

  for x in problems:
    y = x.split()
    first_operand.append(y[0])
    operator.append(y[1])
    second_operand.append(y[2])
  
  ## Check operand type
  for x in operator:
    if x not in ['+','-']:
      return "Error: Operator must be '+' or '-'."

  ## Check operands are only digits
  all_operands = first_operand + second_operand
  for x in all_operands:
    if not x.isdecimal():
      return "Error: Numbers must only contain digits."

  ## Check the number of digits in each operand
  for x in all_operands:
    if len(x) > 4:
      return "Error: Numbers cannot be more than four digits."

  ## Arrange arithmetic problems
  problemsCount = len(operator)
  iteration_list = list(range(problemsCount))
  len_list = []
  for x in iteration_list:
    first_operand_len = len(first_operand[x])
    second_operand_len = len(second_operand[x])
    if first_operand_len > second_operand_len:
      len_list.append(first_operand_len)
    else:
      len_list.append(second_operand_len)
  
  first_row = ''
  second_row = ''
  third_row = ''
  solution_row = ''

  ## Arrange third row
  for x in iteration_list:
    a = len_list[x] + 2
    third_row = third_row + "-"*a + " "*4
  third_row = third_row[:-4]
  
  ## Arrange first row
  for x in iteration_list:
    a = len_list[x] + 2
    b = len(first_operand[x])
    spaces = a - b
    first_row += " "*spaces + first_operand[x] + " "*4
  first_row = first_row[:-4]
