filepath="sigma.txt"
unicorn=[]
with open(filepath,"r") as fileReader:
    content= fileReader.readlines()
    print(content, end="")