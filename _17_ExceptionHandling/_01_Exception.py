# print(10/0)  ZeroDivisionError: division by zero

# Basic Syntax
# try:
#     # risky code
# except:
#     # error handling code

try: 
  num=int(input("Enter the number"))
  print(10/num)
except:
  print("something went wrong")  
