x = 0
while x<=150:
    color = '\033['+str(x)+'m'
    print(str(x) + color + "XXX")
    x+=1
