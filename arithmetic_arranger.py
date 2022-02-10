def calculate_answer(x, y, c):
  """Calculates the total or difference of two numbers"""
  if c == "+":
    answer = x + y
  else:
    answer = x - y

  return answer

def arithmetic_arranger(problems, show_answers = False):
  line1 = ""
  line2 = ""
  dash_line = ""
  answer_line = ""
  arranged_problems = ""
  problem_count = 0 

  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    problem_count += len(problems)
  
  for i in range(len(problems)):
    problem = problems[i]
    problem = problem.replace(",", "").replace(" ", "")
    
    for c in problem:
      if c.isalpha():
        return "Error: Numbers must only contain digits."
      elif not c.isdigit() and c != "+" and c != "-":
        return "Error: Operator must be '+' or '-'."
    j = 0
    space = " "
    dashes = "-"   
    for c in problem:  
      if c == "+" or c == "-":
        x = problem[0:j]
        y = problem[j + 1:]
        if len(x) > 4 or len(y) > 4:
          return "Error: Numbers cannot be more than four digits."
        answer = calculate_answer(int(x), int(y), c)
        answer = str(answer)
        if len(x) == len(y):
          row1 = (space * 2) + x
          row2 = c + space + y
        elif len(y) > len(x):
          difference = len(y) - len(x)
          row1 = (space * 2) + (space * difference) + x
          row2 = c + space + y
        else:
          difference = len(x) - len(y)
          row1 = (space * 2) + x
          row2 = c + space + (space * difference) + y
        
        if len(row2) >= len(answer):
          difference = len(row2) - len(answer)
        answers = (space * difference) + answer
        line1 += row1 
        line2 += row2 
        dash_line += dashes * len(row2)
        answer_line += answers 
        problem_count -= 1
        if problem_count > 0:
          line1 += "    "
          line2 += "    "
          dash_line += "    "
          answer_line += "    "   

      j += 1
  arranged_problems += line1 + "\n" + line2 + "\n" + dash_line 
  if show_answers is True:
    return arranged_problems + "\n" + answer_line             
  return arranged_problems 
   
      

      







