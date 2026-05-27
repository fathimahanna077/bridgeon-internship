char="programming"
count=0
for letters in char:
    if letters in "a,e,i,o,u":
        count+=1
        print(count)