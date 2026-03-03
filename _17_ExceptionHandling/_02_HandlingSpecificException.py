try:
  num=int(input("Enter the number"))
  print(10/num)
except ZeroDivisionError:
  print("you can not divide by zero")
except ValueError:
  print("invalid input ! please enter the integer")      