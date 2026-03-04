marks=[12,3,50,30,98,20,30]

index=0
for mark in marks:
  print(mark)
  if(index==3):
    print("Raushan , awesome")
  index+=1

# by enumerate()
for index,mark in enumerate(marks):
  print(mark)
  if(index==3):
    print("Raushan , awesome")
   