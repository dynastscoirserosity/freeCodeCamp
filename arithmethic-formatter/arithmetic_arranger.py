import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub
}

def arithmetic_arranger(problems, answer = False):
  error = 0
  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''

  if len(problems) > 5:
    error = 1
  else:
    for problem in problems:
      cond_array = problem.split(' ')
      first_no = cond_array[0]
      sec_no = cond_array[2]
      sign = cond_array[1]

      if not(str(first_no).isnumeric() and str(sec_no).isnumeric()):
        error = 2
        break

      if len(first_no) > 4 or len(sec_no) > 4:
        error = 3
        break

      if sign != '+' and sign != '-':
        error = 4
        break

  if error == 0:
    for index, problem in enumerate(problems):
      cond_array = problem.split(' ')
      first_no = cond_array[0]
      sec_no = cond_array[2]
      sign = cond_array[1]

      if len(first_no) > len(sec_no):
        longest_no = first_no
      else:
        longest_no = sec_no

      problem_width = len(longest_no) + 2
      first_line = first_line + (' ' * (problem_width - len(first_no))) + first_no
      second_line = second_line + sign + (' ' * (problem_width - len(sec_no) - 1)) + sec_no
      third_line = third_line + '-' * problem_width

      if answer == True:
        problem_answer = str(ops[sign](int(first_no), int(sec_no)))
        fourth_line = fourth_line + (' ' * (problem_width - len(problem_answer))) + problem_answer
        if index < len(problems) - 1:
          fourth_line = fourth_line + '    '
      else:
        fourth_line = ''

      if index < len(problems) - 1:
        first_line = first_line + '    '
        second_line = second_line + '    '
        third_line = third_line + '    '

    if answer == True:
      arranged_problems = first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
    else:
      arranged_problems = first_line + '\n' + second_line + '\n' + third_line
    return arranged_problems
  elif error == 1:
    msg = 'Error: Too many problems.'
    return msg
  elif error == 2:
    msg = 'Error: Numbers must only contain digits.'
    return msg
  elif error == 3:
    msg = 'Error: Numbers cannot be more than four digits.'
    return msg
  elif error == 4:
    msg = "Error: Operator must be '+' or '-'."
    return msg