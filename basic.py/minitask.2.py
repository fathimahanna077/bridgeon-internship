year=int(input("2024"))
if(year % 4==0 and year % 100!=0 or (year % 400 ==0):
   print(f"{year} a leap year.")
else:
   print(f"{year} not a leap year.")
   
