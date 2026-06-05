nums=[1,2,3,4,5]
result=list(map(lambda x:x*2,nums))
print(result)

names=["hanna","dasom","fida","alfam"]
result=list(map(lambda x:x.upper(), names))
print(result)

nums=[1,2,3,4,5,6]
result=list(filter(lambda x: x%2==0, nums))
print(result)

nums=[-5,-1,-4,-6,3,4,6,-7,8,1]
result=list(filter(lambda x:x>0,nums))
print(result)


