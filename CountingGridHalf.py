number = ["\n"]


c = 0
v = 0
while c != 10:
    for i in range(10):
        if i == 0 and len(number) == 1:
            number.append("00")

        elif ((i*10)+i-c) < v:
            pass
        else:
            number.append((i*10)+i - c)
    c+=1
    v+=10
    number.append("\n")    
    
    


print(" ".join(str(i) for i in number))
