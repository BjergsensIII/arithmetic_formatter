#      235
#    +  52
#    -----
#      ***
#max number 4 digit.
#operator on second line (y number) with 1 space from the 4th digit.

#if more than 5 error on the input... return = Error: "Too many problems."

#accept + and - anything else return = "Error: Operator must be '+' or '-'."

#numeri allineati a destra

#4 space between each problem

#dashes between the calculation and the result long as the problem is

#FUNCTION CALL   
#--> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

#optionally second argument.. set to true and the function will do the calculation

#FUNCTION CALL 
#--> arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
#--------------------------------------------------------------------------------#

def arithmetic_arranger(problems, solver = False):

  #variables
  topNumber = ""
  bottomNumber = ""
  lines = ""
  solutionNumber = ""
  resolution = ""
  solution = ""
  firstNumber = ""
  operator = ""
  secondNumber = ""
    #error too many problems
  if len(problems) > 5:
    return "Error: Too many problems."

  #loop for receiving numbers
  for problem in problems:
    firstNumber = problem.split()[0]
    operator = problem.split()[1]
    secondNumber = problem.split()[2]
    
    # distance needed for different length of numbers
    spaces = max(len(firstNumber), len(secondNumber)) + 2
    
    #conditional error
    if firstNumber.isdigit() and secondNumber.isdigit():
      if len(firstNumber) > 4 or len(secondNumber) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
      return "Error: Numbers must only contain digits."
    #operator error
    if operator == "+":
      solution = str(int(firstNumber) + int(secondNumber))
    elif operator == "-":
      solution = str(int(firstNumber) - int(secondNumber))
    else:
      return "Error: Operator must be '+' or '-'."
    
    #operation system
    if problem != problems[-1]:
      topNumber += str(firstNumber.rjust(spaces)) + "    "
      bottomNumber += operator + str(secondNumber.rjust(spaces - 1)) + "    "
      lines += "-" * (spaces) + "    "
      solutionNumber += solution.rjust(spaces) + "    "
    else:
      topNumber += str(firstNumber.rjust(spaces))
      bottomNumber += operator + str(secondNumber.rjust(spaces - 1))
      lines += "-" * (spaces)
      solutionNumber += solution.rjust(spaces)


    #result
  if solver == True:
    resolution = topNumber + "\n" + bottomNumber + "\n" + lines + "\n" + solutionNumber
  else:
    resolution = topNumber + "\n" + bottomNumber + "\n" + lines
  return resolution