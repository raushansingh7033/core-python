marks={
  "Raushan":100,
  "Ram":90,
  "Raj":20
}


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Raushan" : 90})
print(marks)

print(marks.get("Raushan"))
print(marks["Raushan"])