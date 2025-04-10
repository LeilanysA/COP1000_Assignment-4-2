# Inputs 
employeeName = input("Enter the employee's name: ")
numShifts = int(input("Enter the number of shifts worked: "))
numTranscations = int(input("Enter the number of transcations: "))
transcationValues = float(input("Enter the total dollar value of transcations: "))

# IF and ELSE statements
if numShifts > 0 and numTranscations > 0:
    productivityScore = (transcationValues / numTranscations) / numShifts

    if productivityScore <= 30:
        bonus = 50.00
    else:
      if productivityScore <= 69:
        bonus = 75.00
      else:
        if productivityScore <= 199:
          bonus = 100.00
        else:
          bonus = 200.00
# Final output
print(f"Employee Name: {employeeName}")
print(f"Employee Bonus: ${bonus}")
