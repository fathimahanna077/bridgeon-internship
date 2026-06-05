class InvalidMarkError(Exception):
    passmark=int(input("Enter mark:"))
mark=int(input("Enter mark:"))
if mark>100:
    raise InvalidMarkError("Mark cannot be above 100")
print("valid mark")