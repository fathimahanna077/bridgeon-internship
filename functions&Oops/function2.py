double=lambda x:x*2
print(double(5))

names=["Hanna","Ali","alfam","John"]
result=sorted(names,key=lambda x:len(x))
print(result)

nums=[1,2,3,4,5]
result=list(map(lambda x:x**2,nums))
print(result)

nums=[1,2,-3,-4,-5,6,0,-9]
result=list(filter(lambda x:x>0, nums))
print(result)

square=lambda x:x**2
print(square(4))

def check_number(x):
    if x>0:
        return "positive"
    else:
        return "negative"
print(check_number(-5))
