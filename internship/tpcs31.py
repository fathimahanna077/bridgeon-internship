lists=[45,46,43,40,45,44,41,36,40,48]
total=sum(lists)
print(total)
count=len(lists)
print(count)
average=total/count
print(average)
lists=[45,46,43,40,45,44,41,36,40,48]
highest=max(lists)
lowest=min(lists)
print(highest)
print(lowest)
new=list(set(lists))
print(new)
above_average=[]
for m in lists:
    if m>average:
        above_average.append(m)
print(above_average)
print("__LIST__")
print("average:",average)
print("highest:",highest)
print("lowest:",lowest)
print("no duplicates:",new)
print("above average:",above_average)
        