nums=[1,2,3,4,5]

largest=nums[0]
second_largest=nums[0]

for num in nums:
   if num>largest:
    second_largest=largest
    largest=num
   elif num>second_largest and num!=largest:
        second_largest=num
print("second largest:",second_largest) 
