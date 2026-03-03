try:
  num=int(input("Enter the number"))
  print(10/num)
except ZeroDivisionError as e :
  print(e)