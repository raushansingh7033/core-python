class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise InvalidAgeError("You must be 18+")

print("Access granted")