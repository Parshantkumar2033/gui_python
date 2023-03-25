string = '34+523'
for i in range(len(string)):
    if string[i] == "+":
        print(string[0:i])
        print(string[i+1:])
        print(string[-1])
