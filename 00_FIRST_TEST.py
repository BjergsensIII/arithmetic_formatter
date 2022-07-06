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

def arithmetic_arranger(problems, a=None):

  #variables
  topNumber = ""
  bottomNumber = ""
  lines = ""
  solutionNumber = ""
  resolution = ""
  result = ""
    #error too many problems
  if len(problems) >= 5:
    return "Too many problems."

    #loop for receiving numbers
  for problem in problems:
    firstNumber = ""
    operator = ""
    secondNumber = ""
    firstNumber = problem.split()[0]
    operator = problem.split()[1]
    secondNumber = problem.split()[2]

    
    #conditional error
    if firstNumber.isdigit() and secondNumber.isdigit():
      if len(firstNumber) > 4 or len(secondNumber) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
      return "Error: Numbers must only contain digits."
    if operator == "+":
      result = str(int(firstNumber) + int(secondNumber))
    elif operator == "-":
      result = str(int(firstNumber) - int(secondNumber))
    else:
      return "Error: Operator must be '+' or '-'."

    # distance needed for different length of numbers
    distance = max(len(firstNumber), len(secondNumber)) + 2

    #operation system
    if problem != problems[-1]:
      topNumber = topNumber + str(firstNumber.rjust(distance)) + "    "
      bottomNumber = bottomNumber + operator + str(secondNumber.rjust(distance - 1)) + "    "
      lines = lines + "-" * (distance) + "    "
      solutionNumber = solutionNumber + result.rjust(distance) + "    "
    else:
      topNumber = topNumber + str(firstNumber.rjust(distance))
      bottomNumber = bottomNumber + operator + str(secondNumber.rjust(distance - 1))
      lines = lines + "-" * (distance)
      solutionNumber = solutionNumber + result.rjust(distance)


    #result
    if a == True:
      resolution = topNumber + "\n" + bottomNumber + "\n" + lines + "\n" + solutionNumber
    else:
      resolution = topNumber + "\n" + bottomNumber + "\n" + lines + "\n" 
    return resolution