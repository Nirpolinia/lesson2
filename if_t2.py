a = input ("text 1 ")
b = input ("text 2 ")
print(type(a))
print(type(b))
def function (x,y):
    if (type(x)!= str or type(y)!= str):
        return 0
    else:
        if x == y:
            return 1
        else:
            if len(x) > len(y):
                return 2
            else:
                if y == "learn":
                    return 3
res = function (a,b)
print (res)