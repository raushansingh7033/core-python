try:
  num=int(input("Enter the number"))
  print(num/10)
except :
  print("not divide by zero") 
finally:
  print("this will always execute")           