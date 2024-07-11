number=input("Enter a number: ")
numStr = str(number)

digitList = []
    

for digit in numStr:
    digitList.append(int(digit))

list.reverse(digitList)
print(digitList) 

count=0
for i in digitList:
    count=count+1
    if count==3:
        print(i)
        digitList.insert(i,",")
        print(digitList)