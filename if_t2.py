a = input ("text 1 ")
b = input ("text 2 ")
print(type(a))
print(type(b))
def function (x,y):
    if (type(x)!= str or type(y)!= str):
        return 0
    elif x == y:
        return 1
    elif len(x) > len(y):
        return 2
    elif y == "learn":
        return 3
    else:
        return "else"
res = function (a,b)
print (res)