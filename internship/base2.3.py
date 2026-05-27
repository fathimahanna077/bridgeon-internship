numbers=[]
for i in range(5):
 num=int(input("enter a number:"))
numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
total_sum=0
even_count=0
even_count=0
odd_count=0
for num in numbers:
    total_sum += num
if num>largest:
    largest=num
if num<smallest:
    smallest=num
if num%2==0:
    even_count+=1
else:
    odd_count+=1
print("\n---Results---")
print("numbers list:",numbers)
print("largest number:",largest)
print("smallest number:",smallest)
print("sum of numbers:",total_sum)
print("even numbers count:",even_count)
print("odd numbers count:",odd_count)





